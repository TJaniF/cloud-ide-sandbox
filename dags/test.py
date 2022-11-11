"""
test
DAG auto-generated by Astro Build.
"""

from airflow.decorators import dag
from airflow.operators.bash import BashOperator as ALIASEDBashOperator
from astro import sql as aql
import pandas as pd
import pendulum


@aql.dataframe(task_id="cell_1")
def cell_1_func():
    # Write your code here...
    print("THIS IS THE CLOUD IDE")

@dag(
    schedule_interval=None,
    start_date=pendulum.from_format("2022-11-01", "YYYY-MM-DD"),
)
def test():
    
    t1 = ALIASEDBashOperator(task_id="my_task_231942", bash_command="echo hi") 

dag_obj = test()
