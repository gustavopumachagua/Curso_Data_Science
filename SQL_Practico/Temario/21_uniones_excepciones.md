| **Inicio**            | **atrás 20**               |
| --------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./20_subconsultas.md) |

---

# **Tema de SQL: uniones, intersecciones y excepciones**

Cuando se trabaja con varias tablas, el operador **UNION** y **UNION ALL** le permite agregar los resultados de una consulta a otra, asumiendo que tienen el mismo número de columnas, orden y tipo de datos. Si usa **UNION** sin **ALL**, las filas duplicadas entre las tablas se eliminarán del resultado.

```
SELECT column, another_column
   FROM mytable
UNION / UNION ALL / INTERSECT / EXCEPT
SELECT other_column, yet_another_column
   FROM another_table
ORDER BY column DESC
LIMIT n;
```

En el orden de las operaciones definido en la Lección 12: Orden de ejecución , **UNION** ocurre antes de **ORDER BY** y **LIMIT**. No es común usar **UNION** correos electrónicos, pero si tiene datos en diferentes tablas que no se pueden unir ni procesar, puede ser una alternativa a realizar múltiples consultas en la base de datos.

De manera similar a **UNION**, el **INTERSECT** operador se asegurará de que solo se devuelvan las filas que sean idénticas en ambos conjuntos de resultados, y el **EXCEPT** operador se asegurará de que solo se devuelvan las filas del primer conjunto de resultados que no estén en el segundo. Esto significa que el **EXCEPT** operador depende del orden de las consultas, como **LEFT JOIN** y **RIGHT JOIN**.

Ambos **INTERSECT** y **EXCEPT** también descartan filas duplicadas después de sus respectivas operaciones, aunque algunas bases de datos también admiten **INTERSECT ALL** y **EXCEPT ALL** permiten retener y devolver duplicados.

| **Inicio**            | **atrás 20**               |
| --------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./20_subconsultas.md) |

---
