from dataclasses import dataclass, field


@dataclass
class KnowledgeBase:

    id: str

    title: str

    category: str

    path: str

    status: str = ""

    tags: list[str] = field(default_factory=list)
    