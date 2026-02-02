# Guía del Profesor - EDA II

> ⚠️ **DOCUMENTO PRIVADO** - No compartir con estudiantes

---

## Estructura de Repositorios

```
UNAM-FI-EDAII-2026-1/
│
├── eda-2 (PRIVADO) ← ESTE REPO - VERSIÓN COMPLETA
│   ├── libro/              # Libro LaTeX completo
│   ├── 00-introduccion/    # Todos los capítulos
│   ├── 01-ordenamiento/    # Con soluciones incluidas
│   │   ├── notas/
│   │   ├── practicas/
│   │   ├── tareas/
│   │   ├── src/
│   │   └── soluciones/     # ⚠️ Respuestas (NO copiar al público)
│   ├── ...
│   ├── PROFESOR.md         # Este archivo (NO copiar)
│   └── examenes/           # Exámenes con respuestas (NO copiar)
│
├── eda-2-2026-2 (PÚBLICO) ← TEMPLATE INCREMENTAL
│   │   # Misma estructura que eda-2, pero:
│   │   # - Sin carpetas soluciones/
│   │   # - Sin PROFESOR.md
│   │   # - Sin examenes/
│   │   # - Se va llenando conforme avanza el semestre
│   ├── libro/
│   ├── 00-introduccion/
│   ├── 01-ordenamiento/
│   │   ├── notas/
│   │   ├── practicas/      # Solo esqueletos, sin soluciones
│   │   ├── tareas/
│   │   └── src/
│   └── ...
│
└── eda-2-2026-2-<usuario> (PRIVADO, generado por Classroom)
    └── (copia del template para cada estudiante)
```

**Regla:** `eda-2-2026-2` es espejo de `eda-2` EXCEPTO:
- ❌ `soluciones/` en cada tema
- ❌ `PROFESOR.md`
- ❌ `examenes/`
- ❌ Cualquier archivo con respuestas

---

## Flujo de Trabajo Semestral

### 1. Inicio del Semestre

1. **Crear repo público** `eda-2-2026-2` en la organización
2. **Marcarlo como Template** en Settings → Template repository
3. **Crear classroom** en [classroom.github.com](https://classroom.github.com):
   - New Classroom → Seleccionar organización
   - Nombre: "EDA II 2026-2"
4. **Crear assignment**:
   - New Assignment → Individual
   - Template: `eda-2-2026-2`
   - Visibilidad: Private
   - Admin access: habilitado
5. **Push inicial** al template (solo estructura base):
   ```bash
   cd ~/eda-2-2026-2
   # Copiar README, ENTREGAS, RUBRICA (sin PROFESOR.md)
   # Copiar libro/ y 00-introduccion/
   git add .
   git commit -m "Estructura inicial del curso"
   git push
   ```

### 2. Sincronizar Repos (Cada vez que publicas material)

#### Script para copiar de eda-2 → eda-2-2026-2:

```bash
#!/bin/bash
# sync_to_public.sh
# Ejecutar desde la raíz de eda-2

SOURCE="/Users/rod/eda-2/repos"
DEST="/Users/rod/eda-2-2026-2"  # Ajustar ruta

# Archivos/carpetas a EXCLUIR
EXCLUDE=(
    "PROFESOR.md"
    "soluciones"
    "examenes"
    ".git"
)

# Construir opciones de rsync
EXCLUDE_OPTS=""
for item in "${EXCLUDE[@]}"; do
    EXCLUDE_OPTS="$EXCLUDE_OPTS --exclude=$item"
done

# Sincronizar
rsync -av --delete $EXCLUDE_OPTS "$SOURCE/" "$DEST/"

echo "✅ Sincronizado. Ahora haz commit en eda-2-2026-2"
```

#### Uso:
```bash
# 1. Trabajas en eda-2 (este repo)
# 2. Cuando esté listo para publicar:
./sync_to_public.sh

# 3. Ve al repo público y haz push:
cd ~/eda-2-2026-2
git add .
git commit -m "Agregar práctica 01"
git push
```

### 3. Los Estudiantes Sincronizan

Ellos deben tener configurado el template como remote:
```bash
# Solo la primera vez:
git remote add template https://github.com/UNAM-FI-EDAII-2026-1/eda-2-2026-2.git

# Cada vez que hay nuevo material:
git pull template main
```

### 4. Revisar Entregas

1. **Ver dashboard** en GitHub Classroom
2. **Clonar para revisar** (si necesario):
   ```bash
   # GitHub Classroom tiene opción de descargar todos los repos
   ```
3. **Los tests corren automáticamente** con GitHub Actions
4. **Dar feedback** directamente en el repo del estudiante (Issues o PR comments)

### 4. Calificaciones

1. Ver resultados de tests en cada repo
2. Exportar desde GitHub Classroom (CSV)
3. Ajustar por rúbrica manual si aplica

---

## Comandos Útiles

### Compilar libro completo
```bash
cd libro
make clean && make
open build/main.pdf
```

### Compilar solo un capítulo (debug)
```bash
cd 01-ordenamiento/notas
pdflatex debug.tex
open debug.pdf
```

### Ver estado de entregas
```bash
# En GitHub Classroom → Assignment → Ver submissions
```

### Actualizar template desde este repo
```bash
./sync_to_public.sh
cd ~/eda-2-2026-2
git add . && git commit -m "Actualizar material" && git push
```

---

## Estructura de Cada Tema

```
XX-tema/
├── notas/
│   ├── capitulo.tex      # Capítulo del libro (con ejercicios al final)
│   └── debug.tex         # Para compilación rápida
├── practicas/
│   └── practica_XX/
│       ├── README.md     # Instrucciones
│       ├── src/          # Esqueleto para estudiantes
│       └── tests/        # Tests automáticos
├── tareas/
│   └── tarea_XX.md       # Instrucciones (ejercicios en el libro)
├── src/                  # Código de ejemplo para clase
├── tests/                # Tests del código de ejemplo
└── soluciones/           # ⚠️ NO SUBIR AL TEMPLATE
    ├── practica_XX_sol.py
    └── tarea_XX_sol.pdf
```

---

## Checklist por Semana

- [ ] Preparar material de la semana (notas, ejemplos)
- [ ] Compilar libro si hubo cambios
- [ ] Publicar práctica/tarea si aplica
- [ ] Actualizar template público
- [ ] Notificar a estudiantes
- [ ] Revisar entregas de semana anterior
- [ ] Subir calificaciones

---

## Configuración de GitHub Actions

Los tests de prácticas corren automáticamente. El workflow está en:
```
.github/workflows/tests.yml
```

Para agregar tests de una nueva práctica, asegúrate de que:
1. El archivo de test esté en `practicas/practica_XX/tests/`
2. Siga el patrón `test_*.py`
3. Use pytest

---

## Notas Importantes

1. **Nunca subir soluciones al template público**
2. **Verificar que los tests no revelen la solución**
3. **Mantener sincronizados los ejercicios del libro con las tareas**
4. **Respaldar calificaciones fuera de GitHub**

---

## Contacto de Emergencia

- GitHub Education: education@github.com
- Soporte GitHub Classroom: classroom.github.com/help
