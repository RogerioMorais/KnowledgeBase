from pathlib import Path

import yaml

from lib.models import KnowledgeBase


REQUIRED_FIELDS = (
    "id",
    "title",
    "category",
)


def load(path: Path) -> KnowledgeBase:
    """
    Carrega uma Knowledge Base a partir de um arquivo Markdown com
    Front Matter YAML.
    """

    text = path.read_text(encoding="utf-8")

    # O arquivo deve iniciar com o delimitador do Front Matter
    if not text.lstrip().startswith("---"):
        raise ValueError("Front Matter não encontrado.")

    parts = text.split("---", 2)

    if len(parts) < 3:
        raise ValueError("Front Matter inválido.")

    try:
        metadata = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as ex:
        raise ValueError(f"Erro ao ler YAML: {ex}")

    for field in REQUIRED_FIELDS:
        if not metadata.get(field):
            raise ValueError(f"Campo obrigatório '{field}' não encontrado.")

    tags = metadata.get("tags", [])

    if tags is None:
        tags = []

    if not isinstance(tags, list):
        raise ValueError("O campo 'tags' deve ser uma lista.")

    return KnowledgeBase(
        id=str(metadata["id"]),
        title=str(metadata["title"]),
        category=str(metadata["category"]),
        status=str(metadata.get("status", "draft")),
        tags=tags,
        path=path,
    )