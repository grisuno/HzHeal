# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 2 | **Total Symbols Extracted:** 4 | **Total Imports:** 7

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:75d209c | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Suggested Questions](#suggested-questions)
6. [Hotspot Analysis](#hotspot-analysis)
7. [Change Impact Analysis](#change-impact-analysis)
8. [Suggested Linting Rules](#suggested-linting-rules)
9. [Orphans](#orphans)
10. [Query Recipes](#query-recipes)
11. [Structural Knowledge Map](#structural-knowledge-map)
12. [UML Class Diagram](#uml-class-diagram)
13. [Code Property Graph](#code-property-graph)
14. [Architecture Reference](#architecture-reference)
    - [PY (1 files)](#py-1-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 2 |
| Total Symbols | 4 |
| Total Imports | 7 |
| Call Edges | 84 |
| Inheritance Edges | 0 |
| Languages | 2 |
| Avg Symbols/File | 2.0 |
| Avg Imports/File | 3.5 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `app.py` | 7 | 4 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 2 |

### utility

- `app.py` (py, 4 symbols)
- `install.sh` (sh, 0 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `app.py` | 0.0750 | 0.0000 | 0.0000 | 0.00 | 0.75 |
| 2 | `install.sh` | 0.0000 | 0.0000 | 0.0000 | 0.00 | 0.00 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `app.py` | 0.4 | | 0.0000 |
| `install.sh` | 0.0 | | 0.0000 |

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does app.py depend on, and what depends on it? (0 connections)
- What does install.sh depend on, and what depends on it? (0 connections)
- What is the overall architecture of this codebase?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `app.py` | 1.000 | 1.000 | 1.000 | 4 | 7 |
| `install.sh` | 0.000 | 0.000 | 0.000 | 0 | 0 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `app.py` | 0 | 0 | 0 |
| `install.sh` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM001` | info | Large number of functions in py: 4 total | py | 4 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `install.sh` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

## Structural Knowledge Map

```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    app_py["app.py (py)"]
    class app_py mod;
    app_py_obtener_tasa_muestreo_valida["obtener_tasa_muestreo_valida"]
    class app_py_obtener_tasa_muestreo_valida fn;
    app_py --> app_py_obtener_tasa_muestreo_valida
    app_py_reproducir_tono["reproducir_tono"]
    class app_py_reproducir_tono fn;
    app_py --> app_py_reproducir_tono
    app_py_generar_y_reproducir["generar_y_reproducir"]
    class app_py_generar_y_reproducir fn;
    app_py --> app_py_generar_y_reproducir
    app_py_main["main"]
    class app_py_main fn;
    app_py --> app_py_main
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_numpy["numpy"]
    class ext_numpy ext;
    app_py -.->|imports| ext_numpy
    ext_sounddevice["sounddevice"]
    class ext_sounddevice ext;
    app_py -.->|imports| ext_sounddevice
    ext_time["time"]
    class ext_time ext;
    app_py -.->|imports| ext_time
    ext_rich_console["rich.console"]
    class ext_rich_console ext;
    app_py -.->|imports| ext_rich_console
    ext_rich_progress["rich.progress"]
    class ext_rich_progress ext;
    app_py -.->|imports| ext_rich_progress
    ext_rich_prompt["rich.prompt"]
    class ext_rich_prompt ext;
    app_py -.->|imports| ext_rich_prompt
    ext_threading["threading"]
    class ext_threading ext;
    app_py -.->|imports| ext_threading
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [], "god_nodes": [{"node_id": "app.py", "score": 0.4}, {"node_id": "install.sh", "score": 0.0}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "sounddevice"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "rich.console"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "rich.progress"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "rich.prompt"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "app.py", "target": "threading"}], "generator": "readmenator", "metadata": {"edge_count": 91, "file_count": 2, "language_count": 2, "symbol_count": 4}, "nodes": [{"id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "efacd8207741ae41", "symbol_count": 4, "symbols": [{"doc": "Obtiene una tasa de muestreo válida para el dispositivo", "kind": "function", "line": 35, "name": "obtener_tasa_muestreo_valida", "signature": "def obtener_tasa_muestreo_valida(dispositivo)"}, {"doc": "Función para reproducir en segundo plano", "kind": "function", "line": 43, "name": "reproducir_tono", "signature": "def reproducir_tono(tono, dispositivo, tasa_muestreo)"}, {"doc": "Genera y reproduce un tono mono o binaural", "kind": "function", "line": 55, "name": "generar_y_reproducir", "signature": "def generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha, duracion, amplitud, dispositivo)"}, {"kind": "function", "line": 100, "name": "main", "signature": "def main()"}]}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (1 files)

#### `app.py`
**Path:** `app.py`

**Functions:**
- `obtener_tasa_muestreo_valida` (line 35) `def obtener_tasa_muestreo_valida(dispositivo)` - *Obtiene una tasa de muestreo válida para el dispositivo*
- `reproducir_tono` (line 43) `def reproducir_tono(tono, dispositivo, tasa_muestreo)` - *Función para reproducir en segundo plano*
- `generar_y_reproducir` (line 55) `def generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha, duracion, amplitud, dispositivo)` - *Genera y reproduce un tono mono o binaural*
- `main` (line 100) `def main()`

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
