| **Inicio**            | **atrás 16**                 | **Siguiente 18**               |
| --------------------- | ---------------------------- | ------------------------------ |
| [🏠](../../README.md) | [⏪](./16_eliminar_filas.md) | [⏩](./18_modificar_tablas.md) |

---

# **Lección SQL 16: Crear tablas**

Cuando tenga nuevas entidades y relaciones para almacenar en su base de datos, puede crear una nueva tabla de base de datos usando la **CREATE TABLE** declaración.

```
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
```

La estructura de la nueva tabla está definida por su esquema de tabla , que define una serie de columnas. Cada columna tiene un nombre, el tipo de datos permitidos en esa columna, una restricción de tabla opcional sobre los valores que se insertan y un valor predeterminado opcional.

Si ya existe una tabla con el mismo nombre, la implementación de SQL generalmente arrojará un error, por lo que para suprimir el error y omitir la creación de una tabla, si existe, puede usar la **IF NOT EXISTS** cláusula.

## **Tipos de datos de tabla**

Diferentes bases de datos admiten diferentes tipos de datos, pero los tipos comunes admiten números, cadenas y otras cosas diversas como fechas, valores booleanos o incluso datos binarios. A continuación se muestran algunos ejemplos que podría utilizar en código real.

| **Tipo de datos**                              | **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| INTEGER, BOOLEAN                               | Los tipos de datos enteros pueden almacenar valores enteros completos como el recuento de un número o una edad. En algunas implementaciones, el valor booleano simplemente se representa como un valor entero de solo 0 o 1.                                                                                                                                                                                                                                                                                 |
| FLOAT, DOUBLE, REAL                            | Los tipos de datos de punto flotante pueden almacenar datos numéricos más precisos, como mediciones o valores fraccionarios. Se pueden utilizar diferentes tipos dependiendo de la precisión de coma flotante requerida para ese valor.                                                                                                                                                                                                                                                                      |
| CHARACTER(num_chars), VARCHAR(num_chars), TEXT | Los tipos de datos basados ​​en texto pueden almacenar cadenas y texto en todo tipo de configuraciones regionales. La distinción entre los distintos tipos suele contribuir a la eficiencia de la base de datos al trabajar con estas columnas. Tanto el tipo CHARACTER como el VARCHAR (carácter variable) se especifican con la cantidad máxima de caracteres que pueden almacenar (los valores más largos pueden truncarse), por lo que puede ser más eficiente almacenar y consultar con tablas grandes. |
| DATE, DATETIME                                 | SQL también puede almacenar marcas de fecha y hora para realizar un seguimiento de series temporales y datos de eventos. Puede resultar complicado trabajar con ellos, especialmente cuando se manipulan datos en zonas horarias.                                                                                                                                                                                                                                                                            |
| BLOB                                           | Finalmente, SQL puede almacenar datos binarios en blobs directamente en la base de datos. Estos valores suelen ser opacos para la base de datos, por lo que normalmente hay que almacenarlos con los metadatos correctos para volver a consultarlos.                                                                                                                                                                                                                                                         |

## **restricciones de tabla**

No vamos a profundizar demasiado en las restricciones de la tabla en esta lección, pero cada columna puede tener restricciones de tabla adicionales que limitan los valores que se pueden insertar en esa columna. Esta no es una lista completa, pero mostrará algunas restricciones comunes que pueden resultarle útiles.

| **Restricción**    | **Descripción**                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PRIMARY KEY        | Esto significa que los valores de esta columna son únicos y cada valor se puede utilizar para identificar una sola fila en esta tabla.                                                                                                                                                                                                                                                                                 |
| AUTOINCREMENT      | Para valores enteros, esto significa que el valor se completa e incrementa automáticamente con cada inserción de fila. No es compatible con todas las bases de datos.                                                                                                                                                                                                                                                  |
| UNIQUE             | Esto significa que los valores de esta columna deben ser únicos, por lo que no puede insertar otra fila con el mismo valor en esta columna que otra fila de la tabla. Se diferencia de la `CLAVE PRIMARIA` en que no tiene que ser una clave para una fila de la tabla.                                                                                                                                                |
| NOT NULL           | Esto significa que el valor insertado no puede ser "NULL".                                                                                                                                                                                                                                                                                                                                                             |
| CHECK (expression) | Esto le permite ejecutar una expresión más compleja para probar si los valores insertados son válidos. Por ejemplo, puedes comprobar que los valores sean positivos, o mayores que un tamaño específico, o que comiencen con un prefijo determinado, etc.                                                                                                                                                              |
| FOREIGN KEY        | Se trata de una comprobación de coherencia que garantiza que cada valor de esta columna corresponda a otro valor de una columna de otra tabla. Por ejemplo, si hay dos tablas, una que enumera a todos los empleados por ID y otra que enumera su información de nómina, la "LLAVE EXTRANJERA" puede garantizar que cada fila de la tabla de nómina corresponda a un empleado válido en la lista maestra de empleados. |

**Un ejemplo**

A continuación se muestra un esquema de ejemplo para la tabla Películas que hemos estado usando en las lecciones hasta ahora.

```
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    director TEXT,
    year INTEGER,
    length_minutes INTEGER
);
```

**Ejercicio**

En este ejercicio, necesitará crear una nueva tabla en la que podamos insertar algunas filas nuevas.

```
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);
```

**Ejercicio 16: Tareas**

Cree una nueva tabla nombrada Databasecon las siguientes columnas:
– NameUna cadena (texto) que describe el nombre de la base de datos
– VersionUn número (punto flotante) de la última versión de esta base de datos
– Download_countUn recuento entero del número de veces que se descargó esta base de datos
Esta tabla no tiene restricciones.

| **Inicio**            | **atrás 16**                 | **Siguiente 18**               |
| --------------------- | ---------------------------- | ------------------------------ |
| [🏠](../../README.md) | [⏪](./16_eliminar_filas.md) | [⏩](./18_modificar_tablas.md) |

---
