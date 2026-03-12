# Ejecutar Tests de Grafos

## Problema Común: ModuleNotFoundError

Si ves este error:
```
ModuleNotFoundError: No module named 'src'
```

Es porque Python no encuentra el módulo `src` desde el directorio de tests.

## Solución 1: Usar PYTHONPATH (Recomendado)

### En terminal (macOS/Linux):
```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
PYTHONPATH=. python -m unittest discover -s tests -v
```

### En terminal (Windows PowerShell):
```powershell
cd C:\ruta\a\eda-2\03-grafos
$env:PYTHONPATH = "."
python -m unittest discover -s tests -v
```

### En terminal (Windows CMD):
```cmd
cd C:\ruta\a\eda-2\03-grafos
set PYTHONPATH=.
python -m unittest discover -s tests -v
```

## Solución 2: Usar pytest (Más simple)

Pytest maneja automáticamente los paths:

```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
pytest tests/ -v
```

Con cobertura:
```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
pytest tests/ -v --cov=src --cov-report=term-missing
```

## Solución 3: Agregar __init__.py

Crea archivos `__init__.py` vacíos para que Python reconozca los directorios como paquetes:

```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
touch __init__.py
touch src/__init__.py
touch tests/__init__.py
```

Luego ejecuta normalmente:
```bash
python -m unittest discover -s tests -v
```

## Solución 4: Modificar imports en los tests

En lugar de:
```python
from src.grafo_matriz import GrafoMatriz
```

Usa imports relativos o agrega el path manualmente:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.grafo_matriz import GrafoMatriz
```

## Ejecutar un test específico

### Con unittest:
```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
PYTHONPATH=. python -m unittest tests.test_grafo_matriz -v
```

### Con pytest:
```bash
cd /Users/rod/clases/eda2/eda-2/03-grafos
pytest tests/test_grafo_matriz.py -v
```

## Ejecutar desde el directorio raíz

Si quieres ejecutar desde `/Users/rod/clases/eda2/eda-2/`:

```bash
PYTHONPATH=03-grafos python -m unittest discover -s 03-grafos/tests -v
```

O con pytest:
```bash
cd 03-grafos && pytest tests/ -v
```

## Instalar pytest si no lo tienes

```bash
pip install pytest pytest-cov
```

## Recomendación

**Usa pytest** - es más moderno, flexible y maneja mejor los paths:

```bash
cd 03-grafos
pytest tests/ -v --cov=src
```

## En GitHub Actions

El workflow ya está configurado para manejar esto correctamente usando:
```yaml
env:
  PYTHONPATH: ${{ github.workspace }}/03-grafos
```
