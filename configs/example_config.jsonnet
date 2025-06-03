{
    output_dir: 'results/qwen',
    model_id: 'Qwen/Qwen2.5-0.5B-Instruct',
    temperature: 0.0,
    max_tokens: 512,
    tensor_parallel_size: 1,
    gpu_memory_utilization: 0.9,
    dtype: 'auto',
    max_model_len: 8192,
    system_message: null,
    datasets: ['hellaswag', 'race', 'wandi', 'logic'],
    dataset_path: null,
    template_path: null,
}
