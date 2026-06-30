from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class KnowledgeBase:
    id: str
    title: str
    category: str
    status: str
    tags: list[str] = field(default_factory=list)
    path: Path | None = None