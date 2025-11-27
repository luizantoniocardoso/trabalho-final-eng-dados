# Dashboard Final: Qualidade e Cobertura de Dados Mestres

Este dashboard padrão **One Page View** foi construído para monitorar a **Qualidade e Cobertura dos Dados Mestres (Master Data)** na Camada Gold, utilizando as regras de dimensionalidade e rastreamento histórico (**SCD Tipo 2**).

## Objetivo

Documentar os principais indicadores de Qualidade de Dados e o Perfil Demográfico da base de clientes, validando o processamento SCD Tipo 2.

## Visualização

<iframe src="https://dbc-44b16fbb-f52f.cloud.databricks.com/embed/dashboardsv3/01f0cb31b63b1a278bb499cb72104884?o=672160975034886" width="100%" height="800" frameborder="0"></iframe>

---

## 1. Visão Geral e KPIs Principais

Esta seção apresenta os indicadores de volume e qualidade dos dados mestres.

| KPI | Valor na Amostra | Descrição e Fórmula |
| :--- | :--- | :--- |
| **Total de clientes ativos** | 5 mil | **Tamanho da Base Ativa:** Contagem total dos registros de clientes onde `FLAG_ATIVO = TRUE`. |
| **Clientes com endereço Válido** | 0,75 | **Taxa de Cobertura de Endereço:** Porcentagem de clientes ativos que possuem um endereço válido e vigente (75% de cobertura). |
| **Total de estados ativos** | 27 | **Cobertura Geográfica:** Contagem de estados distintos na dimensão de endereços. |
| **Diversidade de categorias** | 182 | **Variedade de Produtos:** Contagem de categorias de produtos ativas (`FLAG_ATIVO = TRUE`). |

---

## 2. Métricas de Análise Dimensional

### 2.1. Distribuição de Vigência (SCD Tipo 2)

**Gráfico de Pizza: Vigente vs. Histórico**

* **Objetivo:** Medir a proporção de registros que estão ativos *versus* os que foram versionados (historizados) na dimensão (exemplo: Fornecedores).
* **Análise:** Na amostra, 100.00% estão classificados como **'1 - Vigente (Linha Atual)'**. Isso indica que, até o momento da carga, não houve alterações na base que gerassem linhas históricas (`DATA_FIM_VIGENCIA` não nula).

### 2.2. Perfil Demográfico (Faixa Etária)

**Gráfico de Barras: Total de Clientes por Faixa Etária**

* **Objetivo:** Analisar a distribuição demográfica da base ativa de clientes (`gold.clientes`).
* **Análise:** O gráfico mostra que a faixa **65+** (a mais à esquerda) possui o maior volume de clientes ativos, e a faixa **18-24** (a mais à direita) possui o menor volume. Esta métrica ajuda a orientar estratégias de segmentação.
