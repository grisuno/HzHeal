# root

*Community 0 | 2 files | cohesion 1.00*

## Definition

This community groups 2 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `generar_y_reproducir`, `main`, `obtener_tasa_muestreo_valida`, `reproducir_tono`. Core file: `app.py` (4 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 4 | no |
| `install.sh` | sh | utility | 0 | no |

## Key Symbols

- `obtener_tasa_muestreo_valida` (function, `app.py:35`) `def obtener_tasa_muestreo_valida(dispositivo)` - Obtiene una tasa de muestreo válida para el dispositivo
- `reproducir_tono` (function, `app.py:43`) `def reproducir_tono(tono, dispositivo, tasa_muestreo)` - Función para reproducir en segundo plano
- `generar_y_reproducir` (function, `app.py:55`) `def generar_y_reproducir(frecuencia_izquierda, frecuencia_derecha, duracion, amp` - Genera y reproduce un tono mono o binaural
- `main` (function, `app.py:100`) `def main()`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `app.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `install.sh`
