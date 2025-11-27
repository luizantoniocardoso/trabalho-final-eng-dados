<<<<<<< HEAD
# Arquitetura do Pipeline

Descreva aqui a arquitetura geral da solução.
=======
# Diagrama da Arquitetura do Pipeline

Esta arquitetura segue o padrão **Medallion Architecture (Bronze, Silver, Gold)**, implementada em **Databricks**, para transformar o modelo transacional de origem em um modelo dimensional otimizado para BI.

---

## 1. Sistema de Origem

* **Fonte:** Banco de dados relacional que contém o **Modelo Transacional** (as 10+ tabelas: `vendas`, `itens_venda`, `clientes`, `produtos`, `fornecedores`, etc.).
* **Extração:** Utiliza-se a ferramenta de **Orquestração** (ex: Databricks Workflows ou Airflow) para disparar o carregamento.

---

## 2. 🥉 Camada Bronze (Raw Padronizado)

* **Função:** Ingestão *raw* e padronização do formato de armazenamento.
* **Processo:** **Spark/PySpark** lê o volume Landing (CSV/JSON).
* **Formato:** **Delta Lake**.
* **Regras:** * Persistência 1:1 dos dados de origem.
    * Adição de colunas de metadados (`data_hora_bronze`, `nome_arquivo`) para rastreabilidade.

---

## 3. 🥈 Camada Silver (Refinamento e Conformidade)

* **Função:** Limpeza, padronização e regras de qualidade.
* **Processo:** **Spark/PySpark** lê a Bronze.
* **Regras:**
    * **Qualidade:** Aplicação de **Regras de Nomenclatura** unificadas (ex: `CD_` $\to$ `CODIGO_`, `UPPERCASE`).
    * Remoção de colunas de auditoria antigas e adição de rastreamento Silver.
    * Os dados são limpos e conformados, servindo como a *staging area* para a Gold.

---

## 4. 🥇 Camada Gold (Modelagem Dimensional - Consumo)

* **Função:** Modelagem de Dados para consumo de BI e KPIs.
* **Processo:** **Spark/PySpark** lê a Silver.
* **Formato:** **Delta Lake**.
* **Regras de Modelagem:**
    * **Dimensões:** Implementação da lógica **SCD Tipo 2** para rastrear o histórico das 5 dimensões: `clientes`, `enderecos`, `fornecedores`, `produtos`, `transportadoras`.
    * **Tabela Fato:** Construção da tabela **`fato_vendas`** (agregação de transações de vendas, itens, pagamentos e entregas).
* **Output:** Modelo Dimensional (*Star Schema*).

---

## 5. Camada de Consumo

* **Conexão:** O **Dashboard** (Power BI, Superset, etc.) se conecta diretamente à **Camada Gold**.
* **Função:** Cálculo dos **4 KPIs e 2 Métricas**
>>>>>>> origin/main
