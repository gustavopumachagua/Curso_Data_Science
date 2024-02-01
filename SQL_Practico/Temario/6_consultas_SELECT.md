| **Inicio**            | **atrás 5**                  | **Siguiente 7**            |
| --------------------- | ---------------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./5_filtrar_ordenar.md) | [⏩](./7_consulta_JOIN.md) |

---

# **Revisión de SQL: Consultas SELECT simples**

Ahora que ha probado cómo escribir una consulta básica, necesita practicar la redacción de consultas que resulvan problemas reales.

```
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

**Ejercicio**

En el siguiente ejercicio, trabajará con una tabla diferente. En cambio, esta tabla contiene información sobre algunas de las ciudades más pobladas de América del Norte, incluida su población y ubicación geoespacial en el mundo.

> ¿Sabías?
>
> Las latitudes positivas corresponden al hemisferio norte y las longitudes positivas corresponden al hemisferio oriental. Dado que América del Norte está al norte del ecuador y al oeste del primer meridiano, todas las ciudades de la lista tienen latitudes positivas y longitudes negativas.

Intente escribir algunas consultas para encontrar la información solicitada en las tareas que conoce. Es posible que debe utilizar una combinación diferente de cláusulas en su consulta para cada tarea. Una vez que haya terminado, continúe con la siguiente lección para aprender sobre consultas que abarcan varias tablas.

**Table: North_american_cities**

| **City**            | **Country**   | **Population** | **Latitude** | **Longitude** |
| ------------------- | ------------- | -------------- | ------------ | ------------- |
| Guadalajara         | Mexico        | 1500800        | 20.659699    | -103.349609   |
| Toronto             | Canada        | 2795060        | 43.653226    | -79.383184    |
| Houston             | United States | 2195914        | 29.760427    | -95.369803    |
| New York            | United States | 8405837        | 40.712784    | -74.005941    |
| Philadelphia        | United States | 1553165        | 39.952584    | -75.165222    |
| Havana              | Cuba          | 2106146        | 23.05407     | -82.345189    |
| Mexico City         | Mexico        | 8555500        | 19.432608    | -99.133208    |
| Phoenix             | United States | 1513367        | 33.448377    | -112.074037   |
| Los Angeles         | United States | 3884307        | 34.052234    | -118.243685   |
| Ecatepec de Morelos | Mexico        | 1742000        | 19.601841    | -99.050674    |
| Montreal            | Canada        | 1717767        | 45.501689    | -73.567256    |
| Chicago             | United States | 2718782        | 41.878114    | -87.629798    |

**Revisión 1: Tareas**

- **Lista todas las ciudades canadienses y sus poblaciones.**

```
SELECT city, population FROM north_american_cities
WHERE country = "Canada";
```

- **Ordene todas las ciudades de Estados Unidos por su latitud de norte a sur**

```
SELECT city, latitude FROM north_american_cities
WHERE country = "United States"
ORDER BY latitude DESC;
```

- **Enumere todas las ciudades al oeste de Chicago, ordenadas de oeste a este**

```
SELECT city, longitude FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;
```

- **Enumere las dos ciudades más grandes de México (por población)**

```
SELECT city, population FROM north_american_cities
WHERE country LIKE "Mexico"
ORDER BY population DESC
LIMIT 2;
```

- **Enumere la tercera y cuarta ciudad más grande (por población) de los Estados Unidos y su población.**

```
SELECT city, population FROM north_american_cities
WHERE country LIKE "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2;
```

| **Inicio**            | **atrás 5**                  | **Siguiente 7**            |
| --------------------- | ---------------------------- | -------------------------- |
| [🏠](../../README.md) | [⏪](./5_filtrar_ordenar.md) | [⏩](./7_consulta_JOIN.md) |

---
