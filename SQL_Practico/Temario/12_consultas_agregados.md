| **Inicio**            | **atrás 11**                     | **Siguiente 13**              |
| --------------------- | -------------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./11_consultas_agregado.md) | [⏩](./13_orden_ejecucion.md) |

---

# **Lección SQL 11: Consultas con agregados (Parte 2)**

Nuestras consultas se están volviendo bastante complejas, pero casi hemos presentado todas las partes importantes de una **SELECT** consulta. Una cosa que quizás hayas notado es que si la **GROUP BY** cláusula se ejecuta después de la **WHERE** cláusula (que filtra las filas que se van a agrupar), ¿cómo filtramos exactamente las filas agrupadas?

Afortunadamente, SQL nos permite hacer esto agregando una **HAVING** cláusula adicional que se usa específicamente con la **GROUP BY** cláusula para permitirnos filtrar filas agrupadas del conjunto de resultados.

```
SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
FROM mytable
WHERE condition
GROUP BY column
HAVING group_condition;
```

Las **HAVING** restricciones de la cláusula se escriben de la misma manera que las **WHERE** restricciones de la cláusula y se aplican a las filas agrupadas. Con nuestros ejemplos, esto puede no parecer una construcción particularmente útil, pero si imagina datos millones de filas con diferentes propiedades, a menudo es necesario poder aplicar restricciones adicionales para entender rápidamente los datos.

> **¿Sabías?**
>
> Si no está utilizando la cláusula "GROUP BY", una simple cláusula "WHERE" será suficiente.

**Ejercicio**

Para este ejercicio, profundizará en los datos de los empleados en el estudio de cine. Piensa en las diferentes cláusulas que quieres para cada tarea.

**Table: Employees**

| **Role** | **Name**   | **Building** | **Years_employed** |
| -------- | ---------- | ------------ | ------------------ |
| Engineer | Becky A.   | 1e           | 4                  |
| Engineer | Dan B.     | 1e           | 2                  |
| Engineer | Sharon F.  | 1e           | 6                  |
| Engineer | Dan M.     | 1e           | 4                  |
| Engineer | Malcom S.  | 1e           | 1                  |
| Artist   | Tylar S.   | 2w           | 2                  |
| Artist   | Sherman D. | 2w           | 8                  |
| Artist   | Jakob J.   | 2w           | 6                  |
| Artist   | Lillia A.  | 2w           | 7                  |
| Artist   | Brandon J. | 2w           | 7                  |
| Manager  | Scott K.   | 1e           | 9                  |
| Manager  | Shirlee M. | 1e           | 3                  |
| Manager  | Daria O.   | 2w           | 6                  |

**Ejercicio 11: Tareas**

- **Encuentra la cantidad de artistas en el estudio (sin cláusula HAVING )**

```
SELECT role, COUNT(*) as Number_of_artists
FROM employees
WHERE role = "Artist";
```

- **Encuentre la cantidad de empleados de cada rol en el estudio.**

```
SELECT role, COUNT(*)
FROM employees
GROUP BY role;
```

- **Encuentre el número total de años empleados por todos los ingenieros.**

```
SELECT role, SUM(years_employed)
FROM employees
GROUP BY role
HAVING role = "Engineer";
```

| **Inicio**            | **atrás 11**                     | **Siguiente 13**              |
| --------------------- | -------------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./11_consultas_agregado.md) | [⏩](./13_orden_ejecucion.md) |

---
