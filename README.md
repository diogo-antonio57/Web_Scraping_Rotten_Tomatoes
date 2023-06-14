# Web_Scraping_Rotten_Tomatoes
This project is about learning use web scraping and connect python with mysql.

## About this project
This project use web scraping and Beautifulsoup library for get the movie grade, obtained of Rotten Tomatoes site.
In mysql have a table with the movie name, when execute the script, the python connect in mysql get the movie name and send for fuction of web scraping, which use the name for create url of Rotten Tomatoes site, after inserts the note in mysql table.

### Table Mysql
The mysql table have 3 columns: film_name, note and obs
The column Obs serves to when film isn't  find, writing a message Film not found
Example:
| film_name | note | obs |
| --------- | ---- | --- |
| shrek_2   | 89   |     |
| baby_driver | 92 |     |
| baby_driiveer |  | film not found |

## structure of directories

```
├── LICENSE
├── README.md
├── scripts <- scripts developed
│ ├── airflow_filmes.py
│ ├── conexao_mysql.py
│ ├── web_scraping.py
```
