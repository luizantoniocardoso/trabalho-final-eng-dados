# Dashboard Final: KPIs e Métricas de Vendas

Este dashboard padrão **One Page View** foi construído para monitorar o **Desempenho de Vendas e o Comportamento de Compra** da empresa, utilizando dados da **Camada Gold** (Data Marts Otimizados).

## Objetivo

Fornecer uma visão imediata e acionável (actionable) sobre o volume de faturamento, o valor médio das transações e o desempenho dos principais produtos e categorias.

## Visualização

<iframe src="https://dbc-44b16fbb-f52f.cloud.databricks.com/embed/dashboardsv3/01f0cb31b63b1a278bb499cb72104884?o=672160975034886" width="100%" height="800" frameborder="0"></iframe>

---

## 1. Visão Geral e KPIs Principais (Single Value Indicators)

Esta seção apresenta os indicadores de alto nível, essenciais para a saúde financeira do negócio.

| KPI | Valor no Dashboard (Exemplo) | Descrição e Fórmula |
| :--- | :--- | :--- |
| **Faturamento Mensal** | **12,86 mi** | **Receita Bruta:** Soma total dos valores de vendas (`valor_total`) no mês vigente. |
| **Valor Médio Gasto por Cliente** | **5217,76** | **Ticket Médio (AOV):** Faturamento total dividido pelo número de transações distintas (`id_venda`). |
| **Categoria Mais Vendida** | **7,2 mi** (ipsum) | **Contribuição da Categoria Top:** Faturamento total gerado pela Categoria de Produto com maior receita. |
| **A Forma de Pagamento Mais Usada** | **184,25 mi** (PIX) | **Preferência de Pagamento:** Faturamento total associado ao método de pagamento mais utilizado pelos clientes. |

---

## 2. Métricas de Análise Comportamental e Sazonalidade

### 2.1. Vendas Mensais nos Últimos 12 Meses

**Gráfico de Linhas/Barras: Tendência Sazonal**

* **Objetivo:** Analisar a **sazonalidade** e a **tendência** de vendas ao longo do último ano.
* **Métricas Exibidas:**
    * **Quantidade de Vendas (Barras Azuis):** Contagem de transações de venda (`id_venda`) por mês.
    * **Soma de Quantidade Vendidas (Linha Laranja):** Total de unidades (`quantidade`) vendidas por mês.
* **Análise (Exemplo):** O gráfico mostra um pico de volume de vendas no final de **2024-11** e uma estabilidade posterior, com uma queda notável no mês vigente (**2025-11**).

### 2.2. Os 5 Produtos Mais Vendidos

**Gráfico de Barras: Ranking de Produtos por Volume**

* **Objetivo:** Identificar os **"Best-Sellers"** em volume de unidades vendidas.
* **Métrica Exibida:** Soma da `quantidade` vendida, agrupada por `nome_produto`.
* **Análise (Exemplo):** O produto **"Digníssimos"** é o líder de volume, superando os demais produtos no Top 5. Esta métrica orienta o gerenciamento de estoque e campanhas de marketing.
