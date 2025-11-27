FROM apache/airflow:2.8.1-python3.11

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libpq-dev \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir \
    apache-airflow-providers-postgres==5.10.0 \
    apache-airflow-providers-databricks==6.0.0 \
    psycopg2-binary==2.9.9 \
    pandas==2.1.4

WORKDIR /opt/airflow
