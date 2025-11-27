"""
DAG FINAL: Adaptada para o formato Multi-Task Jobs/Runs (necessário para Serverless Compute)
e usando o warehouse_id.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from airflow.operators.dummy import DummyOperator 

# Configurações de conexão
DATABRICKS_CONN_ID = "databricks_default"

NOTEBOOK_PATH_001 = "/Workspace/Users/engdados620@gmail.com/001" # Criação de Schemas
NOTEBOOK_PATH_002 = "/Workspace/Users/engdados620@gmail.com/002" # Leitura CSV -> Bronze
NOTEBOOK_PATH_003 = "/Workspace/Users/engdados620@gmail.com/003" # Transformação Bronze -> Silver
NOTEBOOK_PATH_004 = "/Workspace/Users/engdados620@gmail.com/004" # Modelagem Silver -> Gold/SCD2

WAREHOUSE_ID = # INSIRA O ID DO SQL WAREHOUSE SERVERLESS AQUI


# Argumentos padrão da DAG
default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(hours=2),
}

# Definição da DAG
with DAG(
    dag_id="full_medalhao_pipeline_final",
    default_args=default_args,
    description="Orquestra o fluxo completo Bronze -> Silver -> Gold no Databricks usando Serverless.",
    schedule_interval="0 2 * * *", 
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["databricks", "medalhao", "full_elt"],
    max_active_runs=1,
) as dag:

    start = DummyOperator(task_id="START_PIPELINE")
    end = DummyOperator(task_id="END_PIPELINE")
    
    # --- FASE 1: SETUP (Notebook 001) ---
    setup_schemas = DatabricksSubmitRunOperator(
        task_id="setup_create_schemas",
        databricks_conn_id=DATABRICKS_CONN_ID,
        json={
            "run_name": "Setup_Schemas",
            "tasks": [
                {
                    "task_key": "setup_schemas_task",
                    "sql_warehouse_id": WAREHOUSE_ID,
                    "notebook_task": {
                        "notebook_path": NOTEBOOK_PATH_001,
                    },
                }
            ]
        },
        do_xcom_push=True,
    )

    # --- FASE 2: INGESTÃO E BRONZE (Notebook 002) ---
    ingest_to_bronze = DatabricksSubmitRunOperator(
        task_id="ingest_csv_to_bronze",
        databricks_conn_id=DATABRICKS_CONN_ID,
        json={
            "run_name": "Ingest_to_Bronze",
            "tasks": [
                {
                    "task_key": "ingest_to_bronze_task",
                    "sql_warehouse_id": WAREHOUSE_ID,
                    "notebook_task": {
                        "notebook_path": NOTEBOOK_PATH_002,
                    },
                }
            ]
        },
        do_xcom_push=True,
    )

    # --- FASE 3: TRANSFORMAÇÃO E SILVER (Notebook 003) ---
    transform_to_silver = DatabricksSubmitRunOperator(
        task_id="transform_to_silver",
        databricks_conn_id=DATABRICKS_CONN_ID,
        json={
            "run_name": "Transform_to_Silver",
            "tasks": [
                {
                    "task_key": "transform_silver_task",
                    "sql_warehouse_id": WAREHOUSE_ID,
                    "notebook_task": {
                        "notebook_path": NOTEBOOK_PATH_003,
                    },
                }
            ]
        },
        do_xcom_push=True,
    )
    
    # --- FASE 4: MODELAGEM E GOLD (Notebook 004) ---
    model_to_gold_scd2 = DatabricksSubmitRunOperator(
        task_id="model_to_gold_scd2",
        databricks_conn_id=DATABRICKS_CONN_ID,
        json={
            "run_name": "Model_to_Gold_SCD2",
            "tasks": [
                {
                    "task_key": "model_gold_task",
                    "sql_warehouse_id": WAREHOUSE_ID,
                    "notebook_task": {
                        "notebook_path": NOTEBOOK_PATH_004,
                    },
                }
            ]
        },
        do_xcom_push=True,
    )

    
    start >> setup_schemas >> ingest_to_bronze >> transform_to_silver >> model_to_gold_scd2 >> end