from collections.abc import Sequence
from pathlib import Path
from typing import Any, Optional

from jinja2 import Environment, FileSystemLoader, StrictUndefined, Template


class BaseDataset(Sequence[dict[str, Any]]):
    """
    Base class for all datasets. Handles loading, template rendering, and pre-rendered outputs.

    Attributes:
        default_data_path: Path to the dataset file. Should be set in subclass.
        default_template_path: Path to the Jinja2 template file. Should be set in subclass.
    """

    default_data_path: Optional[str | Path] = None
    default_template_path: Optional[str | Path] = None

    def __init__(
        self,
        data_path: Optional[str | Path] = None,
        template_path: Optional[str | Path] = None,
    ):
        """
        Initialize dataset, loading data and pre-rendering all items.

        Args:
            data_path: Override for dataset file path.
            template_path: Override for template file path.

        Raises:
            ValueError: If either data or template path cannot be found.
        """
        self.data_path = Path(data_path or self.default_data_path)
        self.template_path = Path(template_path or self.default_template_path)

        if self.data_path.suffix != ".jsonl":
            raise ValueError(
                f"Dataset file must be a JSONL file, got: {self.data_path.suffix}"
            )
        if not self.data_path.exists():
            raise ValueError(f"Dataset file not found: {self.data_path}")
        if not self.template_path.exists():
            raise ValueError(f"Template file not found: {self.template_path}")
        self.template: Template = self.load_template(self.template_path)
        self._data: list[dict[str, Any]] = self.load_data()
        self._rendered_data: list[dict[str, Any]] = self._pre_render()

    def load_template(self, template_path: Path) -> Template:
        """
        Load the Jinja2 template with strict undefined variable checking.
        """
        env = Environment(
            loader=FileSystemLoader(template_path.parent), undefined=StrictUndefined
        )
        return env.get_template(template_path.name)

    def load_data(self) -> list[dict[str, Any]]:
        """
        Load data as a list of dicts.
        Must be implemented by subclasses.
        """
        raise NotImplementedError

    def _pre_render(self) -> list[dict[str, Any]]:
        """
        Pre-render all items in the dataset with the template.
        Each returned dict has:
            - All original fields
            - __rendered_text: The rendered string from the template
            - __instance_index: Zero-based instance index
        """
        rendered: list[dict[str, Any]] = []
        for idx, instance in enumerate(self._data):
            rendered_text: str = self.template.render(instance)
            item: dict[str, Any] = dict(instance)  # Copy all fields
            item["__rendered_text"] = rendered_text
            item["__instance_index"] = idx
            rendered.append(item)
        return rendered

    def __getitem__(self, idx: int) -> dict[str, Any]:
        """
        Return pre-rendered dict for instance at given index.
        """
        return self._rendered_data[idx]

    def __len__(self) -> int:
        """
        Return number of items in the dataset.
        """
        return len(self._rendered_data)
