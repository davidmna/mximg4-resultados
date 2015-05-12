# mximg4-resultados
Este repositorio contiene varios scripts para procesar los resultados del concurso de fotografía **[México en una imagen 2014](http://www.lohechoenmexico.mx/mximg4/)**.

###concurso1.py
Este script recibe el ID de la fotografía cargada en el concurso:
```sh
python concurso1.py 78
```
Resultado:
```sh
Id: 78
Autor: Felipe Alberto Flores
Votos: 2
Imagen: m_78_1511193_282636825218863_1322799978_n.jpg
Texto: Col
```
###concurso2.py
Este script procesa todos los registros de todas las fotografías cargadas en el concurso y los guarda en una tabla de MySQL. La estructura de la tabla es la siguiente:
```sql
CREATE TABLE `photos` (
  `id` int(11) NOT NULL,
  `author` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `votes` int(11) DEFAULT NULL,
  `image` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `text` text COLLATE utf8_spanish_ci,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
```
Se configura la conexión a partir de la [línea #8](https://github.com/davidmna/mximg4-resultados/blob/master/concurso2.py#L8):
```python
cnx = mysql.connector.connect(
		user='root', 
		password='', 
		host='localhost',
		database='mximg4')
```
El script se ejecuta sin parámetros:
```sh
python concurso2.py
```
En consola va mostrando las fotografías que se han procesado:
```sh
$ python concurso2.py
Id: 1, Votos: 7
Id: 2, Votos: 2
Id: 3, Votos: 9
Id: 4, Votos: 1
Id: 6, Votos: 196
Id: 7, Votos: 19
Id: 8, Votos: 363
Id: 9, Votos: 15
Id: 10, Votos: 274
````
Un dump de la [base de datos completa](https://github.com/davidmna/mximg4-resultados/blob/master/assets/mximg4.sql) se encuentra en assets.

###concurso3.py

Pendiente.
