from pathlib import Path
import sys

from rich.console import Console

from lib.filesystem import find_markdowns
from lib.filesystem import write_file
from lib.parser import load
from lib.renderer import render_readme
from lib.renderer import render_summary

console = Console()


def main():

    documents = []

    errors = []

    for markdown in find_markdowns(Path("docs")):

        try:

            kb = load(markdown)

            documents.append(kb)

        except Exception as ex:

            errors.append(
                f"{markdown.name}: {ex}"
            )

    documents.sort(key=lambda x: x.id)

    write_file(
        Path("README.md"),
        render_readme(documents)
    )

    write_file(
        Path("SUMMARY.md"),
        render_summary(documents)
    )

    console.print()

    console.print(f"[green]Documentos processados:[/green] {len(documents)}")

    console.print(f"[red]Erros:[/red] {len(errors)}")

    if errors:

        console.print()

        console.print("[yellow]Arquivos ignorados[/yellow]")

        for error in errors:

            console.print(f"- {error}")

        sys.exit(1)

    console.print()

    console.print("[green]README.md atualizado.[/green]")

    console.print("[green]SUMMARY.md atualizado.[/green]")


if __name__ == "__main__":
    main()