| **Inicio**            | **atrás 9**                 | **Siguiente 11**                 |
| --------------------- | --------------------------- | -------------------------------- |
| [🏠](../../README.md) | [⏪](./9_consultas_NULL.md) | [⏩](./11_consultas_agregado.md) |

---

# **Lección SQL 9: Consulta con Expresiones**

Además de consultar y hacer referencia a datos de columnas sin procesar con SQL, también puede usar expresiones para escribir una lógica más compleja en los valores de las columnas en una consulta. Estas expresiones pueden usar funciones matemáticas y de cadena junto con aritmética básica para transformar valores cuando se ejecuta la consulta, como se muestra en este ejemplo de física.

```
SELECT particle_speed / 2.0 AS half_particle_speed
FROM physics_data
WHERE ABS(particle_position) * 10.0 > 500;
```

Cada base de datos tiene su propio conjunto compatible de funciones matemáticas, de cadena y de fecha que se pueden usar en una consulta, que puede encontrar en sus respectivos documentos.

El uso de expresiones puede ahorrar tiempo y un posprocesamiento adicional de los datos del resultado, pero también puede hacer que la consulta sea más difícil de leer, por lo que recomendamos que cuando se utilizan expresiones en la parte de la consulta, también se les dé un alias **SELECT**
descriptivo. utilizando la palabra clave **AS**

```
SELECT col_expression AS expr_description, …
FROM mytable;
```

Además de las expresiones, las columnas normales e incluso las tablas también pueden tener alias para que sea más fácil hacer referencia a ellas en el resultadi y como parte de la simplificación de consultas más complejas.

```
SELECT column AS better_column_name, …
FROM a_long_widgets_table_name AS mywidgets
INNER JOIN widget_sales
  ON mywidgets.id = widget_sales.widget_id;
```

**Ejercicio**

Tendrás que usar expresiones para transformar los datos de BoxOffice en algo más fácil de entender para las siguientes tareas.

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
| 13           | 7.2        | 237283207          | 301700000               |

**Ejercicio 9: Tareas**

- **Enumere todas las películas y sus ventas combinadas en millones de dólares.**

```
SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```

- **Enumere todas las películas y sus calificaciones en porcentaje.**

```
SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
```

- **Enumere todas las películas que se estrenaron en años pares.**

```
SELECT title, year
FROM movies
WHERE year % 2 = 0;
```

| **Inicio**            | **atrás 9**                 | **Siguiente 11**                 |
| --------------------- | --------------------------- | -------------------------------- |
| [🏠](../../README.md) | [⏪](./9_consultas_NULL.md) | [⏩](./11_consultas_agregado.md) |

---
