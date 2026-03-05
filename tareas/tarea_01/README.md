# Tarea 1: Análisis de Algoritmos de Ordenamiento

**Valor:** 5% de la calificación final  
**Fecha de entrega:** Semana 4  
**Modalidad:** Individual

> 📖 **Referencia:** Capítulo 2 del libro - Métodos de Ordenamiento (Sección Ejercicios)

---

## Parte 1: Análisis teórico (40 puntos)

*Resuelve los siguientes ejercicios del libro (Capítulo 2 - Ejercicios Teóricos):*

### Pregunta 1.1 (10 pts) - Ejercicio 1 del libro
Ilustra la operación de Insertion Sort sobre el arreglo A = ⟨31, 41, 59, 26, 41, 58⟩.
Además, demuestra matemáticamente que tiene complejidad O(n²) en el peor caso.

### Pregunta 1.2 (10 pts) - Ejercicios 5-6 del libro
Usando el modelo del libro, ilustra Merge Sort sobre A = ⟨3, 41, 52, 26, 38, 57, 9, 49⟩.
Escribe la recurrencia T(n) = 2T(n/2) + O(n) y resuélvela usando el teorema maestro.

### Pregunta 1.3 (10 pts) - Ejercicios 14-15 del libro
Ilustra Partition sobre A = ⟨13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11⟩.
¿Por qué Quick Sort tiene O(n²) en el peor caso pero O(n log n) en promedio?

### Pregunta 1.4 (10 pts) - Ejercicio 8 del libro
Demuestra que ningún algoritmo de ordenamiento basado en comparaciones puede tener 
complejidad mejor que Ω(n log n). (Hint: usa el argumento del árbol de decisión)

---

## Parte 2: Análisis experimental (40 puntos)

*Basado en Ejercicios de Programación 1-2 del Capítulo 2*

### Ejercicio 2.1 (20 pts)
Implementa los siguientes algoritmos y mide su tiempo de ejecución:
- Insertion Sort
- Merge Sort
- Quick Sort (pivote fijo)
- Quick Sort (pivote aleatorio) - *Ver ejercicio 16 del libro*
- Heap Sort

Usa los siguientes tamaños de entrada: n = 1000, 2000, 5000, 10000, 20000

### Ejercicio 2.2 (10 pts)
Genera una gráfica comparativa del tiempo vs tamaño de entrada para los 5 algoritmos.

### Ejercicio 2.3 (10 pts)
Repite el experimento con:
- Listas ya ordenadas
- Listas en orden inverso
- Listas con muchos elementos repetidos

¿Cómo cambia el comportamiento de cada algoritmo?

---

## Parte 3: Aplicación - Problemas LeetCode (20 puntos)

*Basado en la sección "Problemas de LeetCode" del Capítulo 2*

### Ejercicio 3.1 (10 pts) - LeetCode 912
Implementa tu solución para "Sort an Array" usando Merge Sort o Quick Sort.
NO uses la función de ordenamiento integrada.

### Ejercicio 3.2 (10 pts) - LeetCode 75
Resuelve "Sort Colors" (problema de la bandera holandesa).
Ordena un arreglo con valores 0, 1, 2 en un solo recorrido (in-place).

---

## Formato de Entrega

```
tarea_01/
├── respuestas.md      # Respuestas a Parte 1
├── experimentos.py    # Código de la Parte 2
├── graficas/
│   ├── comparacion.png
│   └── casos_especiales.png
├── leetcode_912.py    # Solución LeetCode 912
└── leetcode_75.py     # Solución LeetCode 75
```

## Rúbrica

| Sección | Puntos |
|---------|--------|
| Parte 1: Análisis teórico (Ejercicios del libro) | 40 |
| Parte 2: Análisis experimental | 40 |
| Parte 3: Problemas LeetCode | 20 |
| **Total** | **100** |
