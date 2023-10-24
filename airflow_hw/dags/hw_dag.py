import datetime as dt
import os
import sys

from airflow.models import DAG
from airflow.operators.python import PythonOperator


path = '.'
# Добавим путь к коду проекта в переменную окружения, чтобы он был доступен python-процессу
os.environ['PROJECT_PATH'] = path
# Добавим путь к коду проекта в $PATH, чтобы импортировать функции
sys.path.insert(0, path)


from modules.pipeline  import pipeline as ppl
from modules.predict import predict as pdt


args = {
    'owner': 'ME! I own it! mwuhahah3',
    'start_date': dt.datetime(2022, 6, 10),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='car_price_prediction_homework',
        schedule_interval="00 15 * * *",
        default_args=args,
) as dag:
    pipeline = PythonOperator(
        task_id='pipeline',
        python_callable=ppl,
    )
    predict = PythonOperator(
        task_id='predict',
        python_callable=pdt,
    )
    #
    pipeline>>predict
    pipeline.set_downstream(predict)

