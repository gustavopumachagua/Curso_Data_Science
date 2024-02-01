| **Inicio**            | **atrás 1**                   | **Siguiente 3**                          |
| --------------------- | ----------------------------- | ---------------------------------------- |
| [🏠](../../README.md) | [⏪](./1_introduccion_sql.md) | [⏩](./3_consultas_con_restricciones.md) |

---

# **Lección SQL 1: Consultas SELECT**

Para recuperar datos de una base de datos SQL, necesitamos escribir **SELECT** declaraciones, a las que a menudo se hace referencia coloquialmente como consultas. Una consulta en sí misma es solo una declaración que declara qué datos estamos buscando, dónde encontrarlos en la base de datos y, opcionalmente, cómo transformarlos antes de que se devuelvan. Sin embargo, tiene una sintaxis específica, que es la que aprenderemos en los siguientes ejercicios.

Como mencionamos en la introducción, puede pensar en una tabla en SQL como un tipo de entidad (es decir, perros), y cada fila de esa tabla como una instancia específica de ese tipo (es decir, un pug, un beagle, un pug de diferentes colores, etc.). Esto significa que las columnas representarían las propiedades comunes compartidas por todas las instancias de esa entidad (es decir, color del pelaje, longitud de la cola, etc.).

y dada una tabla de datos, la consulta más básica que podríamos escribir sería una que seleccione un par de columnas (propiedades) de la tabla con todas las filas (instancias).

```
SELECT column, another_column, ........
FROM mytable;
```

El resultado de esta consulta será un conjunto bidimensional de filas y columnas, efectivamente una copia de la tabla, pero solo las columnas que solicitamos.

Si queremos recuperar absolutamente todas las columnas de datos de una tabla. podemos usar la \* taquigrafía asterisco () en lugar de enumerar todos los nombres de las columnas individualmente.

```
SELECT *
FROM mytable;
```

Esta consulta, en particular, es realmente útil porque es una forma sencilla de inspeccionar una tabla volcando todos a la vez.

**Ejercicio**

Usaremos una base de datos con datos sobre algunas de las películas clásicas de Pixar para la mayoría de nuestros ejercicios. Este primer ejercicio solo involucrará la tabla **Movies** y las consulta predeterminada a continuación muestra actualmente todas las propiedades de cada película. Para continuar con la siguiente lección, modifique la consulta para encontrar la informacion exacta que necesitamos para cada tarea.

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

**Ejercicio 1: Tareas**

- **Encuentra el title de cada película.**

```
SELECT Title FROM Movies;
```

- **Encuentra el director de cada película.**

```
SELECT Director FROM Movies;
```

- **Encuentra el title y director de cada película.**

```
SELECT Title, Director FROM Movies;
```

- **Encuentra el title y year de cada película.**

```
SELECT Title, Year FROM Movies;
```

- **Encuentra all la información de cada película.**

```
SELECT * FROM Movies;
```

| **Inicio**            | **atrás 1**                   | **Siguiente 3**                          |
| --------------------- | ----------------------------- | ---------------------------------------- |
| [🏠](../../README.md) | [⏪](./1_introduccion_sql.md) | [⏩](./3_consultas_con_restricciones.md) |

---
