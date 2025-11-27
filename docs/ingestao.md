# Pipeline de Ingestão – Arquitetura Medalhão (Databricks + Airflow)

Este documento descreve a **pipeline completa de ingestão e transformação de dados** utilizada no projeto, implementada com **Airflow**, **Databricks** e baseada na **arquitetura Medalhão (Bronze → Silver → Gold)**.

A DAG realiza a orquestração do fluxo de dados desde o **Bronze (Raw/Landing)** até a **camada Gold**, onde o modelo dimensional é construído.

---

## Arquitetura Geral

<img src="https://github.com/luizantoniocardoso/trabalho-final-eng-dados/blob/main/assets/diagrama_pipeline.jpeg?raw=true" alt="Diagrama da Pipeline" width="800"/>

A pipeline segue as três camadas da arquitetura medalhão:

| Camada | Descrição | Objetivo |
|-------|-----------|-----------|
| **Bronze (Raw/Landing)** | Armazena os dados brutos vindos do banco de origem | Preservação máxima, sem transformações |
| **Silver (Tratada/Normalizada)** | Dados limpos, padronizados e com tipos ajustados | Servir de base consistente para o Gold |
| **Gold (Modelo Dimensional)** | Tabelas **dimensionais** e **fatos** | Aplicações analíticas e dashboards |

### **Tabelas criadas na Gold**

### **Dimensões**

- `dim_cliente`
- `dim_fornecedor`  
- `dim_pagamento`
- `dim_produto`  
- `dim_transportadora`

### **Tabela Fato**

- `fato_vendas`

---

## Orquestração com Airflow + Databricks

A pipeline foi construída utilizando:

- **Airflow** (DAG principal)
- **Databricks Serverless SQL Warehouse**
- **Notebooks Databricks** (execução via `DatabricksSubmitRunOperator`)

Cada etapa do fluxo executa um notebook:

| Fase | Notebook | Função |
|------|----------|--------|
| Setup | `001` | Criação dos schemas e estruturas iniciais |
| Ingestão | `002` | Extração do banco Postgres → Bronze |
| Transformação | `003` | Bronze → Silver |
| Modelagem | `004` | Silver → Gold (SCD2) |
