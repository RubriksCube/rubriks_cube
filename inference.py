"""
inference.py

Batch inference utility for vLLM and custom datasets.

Features:
- Supports one or more predefined datasets with built-in or user-provided template/dataset paths.
- Uses vLLM for fast, memory-efficient large language model inference (including batching).
- System message can be specified as a string or file path.
- Prompts are formatted using tokenizer's chat template (if available).
- Supports command-line configuration, as well as config files (JSON/YAML, jsonnet) via jsonargparse.

USAGE GUIDE:

# 1. Multiple datasets (default dataset/template locations)
uv run inference.py --output_dir results --model_id mistralai/Mistral-7B-Instruct-v0.3 --datasets hellaswag wandi

# 2. Single dataset, custom paths
uv run inference.py --output_dir results --model_id mistralai/Mistral-7B-Instruct-v0.3 \
    --dataset logic --dataset_path data/logic_custom.jsonl --template_path templates/logic_custom.jinja

# 3. Use a system message (string or path)
uv run inference.py --output_dir results --model_id mistralai/Mistral-7B-Instruct-v0.3 \
    --dataset hellaswag --system_message "You are a helpful assistant."
uv run inference.py --output_dir results --model_id mistralai/Mistral-7B-Instruct-v0.3 \
    --dataset hellaswag --system_message templates/sysmsg.txt

# 4. Config file (YAML or JSON; CLI args override config file values)
uv run inference.py --config config.yaml

# 5. Help
uv run inference.py --help

"""

import sys
from pathlib import Path
from typing import Any, Optional

import jsonlines
from jsonargparse import ArgumentParser
from transformers import PreTrainedTokenizerBase
from vllm import LLM, SamplingParams

from datasets import HellaswagDataset, LogicDataset, RaceDataset, WandiDataset

DATASET_CLASSES = {
    "hellaswag": HellaswagDataset,
    "wandi": WandiDataset,
    "race": RaceDataset,
    "logic": LogicDataset,
}


def load_system_message(system_message: Optional[str]) -> Optional[str]:
    """
    Load a system message, which can be provided as a string or a file path.

    Args:
        system_message: The system message string or a path to a file.

    Returns:
        The loaded system message as a string, or None if not provided.
    """
    if not system_message:
        return None
    path = Path(system_message)
    if path.exists() and path.is_file():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return system_message


def build_prompts(
    dataset: Any,
    tokenizer: PreTrainedTokenizerBase,
    system_message: Optional[str],
) -> list[str]:
    """
    Construct prompts for each dataset instance, applying chat template if needed.

    Args:
        dataset: An iterable of dataset instances.
        tokenizer: The tokenizer, possibly with apply_chat_template.
        system_message: System message to prepend or add as system role.

    Returns:
        List of prompt strings for generation.
    """
    prompts: list[str] = []
    is_chat_model = hasattr(tokenizer, "apply_chat_template")
    if not is_chat_model:
        print("WARNING: You are not using a chat model.")
    for item in dataset:
        rendered: str = item["__rendered_text"]
        if is_chat_model:
            chat: list[dict[str, str]] = []
            if system_message:
                chat.append({"role": "system", "content": system_message})
            chat.append({"role": "user", "content": rendered})
            prompt: str = tokenizer.apply_chat_template(
                chat, tokenize=False, add_generation_prompt=True
            )
        else:
            prompt = f"{system_message}\n{rendered}" if system_message else rendered
        prompts.append(prompt)
    return prompts


def run_inference_on_dataset(
    dataset_name: str,
    dataset_class: type,
    dataset_path: Optional[str],
    template_path: Optional[str],
    model: LLM,
    tokenizer: PreTrainedTokenizerBase,
    sampling_params: SamplingParams,
    output_path: Optional[Path] = None,
    system_message: Optional[str] = None,
) -> None:
    """
    Run inference on a single dataset and save results to output_path.

    Args:
        dataset_name: Name of the dataset.
        dataset_class: The class object for the dataset.
        dataset_path: Path to dataset file or None for default.
        template_path: Path to template file or None for default.
        model: The loaded vLLM model.
        tokenizer: The tokenizer to format prompts.
        sampling_params: Sampling parameters for generation.
        output_path: Where to save the output jsonl.
        system_message: System message string, or None.
    """
    if output_path.exists():
        print(
            f"SKIP: Output for {dataset_name} already exists at {output_path} (not overwriting)."
        )
        return

    print(f"Running inference for dataset: {dataset_name}")
    dataset = dataset_class(
        data_path=dataset_path,
        template_path=template_path,
    )

    prompts: list[str] = build_prompts(dataset, tokenizer, system_message)
    completions: list[str] = []

    outputs = model.generate(prompts, sampling_params=sampling_params)
    completions = [output.outputs[0].text for output in outputs]

    if output_path:
        results = []
        for item, completion in zip(dataset, completions):
            result = {"completion": completion} | {
                k: v for k, v in item.items() if k != "__rendered_text"
            }
            results.append(result)

        with jsonlines.open(output_path, "w") as writer:
            writer.write_all(results)
    return completions


