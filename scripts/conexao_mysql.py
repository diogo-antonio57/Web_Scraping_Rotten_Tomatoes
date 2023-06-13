# import librarys
import mysql.connector
import web_scraping

TABLE = 'filmes'
DATABASE = 'web_scraping'
USER = 'diogo'
PASSWORD = '34254079'

print('Connecting to the database')
try:
    connection = mysql.connector.connect(host='localhost', database=DATABASE, user=USER, password=PASSWORD)
except Exception:
    print ('Could not connect to database. Please check credentials')
else:
    print('Connected to database')
    cursor = connection.cursor()

# query to get movie name without notes
sql_select = f"select nome_filme from {TABLE} where nota is Null"

try:
    cursor.execute(sql_select)

    # get result movie name
    filmes = cursor.fetchall()
    for nome in filmes:
        # the function to get note
        nome = nome[0]

        try:
            nota = web_scraping.nota_filme(nome)
            sql_insert = f"update filmes set nota={nota} where nome_filme = '{nome}'"
        except:
            nota = 'filme_nao_encontrado'
            sql_insert = f"update filmes set obs='{nota}' where nome_filme = '{nome}'"

        # update note in table
        cursor.execute(sql_insert)
        connection.commit()
except:
    print('Could not execute insert query')

connection.close()
print('closed connection')