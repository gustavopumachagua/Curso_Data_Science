| **Inicio**            | **atrás 19**                  | **Siguiente 21**                  |
| --------------------- | ----------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./19_eliminar_tablas.md) | [⏩](./21_uniones_excepciones.md) |

---

# **Tema SQL: Subconsultas**

Es posible que haya notado que incluso con una consulta completa, hay muchas preguntas que no podemos responder sobre nuestros datos sin una publicación o procesamiento previo adicional. En estos casos, puede realizar varias consultas y procesar los datos usted mismo, o puede crear una consulta más compleja utilizando subconsultas SQL.

**Ejemplo: subconsulta general**

Digamos que su empresa tiene una lista de todos los Asociados de Ventas, con datos sobre los ingresos que genera cada Asociado y su salario individual. Los tiempos son difíciles y ahora desea saber cuáles de sus Asociados le están costando a la empresa más que el ingreso promedio generado por Asociado.

Primero, necesitaría calcular los ingresos promedio que generan todos los Asociados:

```
SELECT AVG(revenue_generated)
FROM sales_associates;
```

Y luego, usando ese resultado, podemos comparar los costos de cada uno de los Asociados con ese valor. Para usarlo como subconsulta, podemos escribirlo directamente en la **WHERE** cláusula de la consulta:

```
SELECT *
FROM sales_associates
WHERE salary >
   (SELECT AVG(revenue_generated)
    FROM sales_associates);
```

A medida que se ejecuta la restricción, el salario de cada Asociado se comparará con el valor consultado en la subconsulta interna.

Se puede hacer referencia a una subconsulta en cualquier lugar donde se pueda hacer referencia a una tabla normal. Dentro de una **FROM** cláusula, puede realizar **JOIN** subconsultas con otras tablas, dentro de una restricción **WHERE** o **HAVING**, puede probar expresiones con los resultados de la subconsulta, e incluso en expresiones de la **SELECT** cláusula, que le permiten devolver datos directamente desde la subconsulta. Generalmente se ejecutan en el mismo orden lógico que la parte de la consulta en la que aparecen, como se describió en la última lección.

Debido a que las subconsultas se pueden anidar, cada subconsulta debe estar completamente entre paréntesis para establecer la jerarquía adecuada. De lo contrario, las subconsultas pueden hacer referencia a cualquier tabla de la base de datos y hacer uso de las construcciones de una consulta normal (aunque algunas implementaciones no permiten que las subconsultas utilicen **LIMIT** o **OFFSET**).

## **Subconsultas correlacionadas**

Un tipo de subconsulta más potente es la subconsulta correlacionada en la que la consulta interna hace referencia a una columna o alias de la consulta externa y depende de ella. A diferencia de las subconsultas anteriores, cada una de estas consultas internas debe ejecutarse para cada una de las filas de la consulta externa, ya que la consulta interna depende de la fila de consulta externa actual.

**Ejemplo: subconsulta correlacionada**

En lugar de la lista anterior solo de Asociados de Ventas, imagine si tiene una lista general de Empleados, sus departamentos (ingeniería, ventas, etc.), ingresos y salario. Esta vez, está buscando en toda la empresa los empleados que se desempeñan peor que el promedio en su departamento.

Para cada empleado, deberá calcular su costo en relación con los ingresos promedio generados por todas las personas de su departamento. Para tomar el promedio del departamento, la subconsulta necesitará saber en qué departamento se encuentra cada empleado:

```
SELECT *
FROM employees
WHERE salary >
   (SELECT AVG(revenue_generated)
    FROM employees AS dept_employees
    WHERE dept_employees.department = employees.department);
```

Este tipo de consultas complejas pueden ser poderosas, pero también difíciles de leer y comprender, por lo que debes tener cuidado al usarlas. Si es posible, intente asignar alias significativos a las tablas y valores temporales. Además, las subconsultas correlacionadas pueden ser difíciles de optimizar, por lo que las características de rendimiento pueden variar entre diferentes bases de datos.

## **Pruebas de existencia**

Cuando introdujimos **WHERE** restricciones en la Lección 2: Consultas con restricciones , el **IN** operador se usó para probar si el valor de la columna en la fila actual existía en una lista fija de valores. En consultas complejas, esto se puede ampliar mediante subconsultas para probar si existe un valor de columna en una lista dinámica de valores.

```
SELECT *, …
FROM mytable
WHERE column
    IN/NOT IN (SELECT another_column
               FROM another_table);
```

Al hacer esto, observe que la subconsulta interna debe seleccionar un valor de columna o expresión para producir una lista con la que se pueda probar el valor de la columna externa. Este tipo de restricción es poderosa cuando las restricciones se basan en datos actuales.

| **Inicio**            | **atrás 19**                  | **Siguiente 21**                  |
| --------------------- | ----------------------------- | --------------------------------- |
| [🏠](../../README.md) | [⏪](./19_eliminar_tablas.md) | [⏩](./21_uniones_excepciones.md) |

---