def make_parser():
    parser = ArgumentParser(parser_mode="jsonnet")
    parser.add_argument(
        "--config", action="config", help="Path to a JSON/YAML config file."
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory to save model predictions.",
    )

    # vLLM specific arguments
    parser.add_argument(
        "--model_id",
        type=str,
        required=True,
        help="Model ID or path (Hugging Face or local).",
    )
    parser.add_argument(
        "--temperature", type=float, default=0.0, help="Sampling temperature."
    )
    parser.add_argument(
        "--max_tokens", type=int, default=512, help="Maximum tokens per completion."
    )
    parser.add_argument(
        "--tensor_parallel_size",
        type=int,
        default=1,
        help="Tensor parallel size for vLLM.",
    )
    parser.add_argument(
        "--gpu_memory_utilization",
        type=float,
        default=0.9,
        help="Fraction of GPU memory to use.",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="auto",
        choices=["auto", "float32", "float16", "bfloat16"],
        help="Data type for vLLM.",
    )
    parser.add_argument(
        "--max_model_len",
        type=int,
        default=8192,
        help=(
            "Maximum model length for vLLM. Reduce it to match input sequences "
            "to reduce KV cache memory utilization."
        ),
    )

    # Dataset arguments
    parser.add_argument(
        "--system_message",
        type=str,
        default=None,
        help="System message as a string or path to a file containing the message.",
    )

    parser.add_argument(
        "--datasets",
        "--dataset",
        nargs="+",
        dest="datasets",
        type=str,
        required=True,
        help="One or more dataset names (predefined only).",
    )
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=None,
        help="Custom dataset path (single dataset only).",
    )
    parser.add_argument(
        "--template_path",
        type=str,
        default=None,
        help="Custom template path (single dataset only).",
    )
    return parser


def main() -> None:
    """
    Run batched inference with vLLM on one or more datasets.
    """
    parser = make_parser()
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    system_message: Optional[str] = load_system_message(args.system_message)

    vllm_kwargs = {
        "tensor_parallel_size": args.tensor_parallel_size,
        "pipeline_parallel_size": 1,
        "gpu_memory_utilization": args.gpu_memory_utilization,
        "dtype": args.dtype,
        "max_model_len": args.max_model_len,
        "enable_prefix_caching": True,
    }

    llm = LLM(model=args.model_id, **vllm_kwargs)

    tokenizer = llm.get_tokenizer()
    sampling_params = SamplingParams(
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )

    # If multiple datasets, don't allow custom dataset/template path
    if len(args.datasets) > 1:
        if args.dataset_path or args.template_path:
            sys.exit(
                "Custom dataset_path/template_path can only be used with a single dataset."
            )

    for dataset_name in args.datasets:
        if dataset_name not in DATASET_CLASSES:
            print(f"WARNING: Unknown dataset '{dataset_name}'. Skipping.")
            continue
        dataset_path = args.dataset_path if len(args.datasets) == 1 else None
        template_path = args.template_path if len(args.datasets) == 1 else None
        output_path = output_dir / f"{dataset_name}.jsonl"
        if output_path.exists():
            print(
                f"SKIP: Output for {dataset_name} already exists at {output_path} (not overwriting)."
            )
            continue

        completions = run_inference_on_dataset(
            dataset_name=dataset_name,
            dataset_class=DATASET_CLASSES[dataset_name],
            dataset_path=dataset_path,
            template_path=template_path,
            model=llm,
            tokenizer=tokenizer,
            sampling_params=sampling_params,
            output_path=output_path,
            system_message=system_message,
        )


if __name__ == "__main__":
    main()
