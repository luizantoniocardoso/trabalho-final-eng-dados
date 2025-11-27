# Diagrama da Arquitetura do Pipeline

Esta arquitetura segue o padrão **Medallion Architecture (Bronze, Silver, Gold)**, implementada em **Databricks**, para transformar o modelo transacional de origem (**PostgreSQL**) em um modelo dimensional otimizado para BI.

---

## 1. Sistema de Origem (Source)

* **Fonte:** Banco de dados relacional **PostgreSQL (Railway)** que hospeda o **Modelo Transacional** (tabelas: `clientes`, `produtos`, `vendas`, `itens_venda`, etc.).
* **Extração:** O **Airflow** é utilizado como orquestrador para disparar os *notebooks* do Databricks/PySpark que realizam a leitura e ingestão inicial.

---

## 2. Camada Bronze (Raw Imutável)

* **Função:** Ingestão bruta (`raw`) e persistência **imutável** dos dados de origem. É o primeiro ponto de controle.
* **Processo:** **PySpark** lê diretamente o PostgreSQL ou o *landing zone*.
* **Formato:** **Delta Lake** (sobre o armazenamento de objetos).
* **Regras:**
    * **Persistência 1:1:** O esquema da Bronze reflete fielmente o esquema original.
    * Adição de metadados para rastreabilidade (`data_hora_bronze`, `nome_arquivo`).
    * Nenhuma limpeza, filtro ou transformação é aplicada.

---

## 3. Camada Silver (Limpeza e Conformidade)

* **Função:** Aplicação de **Qualidade de Dados** (limpeza, padronização, deduplicação) e preparação de entidades de negócios.
* **Processo:** **PySpark / Spark SQL** lê a Camada Bronze e aplica transformações.
* **Regras:**
    * **Qualidade:** Tratamento de nulos, *deduplicação* e padronização de campos de identificação (`CPF`, `CNPJ`).
    * **Padronização:** Aplicação de **Regras de Nomenclatura** unificadas e garantia de tipagem correta.
    * Os dados são conformados e *desnormalizados parcialmente*, servindo como a *staging area* para a Camada Gold.

---

## 4. Camada Gold (Modelagem Dimensional - Consumo)

* **Função:** Modelagem final do armazém de dados (*Data Warehouse*) otimizado para análises de BI.
* **Processo:** **Spark/PySpark** lê a Camada Silver e executa a lógica de modelagem dimensional.
* **Formato:** **Delta Lake**.
* **Regras de Modelagem (Star Schema):**
    * **Dimensões:** Criação das 5 dimensões (`dim_cliente`, `dim_fornecedor`, `dim_pagamento`, `dim_produto`, `dim_transportadora`). Implementação da lógica **SCD Tipo 2** (via `MERGE`) para rastrear o histórico de mudanças.
    * **Tabela Fato:** Construção da tabela **`fato_vendas`**, ligando as métricas transacionais (`quantidade`, `valor_total`) às chaves substitutas (`sk_*`) das dimensões.
* **Output:** Modelo Dimensional Pronto para Consumo (Base Final).

---

## 5. Camada de Consumo

* **Conexão:** O **Dashboard (Visualização Databricks/Power BI)** se conecta diretamente às tabelas da **Camada Gold**.
* **Função:** Cálculo e exibição dos **4 KPIs de Vendas** (`Average Order Value`, `Top Categoria`, etc.) e das **2 Métricas de Volume** (`Vendas Mensais 12M`, `Top 5 Produtos`).

