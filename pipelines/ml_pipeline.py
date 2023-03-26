from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator


default_args = {
    "owner": "ericdasse28",
    "depends_on_past": False,
    "email": ["ericdasse28@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "start_date": datetime(2023, 3, 24),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# etl_dag = DAG(dag_id="ML", default_args=default_args)
with DAG(
    "ML",
    default_args=default_args,
    description="A simple ML pipeline",
    schedule=timedelta(hours=1),
    start_date=datetime(2023, 3, 23),
    catchup=False,
    tags=["example"],
) as ml_dag:
    task_1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    task_2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    task_1.doc_md = dedent(
        """\
        #### Task documentation
        You can document your task using the attributes `doc_md` (markdown),
        `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
        rendered in the UI's Task Instance Details page.
        
        ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
        """
    )

    ml_dag.doc_md = """
    This is some documentation
    """

    templated_command = dedent(
        """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7) }}"
        {% endfor %}
        """
    )

    task_3 = BashOperator(
        task_id="templated", depends_on_past=False, bash_command=templated_command
    )

    task_1 >> [task_2, task_3]
