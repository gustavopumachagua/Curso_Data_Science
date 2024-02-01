| **Inicio**            | **atrás 8**                   | **Siguiente 10**                    |
| --------------------- | ----------------------------- | ----------------------------------- |
| [🏠](../../README.md) | [⏪](./8_consultas_JOIN'S.md) | [⏩](./10_consultas_expresiones.md) |

---

# **Lección SQL 8: Una breve nota sobre NULL**

Como prometimos en la última lección, hablaremos rápidamente sobre **NULL** los valores en una base de datos SQL. Siempre es bueno reducir la posibilidad de **NULL** valores en las bases de datos porque requieren atención especial al construir consultas, restricciones (ciertas funciones se comportan de manera diferente con valores nulos) y al procesar los resultados.

Una alternativa a **NULL** los valores en su base de datos es tener valores predeterminados apropiados para el tipo de datos, como 0 para datos numéricos, cadenas vacías para datos de texto, etc. Pero si su base de datos necesita almacenar datos incompletos, entonces los **NULL** valores pueden ser apropiados si los valores predeterminados sesgará el análisis posterior (por ejemplo, al tomar promedios de datos numéricos).

A veces, tampoco es posible evitar **NULL** valores, como vimos en la última lección al unir externamente dos tablas con datos asimétricos. En estos casos, puede probar los **NULL** valores de una columna en una **WHERE** cláusula utilizando la restricción **IS NULL** o **IS NOT NULL**.

```
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```

**Ejercicio**

Este ejercicio será una especie de repaso de las últimas lecciones. Estamos usando la misma tabla de Empleados y Edificios de la última lección, pero hemos contratado a algunos personas más, a quienes aún no se les ha asignado un edificio.

**Table: Buildings**

| **Building_name** | **Capacity** |
| ----------------- | ------------ |
| 1e                | 24           |
| 1w                | 32           |
| 2e                | 16           |
| 2w                | 20           |

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
| Engineer | Yancy I.   |              | 0                  |
| Artist   | Oliver P.  |              | 0                  |

**Ejercicio 8: Tareas**

- **Encuentre el nombre y la función de todos los empleados que no han sido asignados a un edificio**

```
SELECT name, role FROM employees
WHERE building IS NULL;
```

- **Encuentre los nombres de los edificios que no tienen empleados.**

```
SELECT DISTINCT building_name
FROM buildings
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;
```

| **Inicio**            | **atrás 8**                   | **Siguiente 10**                    |
| --------------------- | ----------------------------- | ----------------------------------- |
| [🏠](../../README.md) | [⏪](./8_consultas_JOIN'S.md) | [⏩](./10_consultas_expresiones.md) |

---
