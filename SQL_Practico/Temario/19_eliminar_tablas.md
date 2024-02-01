| **Inicio**            | **atrás 18**                   | **Siguiente 20**           |
| --------------------- | ------------------------------ | -------------------------- |
| [🏠](../../README.md) | [⏪](./18_modificar_tablas.md) | [⏩](./20_subconsultas.md) |

---

# **Lección SQL 18: Eliminación de tablas**

En algunos casos excepcionales, es posible que desee eliminar una tabla completa, incluidos todos sus datos y metadatos, y para hacerlo, puede usar la **DROP TABLE** declaración, que difiere de la **DELETE** declaración en que también elimina por completo el esquema de la tabla de la base de datos.

```
DROP TABLE IF EXISTS mytable;
```

Al igual que la **CREATE TABLE** declaración, la base de datos puede generar un error si la tabla especificada no existe y, para suprimir ese error, puede utilizar la **IF EXISTS** cláusula.

Además, si tiene otra tabla que depende de las columnas de la tabla que está eliminando (por ejemplo, con una **FOREIGN KEY** dependencia), primero tendrá que actualizar todas las tablas dependientes para eliminar las filas dependientes o eliminar esas tablas por completo.

**Ejercicio**

Hemos llegado al final de nuestros ejercicios, así que vamos a limpiar eliminando todas las tablas con las que hemos trabajado.

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

**Ejercicio 18: Tareas**

- **Lamentablemente, hemos llegado al final de nuestras lecciones. Limpiemos eliminando la tabla de Películas.**

```
DROP TABLE Movies;
```

- **Y suelte la mesa de BoxOffice también.**

```
DROP TABLE BoxOffice;
```

| **Inicio**            | **atrás 18**                   | **Siguiente 20**           |
| --------------------- | ------------------------------ | -------------------------- |
| [🏠](../../README.md) | [⏪](./18_modificar_tablas.md) | [⏩](./20_subconsultas.md) |

---
