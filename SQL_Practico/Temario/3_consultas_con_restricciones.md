| **Inicio**            | **atrás 2**                   | **Siguiente 4**                          |
| --------------------- | ----------------------------- | ---------------------------------------- |
| [🏠](../../README.md) | [⏪](./2_consultas_SELECT.md) | [⏩](./4_consultas_con_restricciones.md) |

---

# **Lección SQL 2: Consultas con restricciones (Parte 1)**

Ahora sabemos cómo seleccionar columnas de datos específicas de una tabla, pero si tuviera una tabla con cien millones de filas de datos, leer todas las filas sería ineficiente y quizás incluso imposible.

Para evitar que se devuelvan ciertos resultados, necesitamos usar una **WHERE** cláusula en la consulta. La cláusula se aplica a cada fila de datos verificando valores de columna específicos para determinar si deben incluirse en los resultados o no.

```
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```

Se pueden construir cláusulas más complejas uniendo numerosas palabras clave **AND** lógicas **OR** (es decir, num_wheels >= 4 AND puertas <=2). Y a continuación se muestran algunos operadores útiles que puede utilizar para datos numéricos (es decir, enteros o de punto flotante):

| **Operador**        | **Condición**                                                 | **Ejemplo de SQL**                        |
| ------------------- | ------------------------------------------------------------- | ----------------------------------------- |
| =, !=, < <=, >, >=  | Operadores numéricos estándar                                 | col_name != 4                             |
| BETWEEN … AND …     | El número está dentro del rango de dos valores (inclusive)    | (inclusive) col_name BETWEEN 1.5 AND 10.5 |
| NOT BETWEEN … AND … | El número no está dentro del rango de dos valores (inclusive) | col_name NOT BETWEEN 1 AND 10             |
| IN (…)              | El número existe en una lista.                                | col_name IN (2, 4, 6)                     |
| NOT IN (…)          | El número no existe en una lista                              | col_name NOT IN (1, 3, 5)                 |

Además de hacer que los resultados sean más fáciles de entender, escribir cláusulas para restringir el conjunto de filas devueltas también permite que la consulta se ejecute más rápido debido a la reducción de datos innecesarios que se devuelven.

> **¿Sabias?**
>
> Como ya habrás notado, SQL no requiere que escribas las palabras clave en mayúsculas, pero como convención, ayuda a las personas a distinguir las palabras clave SQL de los nombres de columnas y tablas, y hace que la consulta sea más fácil de leer.

**Ejercicio**

Usando las restricciones correctas, encuentre la información que necesitamos en la tabla **Movies** para cada tarea a continuación.

**Table: Movies**

| **Id** | **Title**           | **Director**   | **Year** | **Length_minutes** |
| ------ | ------------------- | -------------- | -------- | ------------------ |
| 1      | Toy Story           | John Lasseter  | 1995     | 81                 |
| 2      | A Bug's Life        | John Lasseter  | 1998     | 95                 |
| 3      | Toy Story 2         | John Lasseter  | 1999     | 93                 |
| 4      | Monsters, Inc.      | Pete Docter    | 2001     | 92                 |
| 5      | Finding Nemo        | Andrew Stanton | 2003     | 107                |
| 6      | The Incredibles     | Brad Bird      | 2004     | 116                |
| 7      | Cars                | John Lasseter  | 2006     | 117                |
| 8      | Ratatouille         | Brad Bird      | 2007     | 115                |
| 9      | WALL-E              | Andrew Stanton | 2008     | 104                |
| 10     | Up                  | Pete Docter    | 2009     | 101                |
| 11     | Toy Story 3         | Lee Unkrich    | 2010     | 103                |
| 12     | Cars 2              | John Lasseter  | 2011     | 120                |
| 13     | Brave               | Brenda Chapman | 2012     | 102                |
| 14     | Monsters University | Dan Scanlon    | 2013     | 110                |

---

**Ejercicio 2: Tareas**

- **Encuentra la película con una fila id de 6.**

```
SELECT Id, Title FROM Movies
WHERE Id = 6;
```

- **Encuentra las películas estrenadas en la year década de 2000 y 2010.**

```
SELECT Title, Year FROM Movies
WHERE Year BETWEEN 2000 AND 2010;
```

- **Encuentra las películas no estrenadas en la year década de 2000 y 2010.**

```
SELECT Title, Year FROM Movies
WHERE Year < 2000 OR Year > 2010;
```

- **Encuentra las primeras 5 películas de Pixar y su estreno year**

```
SELECT Title, Year FROM Movies
WHERE Year <= 2003;
```

| **Inicio**            | **atrás 2**                   | **Siguiente 4**                          |
| --------------------- | ----------------------------- | ---------------------------------------- |
| [🏠](../../README.md) | [⏪](./2_consultas_SELECT.md) | [⏩](./4_consultas_con_restricciones.md) |

---
