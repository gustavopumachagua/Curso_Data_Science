| **Inicio**            | **atrás 4**                              | **Siguiente 6**               |
| --------------------- | ---------------------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./4_consultas_con_restricciones.md) | [⏩](./6_consultas_SELECT.md) |

---

# **Lección SQL 4: Filtrar y Ordenar resultados de consultas**

Aunque los datos de una base de datos pueden ser únicos, los resultados de una consulta en particular pueden no serlo; tomemos nuestra tabla de Películas, por ejemplo, se pueden estrenar muchas películas diferentes el mismo año. En tales casos, SQL proporciona una manera conveniente de descartar filas que tienen un valor de columna duplicado nediante la **DISTINCT** palabra clave.

```
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```

Dado que la **DISTINCT** palabra clave eliminará ciegamente filas duplicadas, en una lección futura aprenderemos cómo descartar duplicados en función de columnas específicas mediante la agrupación y la **GROUP BY** cláusula.

## **Resultados del pedido**

A diferencia de nuestra tabla cuidadosamente ordenada de las últimas lecciones, la mayoría de los datos en bases de datos reales se agregan sin ningún orden de columnas en particular. Como resultado, puede resultar difícil leer y comprender los resultados de una consulta a medida que el tamaño de una tabla aumenta a miles o incluso millones de filas.

Para ayudar con esto, SQL proporciona una manera de ordenar los resultados por una columna determinada en orden ascendente o descendente utilizando la **ORDER BY** cláusula.

```
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```

Cuando **ORDER BY** se especifica una cláusula, cada fila se ordena alfanuméricamente según el valor de la columna especificada. En algunas bases de datos, también puede especificar una intercalación para ordenar mejor los datos que contienen texto internacional.

## **Limitar los resultados a un subconjunto**

Otra cláusula que se usa comúnmente con la **ORDER BY** cláusula son las cláusulas **LIMIT** y **OFFSET**, que son una optimización útil para indicar a la base de datos el subconjunto de los resultados que le interesan.

Reducirá **LIMIT** el número de filas a devolver y el opcional **OFFSET** especificará desde dónde empezar a contar el número de filas.

```
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

Si piensa en sitios web como Reddit o Pinterest, la página principal es una lista de enlaces ordenados por popularidad y tiempo, y cada página posterior puede representarse mediante
conjuntos de enlaces en diferentes posiciones en la base de datos. Al utilizar estas cláusulas, la base de datos puede ejecutar consultas de manera más rápida y eficiente al procesar y devolver solo el contenido solicitado.

> ¿Sabías?
>
> Si tiene curiosidad sobre cuándo se aplican **LIMIT** y **OFFSET** en relación con las otras partes de una consulta, generalmente se hacen al final después de que se hayan aplicado las otras cláusulas. Tocaremos más sobre esto en la lección 12: Orden de ejecución después de presentar algunas partes más de la consulta.

**Ejercicio**

Hay algunos conceptos en esta lección, pero todos son bastante sencillos de aplicar. Para darle vida a las cosas, hemos codificado la tabla **Películas** en el ejercicio para imitar mejor el tipo de datos que podría ver en la vida real. Intente utilizar las palabras clave y cláusulas necesarias presentadas anteriormente en sus consultas.

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

**Ejercicio 4: Tareas**

- **Enumere todos los directores de las películas de Pixar (alfabéticamente), sin duplicados**

```
SELECT DISTINCT Director FROM Movies
ORDER BY director ASC;
```

- **Enumere las últimas cuatro películas de Pixar estrenadas (ordenadas de más reciente a menos)**

```
SELECT Title, Year FROM Movies
ORDER BY Year DESC
LIMIT 4;
```

- **Enumere las cinco primeras películas de Pixar ordenadas alfabéticamente**

```
SELECT Title FROM Movies
ORDER BY Title ASC
LIMIT 5;
```

- **Enumere las próximas cinco películas de Pixar ordenadas alfabéticamente**

```
SELECT Title FROM Movies
ORDER BY Title ASC
LIMIT 5 OFFSET 5;
```

| **Inicio**            | **atrás 4**                              | **Siguiente 6**               |
| --------------------- | ---------------------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./4_consultas_con_restricciones.md) | [⏩](./6_consultas_SELECT.md) |

---
