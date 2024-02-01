| **Inicio**            | **atrás 15**                      | **Siguiente 17**           |
| --------------------- | --------------------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./15_actualizacion_filas.md) | [⏩](./17_crear_tablas.md) |

---

# **Lección SQL 15: Eliminar filas**

Cuando necesite eliminar datos de una tabla en la base de datos, puede utilizar una **DELETE** declaración que describa la tabla sobre la que actuar y las filas de la tabla que eliminará a través de la **WHERE** cláusula.

```
DELETE FROM mytable
WHERE condition;
```

Si decide omitir la **WHERE** restricción, se eliminan todas las filas, lo cual es una manera rápida y fácil de borrar una tabla por completo (si es intencional).

## **Teniendo mucho cuidado**

Al igual que la **UPDATE** declaración de la lección anterior, se recomienda ejecutar **SELECT** primero la restricción en una consulta para asegurarse de eliminar las filas correctas. Sin una copia de seguridad o una base de datos de prueba adecuada, es muy fácil eliminar datos irrevocablemente, así que siempre lea sus **DELETE** declaraciones dos veces y ejecútelas una vez.

**Ejercicio**

Es necesario limpiar un poco la base de datos, así que intente eliminar algunas filas en las tareas siguientes.

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

**Ejercicio 15: Tareas**

- **Esta base de datos se está volviendo demasiado grande, eliminemos todas las películas que se estrenaron antes de 2005.**

```
DELETE FROM movies
where year < 2005;
```

- **Andrew Stanton también dejó el estudio, así que elimine todas las películas dirigidas por él.**

```
DELETE FROM movies
where director = "Andrew Stanton";
```

| **Inicio**            | **atrás 15**                      | **Siguiente 17**           |
| --------------------- | --------------------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./15_actualizacion_filas.md) | [⏩](./17_crear_tablas.md) |

---
