FROM quay.io/astronomer/astro-runtime:7.2.0

RUN AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True