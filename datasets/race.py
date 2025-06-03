from pathlib import Path
from typing import Any

import jsonlines

from .base import BaseDataset


class RaceDataset(BaseDataset):
    """
    Dataset for RACE. Expects a JSONL file and template.
    """

    default_data_path = Path(__file__).parent.parent / "data" / "race.jsonl"
    default_template_path = (
        Path(__file__).parent.parent / "templates" / "race" / "prediction_task.j2.md"
    )

    def load_data(self) -> list[dict[str, Any]]:
        with jsonlines.open(self.data_path, "r") as reader:
            return [obj for obj in reader]
