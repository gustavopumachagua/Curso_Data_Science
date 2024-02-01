| **Inicio**            | **atrás 6**                   | **Siguiente 8**               |
| --------------------- | ----------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./6_consultas_SELECT.md) | [⏩](./8_consultas_JOIN'S.md) |

---

# **Lección de SQL 6: Consultas de varias tablas con JOIN**

Hasta ahora, hemos estado trabajando con una sola tabla, pero los datos de entidades en el mundo real a menudo se dividen en partes y se almacenan en múltiples tablas ortogonales mediante un proceso conocido como normalización.

## **Normalización de base de datos**

La normalización de la base de datos es útil porque minimiza los datos duplicados en cualquier tabla y permite que los datos de la base de datos crezcan independientemente unos de otros (es decir, los tipos de motores de automóviles oueden crecer independientemente de cada tipo de automóvil).

Como compensación, las consultas se vuelven un poco más complejas ya que deben poder encontrar datos de diferentes partes de la base de datos y pueden surgir problemas de rendimiento cuando se trabaja con muchas tablas grandes.

Para responder preguntas sobre una entidad que tiene datos que abarcan varias tablas en una base de datos normalizada, necesitamos aprender a escribir una consulta que pueda combinar todos esos datos y extraer exactamente la información que necesitamos.

## **Consultas de varias tablas con JOIN**

Las tablas que comparten información sobre única entidad deben tener una clave principal que identifique esa entidad de forma única en toda la base de datos. Un tipo de clave principal común es un número entero que se incrementa automaticamente (porque ahorra espacio), pero también puede ser una cadena, un valor hash, siempre que sea único.

Al usar la **JOIN** clásusula en una consulta, podemos combinar datos de filas en dos tablas separadas usando esta clave única. La primera de las combinaciones que presentaremos es **INNER JOIN**.

```
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

Es **INNER JOIN** un proceso que hace coincidir filas de la primera tabla y la segunda tabla que tienen la misma clave (Según lo definido por la **ON** restricción) para crear una fila de resultado con las columnas combinadas de ambas tablas. Una vez unidas las tablas se aplican las demás cláusulas que aprendimos anteriormente.

![sql joins](../img/sqljoin.jpeg "sql joins")

> ¿Sabías?
>
> Es posible que vea consultas en las que **INNER JOIN** esté escrito simplemente como **JOIN**. Estos dos son equivalentes, pero continuaremos refiriéndonos a estas uniones como uniones internas porque hacen que la consulta sea más fácil de leer una vez que comience a usar otros tipos de uniones que se presentarán en la siguiente lección.

**Ejercicio**

Hemos agregado una nueva tabla a la base de datos de Pixar que puedas intentar practicar algunas uniones. La tabla **BoxOffice** almacena información sobre las calificaciones y las ventas de cada película de Pixar en particular, y la columna **Movie_id** en esa tabla se corresponde con la columna **id** en la tabla películas 1 a 1. Intente resolver las siguientes tareas utilizando lo **INNER JOIN** presentado anteriormente.

**Table: Movies**

| **Id** | **Title**      | **Director**  | **Year** | **Length_minutes** |
| ------ | -------------- | ------------- | -------- | ------------------ |
| 1      | Toy Story      | John Lasseter | 1995     | 81                 |
| 2      | A Bug's Life   | John Lasseter | 1998     | 95                 |
| 3      | Toy Story 2    | John Lasseter | 1999     | 93                 |
| 4      | Monsters, Inc. | Pete Docter   | 2001     | 92                 |

**Table: Boxoffice**

| **Movie_id** | **Rating** | **Domestic_sales** | **International_sales** |
| ------------ | ---------- | ------------------ | ----------------------- |
| 5            | 8.2        | 380843261          | 555900000               |
| 14           | 7.4        | 268492764          | 475066843               |
| 8            | 8          | 206445654          | 417277164               |
| 12           | 6.4        | 191452396          | 368400000               |
| 3            | 7.9        | 245852179          | 239163000               |
| 6            | 8          | 261441092          | 370001000               |
| 9            | 8.5        | 223808164          | 297503696               |
| 11           | 8.4        | 415004880          | 648167031               |
| 1            | 8.3        | 191796233          | 170162503               |
| 7            | 7.2        | 244082982          | 217900167               |
| 10           | 8.3        | 293004164          | 438338580               |
| 4            | 8.1        | 289916256          | 272900000               |
| 2            | 7.2        | 162798565          | 200600000               |
| 13           | 7.2        | 237283207          | 3017                    |

**Ejercicio 6: Tareas**

- **Encuentra las ventas nacionales e internacionales de cada película.**

```
SELECT title, domestic_sales, international_sales
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```

- **Muestre las cifras de ventas de cada película que obtuvo mejores resultados a nivel internacional que a nivel nacional.**

```
SELECT title, domestic_sales, international_sales
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;
```

- **Enumere todas las películas por clasificación en orden descendente.**

```
SELECT title, rating
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;
```

| **Inicio**            | **atrás 6**                   | **Siguiente 8**               |
| --------------------- | ----------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./6_consultas_SELECT.md) | [⏩](./8_consultas_JOIN'S.md) |

---
