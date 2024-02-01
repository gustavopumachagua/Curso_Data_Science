| **Inicio**            | **atrás 3**                              | **Siguiente 5**              |
| --------------------- | ---------------------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./3_consultas_con_restricciones.md) | [⏩](./5_filtrar_ordenar.md) |

---

# **Lección SQL 3: Consultas con restricciones (Parte 2)**

Al escribir **WHERE** cláusulas con columnas que contienen datos de texto, SQL admiten una serie de operadores útiles para hacer cosas como la comparación de cadenas que no distingue entre mayúsculas y minúsculas y la coincidencia de patrones comodín. A continuación mostramos algunos operadores comunes específicos de datos de texto:

| **Operador** | **Condición**                                                                                                                 | **Ejemplo**                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| =            | Comparación de cadenas exactas que distinguen entre mayúsculas y minúsculas ( observe que el único es igual )                 | col_name = "abc"                                                   |
| != or <>     | Comparación de desigualdad de cadenas exactas que distingue entre mayúsculas y minúsculas                                     | col_name != "abcd"                                                 |
| LIKE         | Comparación de cadenas exactas que no distinguen entre mayúsculas y minúsculas                                                | col_name LIKE "ABCD"                                               |
| NOT LIKE     | Comparación de desigualdad de cadenas exactas que no distingue entre mayúsculas y minúsculas                                  | col_name NOT LIKE "ABCD"                                           |
| %            | Se usa en cualquier parte de una cadena para hacer coincidir una secuencia de cero o más caracteres (solo con LIKE o NO LIKE) | col_name LIKE "%AT%" (matches "AT", "ATTIC", "CAT" or even "BATS") |
| \_           | Se usa en cualquier parte de una cadena para que coincida con un solo carácter (solo con LIKE o NO LIKE)                      | col*name LIKE "AN*" (matches "AND", but not "AN")                  |
| IN (…)       | La cadena existe en una lista.                                                                                                | col_name IN ("A", "B", "C")                                        |
| NOT IN (…)   | La cadena no existe en una lista                                                                                              | col_name NOT IN ("D", "E", "F")                                    |

> **¿Sabías?**
>
> Todas las cadenas deben estar entre comillas para que el analizador de consultas pueda distinguir las palabras de la cadena de las palabras clave SQL.

Debemos tener en cuenta que, si bien la mayoría de las implementaciones de bases de datos son bastante eficientes cuando se utilizan estos operadores, es mejor dejar la búsqueda de texto completo en bibliotecas dedicadas como Apache Lucene o Sphinx. Estas bibliotecas están diseñadas específicamente para realizar búsquedas de texto completo y, como resultado, son más eficientes y pueden admitir una variedad más amplia de funciones de búsqueda, incluida la internacionalización y consultas avanzadas.

**Ejercicio**

Aquí está nuevamente la definición de una consulta con una **WHERE** cláusula, continúe e intente escribir algunas consultas con los operadores anteriores para limitar los resultados a la información que necesitamos en las tareas siguientes.

```
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```

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

**Ejercicio 3: Tareas**

- **Encuentra todas las películas de Toy Story**

```SELECT Title, Director FROM Movies
WHERE Title LIKE "Toy Story%";
```

- **Encuentra todas las películas dirigidas por John Lasseter**

```
SELECT Title, Director FROM Movies
WHERE Director = "John Lasseter";
```

- **Encuentra todas las películas (y directores) no dirigidas por John Lasseter**

```
SELECT Title, Director FROM Movies
WHERE Director != "John Lasseter";
```

- **Encuentra todas las películas de WALL-**

```
SELECT * FROM Movies
WHERE Title LIKE "WALL-_";
```

| **Inicio**            | **atrás 3**                              | **Siguiente 5**              |
| --------------------- | ---------------------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./3_consultas_con_restricciones.md) | [⏩](./5_filtrar_ordenar.md) |

---
