| **Inicio**            | **atrás 14**                 | **Siguiente 16**             |
| --------------------- | ---------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./14_insertar_filas.md) | [⏩](./16_eliminar_filas.md) |

---

# **Lección SQL 14: Actualización de filas**

Además de agregar nuevos datos, una tarea común es actualizar los datos existentes, lo que se puede hacer mediante una **UPDATE** declaración. De manera similar a la **INSERT** declaración, debe especificar exactamente qué tabla, columnas y filas actualizar. Además, los datos que está actualizando deben coincidir con el tipo de datos de las columnas del esquema de la tabla.

```
UPDATE mytable
SET column = value_or_expr,
    other_column = another_value_or_expr,
    …
WHERE condition;
```

La declaración funciona tomando múltiples pares de columna/valor y aplicando esos cambios a todas y cada una de las filas que satisfacen la restricción de la **WHERE** cláusula.

## **Teniendo cuidado**

La mayoría de las personas que trabajan con SQL cometerán errores al actualizar los datos en un momento u otro. Ya sea que se trate de actualizar el conjunto incorrecto de filas en una base de datos de producción o de omitir accidentalmente la **WHERE** cláusula (lo que hace que la actualización se aplique a todas las filas), debe tener mucho cuidado al construir **UPDATE** declaraciones.

Un consejo útil es escribir siempre la restricción primero y probarla en una **SELECT** consulta para asegurarse de que está actualizando las filas correctas, y solo luego escribir los pares de columna/valor para actualizar.

**Ejercicio**

Parece que parte de la información de nuestra base de datos de películas puede ser incorrecta, así que continúa y corrígela mediante los ejercicios siguientes.

**Table: Movies**

| **Id** | **Title**           | **Director**   | **Year** | **Length_minutes** |
| ------ | ------------------- | -------------- | -------- | ------------------ |
| 1      | Toy Story           | John Lasseter  | 1995     | 81                 |
| 2      | A Bug's Life        | El Directore   | 1998 95  |
| 3      | Toy Story 2         | John Lasseter  | 1899     | 93                 |
| 4      | Monsters, Inc.      | Pete Docter    | 2001     | 92                 |
| 5      | Finding Nemo        | Andrew Stanton | 2003     | 107                |
| 6      | The Incredibles     | Brad Bird      | 2004     | 116                |
| 7      | Cars                | John Lasseter  | 2006     | 117                |
| 8      | Ratatouille         | Brad Bird      | 2007     | 115                |
| 9      | WALL-E              | Andrew Stanton | 2008     | 104                |
| 10     | Up                  | Pete Docter    | 2009     | 101                |
| 11     | Toy Story 8         | El Directore   | 2010     | 103                |
| 12     | Cars 2              | John Lasseter  | 2011     | 120                |
| 13     | Brave               | Brenda Chapman | 2012     | 102                |
| 14     | Monsters University | Dan Scanlon    | 2013     | 110                |

**Ejercicio 14: Tareas**

- **El director de Bichos está equivocado, en realidad fue dirigida por John Lasseter**

```
UPDATE movies
SET director = "John Lasseter"
WHERE id = 2;
```

- **El año en que se lanzó Toy Story 2 es incorrecto, en realidad se lanzó en 1999.**

```
UPDATE movies
SET year = 1999
WHERE id = 3;
```

- **¡Tanto el título como el director de Toy Story 8 son incorrectos! El título debería ser "Toy Story 3" y fue dirigida por Lee Unkrich**

```
UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
WHERE id = 11;
```

| **Inicio**            | **atrás 14**                 | **Siguiente 16**             |
| --------------------- | ---------------------------- | ---------------------------- |
| [🏠](../../README.md) | [⏪](./14_insertar_filas.md) | [⏩](./16_eliminar_filas.md) |

---
