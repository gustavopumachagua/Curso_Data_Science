| **Inicio**            | **atrás 12**                      | **Siguiente 14**             |
| --------------------- | --------------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./12_consultas_agregados.md) | [⏩](./14_insertar_filas.md) |

---

# **Lección SQL 12: Orden de ejecución de una consulta**

Ahora que tenemos una idea de todas las partes de una consulta, podemos hablar de cómo encajan todas en el contexto de una consulta completa.

```
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
    JOIN another_table
      ON mytable.column = another_table.column
    WHERE constraint_expression
    GROUP BY column
    HAVING constraint_expression
    ORDER BY column ASC/DESC
    LIMIT count OFFSET COUNT;
```

Cada consulta comienza encontrando los datos que necesitamos en una base de datos y luego filtrándolos hasta convertirlos en algo que pueda procesarse y comprenderse lo más rápido posible. Debido a que cada parte de la consulta se ejecuta secuencialmente, es importante comprender el orden de ejecución para saber a qué resultados se puede acceder y dónde.

## **Orden de ejecución de la consulta**

**1. FROM y JOINs**

La **FROM** cláusula y las subsiguientes **JOIN** se ejecutan primero para determinar el conjunto de datos de trabajo total que se está consultando. Esto incluye subconsultas en esta cláusula y puede provocar que se creen tablas temporales internas que contengan todas las columnas y filas de las tablas que se unen.

**2.WHERE**

Una vez que tenemos el conjunto total de datos de trabajo, las **WHERE** restricciones de primer paso se aplican a las filas individuales y las filas que no satisfacen la restricción se descartan. Cada una de las restricciones solo puede acceder a columnas directamente desde las tablas solicitadas en la **FROM** cláusula. Los alias en la **SELECT** parte de la consulta no son accesibles en la mayoría de las bases de datos, ya que pueden incluir expresiones que dependen de partes de la consulta que aún no se han ejecutado.

**3.GROUP BY**

Las filas restantes después **WHERE** de aplicar las restricciones se agrupan según valores comunes en la columna especificada en la **GROUP BY** cláusula. Como resultado de la agrupación, solo habrá tantas filas como valores únicos en esa columna. Implícitamente, esto significa que solo debería necesitar usar esto cuando tenga funciones agregadas en su consulta.

**4.HAVING**

Si la consulta tiene una **GROUP BY** cláusula, las restricciones de la **HAVING** cláusula se aplican a las filas agrupadas y se descartan las filas agrupadas que no satisfacen la restricción. Al igual que la **WHERE** cláusula, tampoco se puede acceder a los alias desde este paso en la mayoría de las bases de datos.

**5.SELECT**

**SELECT** Finalmente se calculan todas las expresiones de la parte de la consulta.

**6.DISTINCT**

**DISTINCT** De las filas restantes, se descartarán las filas con valores duplicados en la columna marcada como .

**7.ORDER BY**

Si la cláusula especifica un orden **ORDER BY**, las filas se ordenan según los datos especificados en orden ascendente o descendente. Dado que se han calculado todas las expresiones de la **SELECT** parte de la consulta, puede hacer referencia a los alias en esta cláusula.

**8. LIMIT/OFFSET**

Finalmente, las filas que quedan fuera del rango especificado por **LIMIT** y **OFFSET** se descartan, dejando el conjunto final de filas que se devolverá de la consulta.

**Conclusión**

No todas las consultas necesitan tener todas las partes que enumeramos anteriormente, pero una de las razones por las que SQL es tan flexible es que permite a los desarrolladores y analistas de datos manipular datos rápidamente sin tener que escribir código adicional, todo simplemente usando las cláusulas anteriores.

**Ejercicio**

Aquí terminan nuestras lecciones sobre **SELECT** consultas, ¡felicidades por llegar hasta aquí! Este ejercicio intentará poner a prueba su comprensión de las consultas, así que no se desanime si las encuentra desafiantes. Trata de dar lo mejor.

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

**Ejercicio 12: Tareas**

- **Calcula el número de películas que ha dirigido cada director.**

```
SELECT director, COUNT(id) as Num_movies_directed
FROM movies
GROUP BY director;
```

- **Encuentre el total de ventas nacionales e internacionales que se pueden atribuir a cada director.**

```
SELECT director, SUM(domestic_sales + international_sales) as Cumulative_sales_from_all_movies
FROM movies
    INNER JOIN boxoffice
        ON movies.id = boxoffice.movie_id
GROUP BY director;
```

| **Inicio**            | **atrás 12**                      | **Siguiente 14**             |
| --------------------- | --------------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./12_consultas_agregados.md) | [⏩](./14_insertar_filas.md) |

---
