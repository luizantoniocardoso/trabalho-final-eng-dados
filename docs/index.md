# Trabalho Final – Engenharia de Dados  

## Documentação Oficial do Projeto

Bem-vindo à documentação do Trabalho Final da disciplina de **Engenharia de Dados**, desenvolvido em equipe, utilizando a **Arquitetura Medalhão (Bronze, Silver e Gold)** no **Databricks**.

Use o menu à esquerda para navegar entre as seções.

# 1. Objetivo do Projeto

O objetivo deste trabalho é construir um **pipeline completo de engenharia de dados**, desde a ingestão de um banco relacional até a criação de **camadas Bronze, Silver e Gold**, aplicando boas práticas de:

- Ingestão de dados  
- Limpeza e padronização (ETL/ELT)  
- Modelagem dimensional  
- Criação de tabelas SCD2  
- Geração de KPIs e métricas  
- Armazenamento em Delta Lake  
- Processamento no Databricks  

---

# 2. Equipe

Trabalho desenvolvido em grupo

> **Integrantes:**  

> - ALEXANDRE SARTOR TEIXEIRA
> - CRISTHIAN CARDOSO BERTAN
> - LUIZ CARDOSO ANTONIO
> - CRISTOFFER FIGUEIREDO MARTINS
> - DAVI CARLOS FREITAS
> - GUILHERME ZAPELINI DA ROSA SCHWA
> - TIAGO SILVEIRA DE BITTENCOURT

---

# 3. Arquitetura Geral

O projeto foi construído utilizando a **Arquitetura Medalhão**, composta pelas seguintes camadas:

### Bronze  

- Dados crus extraídos do PostgreSQL (Railway).  
- Nenhuma transformação aplicada.  
- Estrutura original preservada.

### Silver  

- Dados tratados e padronizados.  
- Normalização de schemas.  
- Remoção de nulos, duplicidades e inconsistências.

### Gold

- Modelagem dimensional.  
- Implementação de SCD2.  
- Criação de tabelas fato e dimensões.  
- Base final para KPIs e métricas.

---

# 4. Pipeline de Dados (Medalhão)

O fluxo do pipeline segue as etapas abaixo:

### **1. Extração**

- Conexão com o banco PostgreSQL hospedado no Railway.  
- Leitura das tabelas originais.

### **2. Bronze**

- Armazenamento bruto no Delta Lake.  
- Sem alteração de tipos ou nomes.

### **3. Silver**

- Limpeza dos dados.  
- Padronização de nomes e tipos.  
- Tratamento de colunas como CPF, email, telefone etc.  
- Deduplicação.

### **4. Gold**

- Aplicação de SCD2.  
- Criação de dimensões e fatos.  
- Preparação dos dados analíticos.

---

# 5. Modelos de Dados

Entidades principais do sistema:

- **Clientes**
- **fornecedores**
- **produtos**
- **pagamento**
- **transportadoras**
- **vendas**

Na camada Gold, os dados serão organizados em:

### **Dimensões**

- `dim_cliente`
- `dim_fornecedor`  
- `dim_pagamento`
- `dim_produto`  
- `dim_transportadora`

### **Tabela Fato**

- `fato_vendas`

---

# 6. 📊 KPIs

Serão **4 KPIs** Definidos pela equipe:

- KPI - Average Revenue *Receita Média*
- KPI - Average Order Value - AOV *Valor Médio de Pedido*
- KPI - Top Categoria *Categoria Mais Vendida*
- KPI - Top Forma de Pagamento *Forma de Pagamento Mais Utilizada*

---

# 8. 7 Métricas 

Serão **2 métricas**, como:

- Métrica - vendas mensais *Vendas Mensais nos ultimos 12 meses*
- Métrica - Top 5 Produtos *Produtos Mais Vendidos*

---

# 9. 🛠 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|-----------|------------|
| **Databricks** | Execução dos notebooks e processamento distribuído |
| **Delta Lake** | Armazenamento estruturado das camadas Bronze/Silver/Gold |
| **Airflow** | Orquestração da pipeline |
| **PySpark / Spark SQL** | Transformações e processamento |
| **PostgreSQL (Railway)** | Banco de origem |
| **GitHub** | Versionamento |
| **Databricks** | Visualização de KPIs |

---
