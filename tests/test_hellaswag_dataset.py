import jsonlines
import pytest
from jinja2 import exceptions

from datasets.hellaswag import HellaswagDataset


@pytest.fixture
def temp_jsonl(tmp_path):
    # Use unique text for assertions
    data = [
        {
            "ctx_a": "Aliens landed in Tokyo Tower.",
            "ctx_b": "The crowd watched as",
            "endings": [
                "the aliens waved hello.",
                "the sky turned purple.",
                "the police arrived.",
                "a UFO hovered overhead.",
            ],
        }
    ]
    jsonl_path = tmp_path / "unique_hellaswag.jsonl"
    with jsonlines.open(jsonl_path, mode="w") as writer:
        writer.write_all(data)
    return jsonl_path


@pytest.fixture
def temp_template(tmp_path):
    template_content = (
        "SPECIAL_CONTEXT: {{ctx_a}}\n\n"
        "UNIQUE_OPTIONS:\n"
        "A. {{ctx_b}} {{endings[0]}}\n"
        "B. {{ctx_b}} {{endings[1]}}\n"
        "C. {{ctx_b}} {{endings[2]}}\n"
        "D. {{ctx_b}} {{endings[3]}}\n"
    )
    template_path = tmp_path / "custom_hellaswag_template.j2.md"
    template_path.write_text(template_content)
    return template_path


def test_default_template_rendering(temp_jsonl):
    # Instantiate dataset with custom paths
    dataset = HellaswagDataset(data_path=temp_jsonl)

    # Only one item in our temp file
    assert len(dataset) == 1
    item = dataset[0]

    # Rendered keys must exist
    assert "__rendered_text" in item
    assert "__instance_index" in item

    # The rendered text should contain unique parts of our template/data
    rendered = item["__rendered_text"]
    assert "Context: Aliens landed in Tokyo Tower." in rendered
    assert "A. The crowd watched as the aliens waved hello." in rendered
    assert "B. The crowd watched as the sky turned purple." in rendered
    assert "C. The crowd watched as the police arrived." in rendered
    assert "D. The crowd watched as a UFO hovered overhead." in rendered


def test_dataset_uses_given_template(temp_jsonl, tmp_path):
    # Use a very different template to verify template override works
    template_content = "CHECKPOINT: {{ctx_a}} ** {{ctx_b}} => {{endings[1]}}"
    template_path = tmp_path / "alt_template.j2.md"
    template_path.write_text(template_content)

    dataset = HellaswagDataset(data_path=temp_jsonl, template_path=template_path)

    items = list(dataset)
    rendered = items[0]["__rendered_text"]

    assert rendered.startswith("CHECKPOINT:")
    assert "Aliens landed in Tokyo Tower." in rendered
    assert "The crowd watched as" in rendered
    assert "the sky turned purple." in rendered


def test_rendering_error_on_missing_field(temp_jsonl, temp_template, tmp_path):
    # Write a bad JSONL missing ctx_b
    bad_data = [
        {
            "ctx_a": "Aliens landed in Tokyo Tower.",
            # "ctx_b" is missing
            "endings": [
                "the aliens waved hello.",
                "the sky turned purple.",
                "the police arrived.",
                "a UFO hovered overhead.",
            ],
        }
    ]
    bad_jsonl_path = tmp_path / "bad_hellaswag.jsonl"
    with jsonlines.open(bad_jsonl_path, mode="w") as writer:
        writer.write_all(bad_data)

    # Should error when iterating
    with pytest.raises(exceptions.UndefinedError):
        _ = HellaswagDataset(
            data_path=bad_jsonl_path,
        )


def test_dataset_fails_with_non_jsonl(tmp_path):
    # Write a file that is NOT valid JSONL (just some garbage text)
    bad_file = tmp_path / "not_jsonl.txt"
    bad_file.write_text("This is not JSON!\nNor is this.\nJust some text.")

    # Should raise when attempting to load or iterate (since the loader expects JSONL)
    with pytest.raises(ValueError):
        _ = HellaswagDataset(data_path=bad_file)
