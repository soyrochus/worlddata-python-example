Os envió la tercera set de los datos. Aquí encontráis el base de datos sqlite “world-gdp.db” que contiene tablas “countries” y “gdp”. Cada file en “gpd” contiene el valor del PIB de un país por año y sui crecimiento.-

También contiene los fuentes originales (CSV)  y los scripts de Python que he utilizado para importar los datos.

 

Pero utiliza el BDD de Sqlite por favor. Y no con el interfaz de sqlite de Python pero con SQLAlchemy como definimos el lunes.

https://www.sqlalchemy.org/

 

 

Tenéis que

    Analizar los datos; que significa los campos, haya anomalías?
    Hacer un módulo / clase / Liberia (ver que vez adecuado) que se proporciona una interfaz que:

    Devuelve una lista de países con cada país una lista de años con un set de datos (tupla o dict) que contiene gdp y crecimiento
    Una series de funciones / métodos que devuelve:

        Min valor gdp con el año 
        Max valor gdp con el año 
        Promedio valor gdp por rango de años
        Min crecimiento con el año 
        Max crecimiento con el año 
        Promedio crecimiento por rango de años


Ojo: cada función debería tener un filtro que especifica:

        1 País o más países 
        Rango de años (p.e. 1970 – 1980)

    Todo hecho con TDD / pruebas unitarias. 

 

 

Podéis utilizar https://sqlitebrowser.org/ para abrir y modificar el bdd

 