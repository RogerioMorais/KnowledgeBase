from pathlib import Path
import sys

from rich.console import Console
from rich.table import Table

from lib.filesystem import find_markdowns
from lib.parser import load

console = Console()


def main():

    ids = {}
    titles = {}

    errors = []

    table = Table(title="KnowledgeBase Validation")

    table.add_column("Documento")
    table.add_column("Status")

    for markdown in find_markdowns(Path("docs")):

        try:

            kb = load(markdown)

            if kb.id in ids:
                errors.append(
                    f"ID duplicado: {kb.id}"
                )

            else:
                ids[kb.id] = markdown

            if kb.title in titles:
                errors.append(
                    f"Título duplicado: {kb.title}"
                )

            else:
                titles[kb.title] = markdown

            table.add_row(
                markdown.name,
                "[green]OK[/green]"
            )

        except Exception as ex:

            errors.append(
                f"{markdown.name}: {ex}"
            )

            table.add_row(
                markdown.name,
                "[red]ERRO[/red]"
            )

    console.print(table)

    console.print()

    if errors:

        console.print("[red]Erros encontrados[/red]\n")

        for error in errors:
            console.print(f"- {error}")

        sys.exit(1)

    console.print("[green]Nenhum erro encontrado.[/green]")


if __name__ == "__main__":
    main()