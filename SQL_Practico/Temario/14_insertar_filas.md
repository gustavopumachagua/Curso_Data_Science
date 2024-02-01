| **Inicio**            | **atrás 13**                  | **Siguiente 15**                  |
| --------------------- | ----------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./13_orden_ejecucion.md) | [⏩](./15_actualizacion_filas.md) |

---

# **Lección SQL 13: Insertar filas**

Hemos dedicado bastantes lecciones sobre cómo consultar datos en una base de datos, por lo que es hora de comenzar a aprender un poco sobre esquemas SQL y cómo agregar nuevos datos.

## **¿Qué es un esquema?**

Anteriormente describimos una tabla en una base de datos como un conjunto bidimensional de filas y columnas, donde las columnas son las propiedades y las filas son instancias de la entidad en la tabla. En SQL, el esquema de la base de datos es lo que describe la estructura de cada tabla y los tipos de datos que puede contener cada columna de la tabla.

**Ejemplo: subconsulta correlacionada**

Por ejemplo, en nuestra tabla Películas , los valores de la columna Año deben ser un número entero y los valores de la columna Título deben ser una cadena.

Esta estructura fija es lo que permite que una base de datos sea eficiente y consistente a pesar de almacenar millones o incluso miles de millones de filas.

## **Insertando nuevos datos**

Al insertar datos en una base de datos, necesitamos usar una **INSERT** declaración que declare en qué tabla escribir, las columnas de datos que estamos completando y una o más filas de datos a insertar. En general, cada fila de datos que inserte debe contener valores para cada columna correspondiente de la tabla. Puede insertar varias filas a la vez simplemente enumerándolas secuencialmente.

```
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;

```

En algunos casos, si tiene datos incompletos y la tabla contiene columnas que admiten valores predeterminados, puede insertar filas solo con las columnas de datos que tiene especificándolas explícitamente.

```
INSERT INTO mytable
(column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;

```

En estos casos, la cantidad de valores debe coincidir con la cantidad de columnas especificadas. A pesar de que se trata de una declaración más detallada de escribir, insertar valores de esta manera tiene la ventaja de ser compatible con versiones posteriores. Por ejemplo, si agrega una nueva columna a la tabla con un valor predeterminado, no **INSERT** será necesario cambiar ninguna declaración codificada para adaptarse a ese cambio.

Además, puedes utilizar expresiones matemáticas y de cadena con los valores que vayas insertando.
Esto puede resultar útil para garantizar que todos los datos insertados tengan un formato determinado.

```
INSERT INTO boxoffice
(movie_id, rating, sales_in_millions)
VALUES (1, 9.9, 283742034 / 1000000);
```

**Ejercicio**

En este ejercicio, jugaremos como ejecutivos de estudio y agregaremos algunas películas a Películas de nuestro portafolio. En esta tabla, el **ID** es un número entero que se incrementa automáticamente, por lo que puede intentar insertar una fila solo con las otras columnas definidas.

Dado que las siguientes lecciones modificarán la base de datos, tendrás que ejecutar manualmente cada consulta una vez que estén listas.

**Table: Movies**

| **Id** | **Title**    | **Director**  | **Year** | **Length_minutes** |
| ------ | ------------ | ------------- | -------- | ------------------ |
| 1      | Toy Story    | John Lasseter | 1995     | 81                 |
| 2      | A Bug's Life | John Lasseter | 1998     | 95                 |
| 3      | Toy Story 2  | John Lasseter | 1999     | 93                 |

**Table: Boxoffice**

| **Movie_id** | **Rating** | **Domestic_sales** | **International_sales** |
| ------------ | ---------- | ------------------ | ----------------------- |
| 3            | 7.9        | 245852179          | 239163000               |
| 1            | 8.3        | 191796233          | 170162503               |
| 2            | 7.2        | 162798565          | 200600000               |

**Ejercicio 13: Tareas**

- **Agrega la nueva producción del estudio, Toy Story 4 a la lista de películas (puedes usar cualquier director)**

```
INSERT INTO movies VALUES (4, "Toy Story 4", "El Directore", 2015, 90);
```

- **¡Toy Story 4 ha sido lanzado con gran éxito de crítica! Tenía una calificación de 8,7 y ganó 340 millones a nivel nacional y 270 millones a nivel internacional . Agregue el registro a la BoxOfficetabla.**

```
INSERT INTO boxoffice VALUES (4, 8.7, 340000000, 270000000);
```

| **Inicio**            | **atrás 13**                  | **Siguiente 15**                  |
| --------------------- | ----------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./13_orden_ejecucion.md) | [⏩](./15_actualizacion_filas.md) |

---
