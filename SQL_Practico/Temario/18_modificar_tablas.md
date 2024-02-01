| **Inicio**            | **atrás 17**               | **Siguiente 19**              |
| --------------------- | -------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./17_crear_tablas.md) | [⏩](./19_eliminar_tablas.md) |

---

# **Lección SQL 17: Modificación de tablas**

A medida que sus datos cambian con el tiempo, SQL le proporciona una manera de actualizar sus tablas y esquemas de bases de datos correspondientes utilizando la **ALTER TABLE** declaración para agregar, eliminar o modificar columnas y restricciones de tablas.

## **Agregar columnas**

La sintaxis para agregar una nueva columna es similar a la sintaxis al crear nuevas filas en la **CREATE TABLE** declaración. Debe especificar el tipo de datos de la columna junto con las posibles restricciones de la tabla y los valores predeterminados que se aplicarán tanto a las filas existentes como a las nuevas. En algunas bases de datos como MySQL, incluso puedes especificar dónde insertar la nueva columna usando las cláusulas **FIRST** o **AFTER**, aunque esta no es una característica estándar.

```
ALTER TABLE mytable
ADD column DataType OptionalTableConstraint
    DEFAULT default_value;
```

## **Eliminando columnas**

Eliminar columnas es tan fácil como especificar la columna que se eliminará; sin embargo, algunas bases de datos (incluida SQLite) no admiten esta función. En su lugar, es posible que tengas que crear una nueva tabla y migrar los datos.

```
ALTER TABLE mytable
DROP column_to_be_deleted;
```

## **Cambiar el nombre de la tabla**

Si necesita cambiar el nombre de la tabla, también puede hacerlo utilizando la **RENAME TO** cláusula de la declaración.

```
ALTER TABLE mytable
RENAME TO new_table_name;
```

## **Otros cambios**

Cada implementación de base de datos admite diferentes métodos para alterar sus tablas, por lo que siempre es mejor consultar los documentos de su base de datos antes de continuar: MySQL , Postgres , SQLite , Microsoft SQL Server .

**Ejercicio**

Nuestros ejercicios utilizan una implementación que solo admite la adición de nuevas columnas, así que pruébelo a continuación.

**Table: Movies**

| **Id** | **Title**           | **Director**       | **Year** | **Length_minutes** |
| ------ | ------------------- | ------------------ | -------- | ------------------ |
| 1      | Toy Story           | John Lasseter      | 1995     | 81                 |
| 2      | A Bug's Life        | John Lasseter      | 1998     | 95                 |
| 3      | Toy Story 2         | John Lasseter      | 1999     | 93                 |
| 4      | Monsters, Inc.      | Pete Docter        | 2001     | 92                 |
| 5      | Finding Nemo        | Andrew Stanton     | 2003     | 107                |
| 6      | The Incredibles     | Brad Bird          | 2004     | 116                |
| 7      | Cars                | John Lasseter      | 2006     | 117                |
| 8      | Ratatouille         | Brad Bird          | 2007     | 115                |
| 9      | WALL-E              | Andrew Stanton     | 2008     | 104                |
| 10     | Up                  | Pete Docter        | 2009     | 101                |
| 11     | Toy Story 3         | Lee Unkrich        | 2010     | 103                |
| 12     | Cars 2              | John Lasseter 2011 | 120      |
| 13     | Brave               | Brenda Chapman     | 2012     | 102                |
| 14     | Monsters University | Dan Scanlon        | 2013     | 110                |

**Ejercicio 17: Tareas**

- **Agregue una columna llamada Aspect_ratio con un tipo de datos FLOAT para almacenar la relación de aspecto en la que se lanzó cada película.**

```
ALTER TABLE Movies
  ADD COLUMN Aspect_ratio FLOAT DEFAULT 2.39;
```

- **Agregue otra columna denominada Idioma con un tipo de datos TEXTO para almacenar el idioma en el que se estrenó la película. Asegúrese de que el idioma predeterminado para este idioma sea el inglés.**

```
ALTER TABLE Movies
  ADD COLUMN Language TEXT DEFAULT "English";
```

| **Inicio**            | **atrás 17**               | **Siguiente 19**              |
| --------------------- | -------------------------- | ----------------------------- |
| [🏠](../../README.md) | [⏪](./17_crear_tablas.md) | [⏩](./19_eliminar_tablas.md) |

---
