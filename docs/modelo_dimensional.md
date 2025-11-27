# Modelo Dimensional – Arquitetura Medalhão (Camada Gold)

Este documento detalha o **Modelo Dimensional (Star Schema)** implementado na camada **Gold**, otimizado para o cálculo dos KPIs e Métricas de negócio.

<img src="https://github.com/luizantoniocardoso/trabalho-final-eng-dados/blob/main/assets/modelo_conceitual_ouro.jpg?raw=true" alt="Modelo Dimensional" width="800"/>

---

## 1. Visão Geral do Star Schema

O modelo é composto pelas 5 dimensões e 1 tabela fato confirmadas no ambiente Databricks.

* **5 Tabelas Dimensão (Contexto):** `dim_cliente`, `dim_fornecedor`, `dim_pagamento`, `dim_produto`, `dim_transportadora`.
* **1 Tabela Fato (Eventos):** `fato_vendas`.

---

## 2. Dimensões (Slowly Changing Dimension Type 2 - SCD2)

Todas as dimensões utilizam a implementação **SCD Tipo 2** (rastreamento histórico via `dt_inicio`, `dt_fim`, `flag_ativo`).

### `dim_cliente`

| Campo | Tipo | Descrição |
|:---|:---|:---|
| **`sk_cliente` (PK)** | `BIGINT` | **Chave Substituta** (PK na Gold). |
| **`nk_cliente`** | `INT` | **Chave Natural (NK)**: ID original do cliente. |
| `nome` | `STRING` | Nome do cliente. |
| `email`, `telefone` | `STRING` | Dados de contato. |
| `data_nascimento` | `DATE` | Data de nascimento. |
| `created_at` | `TIMESTAMP` | Data/hora de criação do registro de origem. |
| `dt_inicio`, `dt_fim` | `TIMESTAMP` | **Vigência SCD2**. |
| `flag_ativo` | `STRING` | Flag SCD2 (`TRUE`/`FALSE`). |

---

### `dim_fornecedor`

| Campo | Tipo | Descrição |
|:---|:---|:---|
| **`sk_fornecedor` (PK)** | `BIGINT` | **Chave Substituta**. |
| **`nk_fornecedor`** | `INT` | **Chave Natural (NK)**. |
| `nome` | `STRING` | Nome / Razão social. |
| `cnpj` | `STRING` | CNPJ. |
| `telefone`, `email` | `STRING` | Dados de contato. |
| `dt_inicio`, `dt_fim` | `TIMESTAMP` | Vigência SCD2. |
| `flag_ativo` | `STRING` | Flag SCD2. |

---

### `dim_produto`

| Campo | Tipo | Descrição |
|:---|:---|:---|
| **`sk_produto` (PK)** | `BIGINT` | **Chave Substituta**. |
| **`nk_produto`** | `INT` | **Chave Natural (NK)**. |
| `nome` | `STRING` | Nome do Produto. |
| `categoria` | `STRING` | Categoria (Usado no KPI Top Categoria). |
| `preco` | `DOUBLE` | Preço no momento da vigência. |
| `fornecedor_id` | `INT` | FK para a chave natural do fornecedor (para rastreamento). |
| `dt_inicio`, `dt_fim` | `TIMESTAMP` | Vigência SCD2. |
| `flag_ativo` | `STRING` | Flag SCD2. |

---

### `dim_transportadora`

| Campo | Tipo | Descrição |
|:---|:---|:---|
| **`sk_transportadora` (PK)** | `BIGINT` | **Chave Substituta**. |
| **`nk_transportadora`** | `INT` | **Chave Natural (NK)**. |
| `nome` | `STRING` | Nome da Transportadora. |
| `telefone`, `email` | `STRING` | Dados de contato. |
| `dt_inicio`, `dt_fim` | `TIMESTAMP` | Vigência SCD2. |
| `flag_ativo` | `STRING` | Flag SCD2. |

---

### `dim_pagamento`

| Campo | Tipo | Descrição |
|:---|:---|:---|
| **`sk_pagamento` (PK)** | `BIGINT` | **Chave Substituta**. |
| **`nk_pagamento`** | `INT` | **Chave Natural (NK)**. |
| `id_venda` | `INT` | ID original da Venda (Chave Degenerada para rastreio). |
| `forma_pagamento` | `STRING` | Método de pagamento (Usado no KPI Top Forma de Pagamento). |
| `status` | `STRING` | Status final do pagamento. |
| `valor` | `DOUBLE` | Valor transacionado. |

---

## 3. Fato – `fato_vendas`

Tabela central de granularidade de **transação/item**, conectando todas as dimensões e centralizando as métricas.

| Campo | Tipo | Descrição |
|:---|:---|:---|
| `sk_cliente` | `BIGINT` | **FK** para `dim_cliente` (versão correta SCD2). |
| `sk_produto` | `BIGINT` | **FK** para `dim_produto` (versão correta SCD2). |
| `sk_pagamento` | `BIGINT` | **FK** para `dim_pagamento`. |
| `sk_transportadora` | `BIGINT` | **FK** para `dim_transportadora`. |
| **`id_venda`** | `INT` | ID original da Venda (Chave Degenerada). |
| `quantidade` | `INT` | **Métrica Aditiva**: Quantidade vendida (Usado em Top 5 Produtos). |
| `valor_total` | `DOUBLE` | **Métrica Aditiva**: Valor total (Usado em AOV e Faturamento). |
| `data_venda` | `TIMESTAMP` | Data do evento. |
| *Outras colunas* | *INT/DOUBLE* | *Preço unitário, subtotal, etc.* |
