| **Inicio**            | **atrás 10**                        | **Siguiente 12**                  |
| --------------------- | ----------------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./10_consultas_expresiones.md) | [⏩](./12_consultas_agregados.md) |

---

# **Lección SQL 10: Consultas con agregados (Parte 1)**

Además de las expresiones simples que presentamos en la última lección, SQL también admite el uso de expresiones (o funciones) agregadas que le permiten resumir información sobre un grupo de filas de datos. Con la base de datos de Pixar que ha estado utilizando, se pueden utilizar funciones agregadas para responder preguntas como "¿Cuántas películas ha producido Pixar?" o "¿Cuál es la película de Pixar con mayor recaudación cada año?".

```
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

Sin una agrupación específica, cada función agregada se ejecutará en todo el conjunto de filas de resultados y devolverá un valor único. Y al igual que las expresiones normales, darle un alias a sus funciones agregadas garantiza que los resultados serán más fáciles de leer y procesar.

## **Funciones agregadas comunes**

A continuación se muestran algunas funciones agregadas comunes que usaremos en nuestros ejemplos:

| **Función**              | **Descripción**                                                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| COUNT(\*), COUNT(column) | Una función común que se utiliza para contar el número de filas del grupo si no se especifica ningún nombre de columna. De lo contrario, cuente el número de filas del grupo con valores no NULL en la columna especificada |
| MIN(column)              | Encuentra el valor numérico más pequeño en la columna especificada para todas las filas del grupo.                                                                                                                          |
| MAX(column)              | Encuentra el valor numérico más grande en la columna especificada para todas las filas del grupo.                                                                                                                           |
| AVG(column)              | Encuentra el valor numérico promedio en la columna especificada para todas las filas del grupo.                                                                                                                             |
| SUM(column)              | Encuentra la suma de todos los valores numéricos en la columna especificada para las filas del grupo.                                                                                                                       |

## **Funciones agregadas agrupadas**

Además de agregar en todas las filas, puede aplicar las funciones agregadas a grupos individuales de datos dentro de ese grupo (es decir, ventas de taquilla para películas de comedia o de acción).

Esto crearía tantos resultados como grupos únicos definidos en la **GROUP BY** Cláusula.

```
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression
GROUP BY column;
```

La **Group BY** Cláusula funciona agrupando filas que tienen el mismo valor en la columna especificada.

**Ejercicio**

Para este ejercicio. vamos a trabajar con nuestra tabla Empleados. Observe cómo las filas de esta tabla tiene datos compartidos, lo que nos dará la oportunidad de utilizar funciones agregadas para resumir algunas métricas de alto nivel sobre los equipos. Adelante, inténtalo.

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

**Ejercicio 10: Tareas**

- **Encuentre el tiempo más largo que un empleado ha estado en el estudio**

```
SELECT MAX(years_employed) as Max_years_employed
FROM employees;
```

- **Para cada puesto, encuentre el número promedio de años empleados por los empleados en ese puesto.**

```
SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;
```

- **Encuentre el número total de años de empleados trabajados en cada edificio.**

```
SELECT building, SUM(years_employed) as Total_years_employed
FROM employees
GROUP BY building;
```

| **Inicio**            | **atrás 10**                        | **Siguiente 12**                  |
| --------------------- | ----------------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./10_consultas_expresiones.md) | [⏩](./12_consultas_agregados.md) |

---
