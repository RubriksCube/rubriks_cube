from pathlib import Path
from typing import Any

import jsonlines

from .base import BaseDataset


class HellaswagDataset(BaseDataset):
    """
    Dataset for HellaSwag. Expects a JSONL file and template.
    """

    default_data_path = Path(__file__).parent.parent / "data" / "hellaswag.jsonl"
    default_template_path = (
        Path(__file__).parent.parent
        / "templates"
        / "hellaswag"
        / "prediction_task.j2.md"
    )

    def load_data(self) -> list[dict[str, Any]]:
        with jsonlines.open(self.data_path, "r") as reader:
            return [obj for obj in reader]
