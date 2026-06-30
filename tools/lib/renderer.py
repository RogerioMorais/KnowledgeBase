from collections import defaultdict

from lib.models import KnowledgeBase


def _group_by_category(items: list[KnowledgeBase]) -> dict[str, list[KnowledgeBase]]:

    groups = defaultdict(list)

    for item in items:
        groups[item.category].append(item)

    return dict(sorted(groups.items()))


def render_readme(items: list[KnowledgeBase]) -> str:

    groups = _group_by_category(items)

    lines = []

    lines.append("# KnowledgeBase")
    lines.append("")
    lines.append("Base de conhecimento sobre Inteligência Artificial, Direito Digital, Arquitetura de Software e Segurança.")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Estatísticas")
    lines.append("")
    lines.append(f"Total de documentos: **{len(items)}**")
    lines.append("")

    for category, docs in groups.items():
        lines.append(f"- {category}: {len(docs)}")

    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Índice")
    lines.append("")

    for category, docs in groups.items():

        lines.append(f"### {category}")
        lines.append("")

        for doc in docs:
            lines.append(f"- {doc.id} - {doc.title}")

        lines.append("")

    return "\n".join(lines)


def render_summary(items: list[KnowledgeBase]) -> str:

    groups = _group_by_category(items)

    lines = []

    lines.append("# Summary")
    lines.append("")

    for category, docs in groups.items():

        lines.append(f"## {category}")
        lines.append("")

        for doc in docs:

            relative = str(doc.path).replace("\\", "/")

            lines.append(
                f"- [{doc.id} - {doc.title}]({relative})"
            )

        lines.append("")

    return "\n".join(lines)