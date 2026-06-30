from pathlib import Path


def find_markdowns(root: Path) -> list[Path]:
    """
    Retorna todos os arquivos KB-*.md encontrados abaixo do diretório.
    """

    return sorted(root.rglob("KB-*.md"))


def write_file(path: Path, content: str) -> None:
    """
    Escreve um arquivo UTF-8.
    """

    path.write_text(content, encoding="utf-8")