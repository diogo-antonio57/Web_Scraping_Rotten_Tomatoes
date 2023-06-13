# Import librarys
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Variables
conexao_sql = '~/Documentos/Projetos Python/Web_Scraping_ETL/Scripts/conexao_mysql.py'

# defining DAGS arguments
default_args = {
    'owner': 'Diogo',
    'start_date': days_ago(0),
    'email': ['diogoantonio57@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# define the DAG
dag = DAG(
    dag_id = 'Notas_Filmes',
    default_args = default_args,
    description = 'Gets the film note of rotten tomatoes with web scraping',
    schedule_interval = timedelta(hours=12)
)

# define the tasks
# task the call connection with mysql and write films note
nota_filme = BashOperator(
    task_id = 'nota_filme',
    bash_command = f'python 3 {conexao_sql}',
    dag = dag
) 

nota_filme
