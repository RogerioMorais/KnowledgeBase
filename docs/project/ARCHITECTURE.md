# Arquitetura da KnowledgeBase

## ADR-001 — Linguagem

### Decisão

A ferramenta será desenvolvida em Python.

### Motivo

- Excelente suporte a processamento de texto.
- Ecossistema maduro para Markdown e YAML.
- Fácil execução via Docker.

Status

Aceito

---

## ADR-002 — Execução

### Decisão

O Python será executado exclusivamente em Docker.

### Motivo

- Não exigir instalação local.
- Ambiente reproduzível.
- Facilita colaboração.

Status

Aceito

---

## ADR-003 — Metadados

### Decisão

As KB utilizarão YAML Front Matter.

### Motivo

- Compatível com o ecossistema Markdown.
- Fácil leitura com PyYAML.
- Permite futura integração com MkDocs, Obsidian, Hugo etc.

Status

Aceito

---

## ADR-004 — Manipulação de arquivos

### Decisão

Utilizar pathlib.

### Motivo

- API moderna.
- Código mais legível.
- Recomendação da documentação oficial do Python.

Status

Aceito