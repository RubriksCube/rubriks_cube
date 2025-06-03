from pathlib import Path
from typing import Any

import jsonlines

from .base import BaseDataset


class WandiDataset(BaseDataset):
    """
    Dataset for WANDI. Expects a JSONL file and template.
    """

    default_data_path = Path(__file__).parent.parent / "data" / "wandi.jsonl"
    default_template_path = (
        Path(__file__).parent.parent / "templates" / "wandi" / "prediction_task.j2.md"
    )

    def load_data(self) -> list[dict[str, Any]]:
        with jsonlines.open(self.data_path, "r") as reader:
            return [obj for obj in reader]
