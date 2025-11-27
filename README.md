# Projeto de Pipeline de Dados — Data Lakehouse com ETL/ELT Completo
## Objetivo do Projeto

#### O objetivo deste projeto é construir um pipeline de dados completo, seguindo as melhores práticas de arquitetura Data Lakehouse, integrando diferentes fontes de dados (SQL), realizando ingestão, tratamento, modelagem dimensional e disponibilização analítica para dashboards.
#### Este projeto simula um ambiente corporativo real e abrange todas as etapas do ciclo de vida de engenharia de dados, desde a criação do ambiente de origem até a entrega em ferramenta de BI, incluindo documentação detalhada em MKDocs.
#### Ao final, o pipeline permitirá consultas rápidas, confiáveis e padronizadas, suportando métricas e KPIs essenciais definidos na camada Gold.
---
## Escopo Geral

### O projeto contempla:

#### 1. Arquitetura Lakehouse

- Organização das camadas Landing → Bronze → Silver → Gold

- Padrões de armazenamento em Delta Lake

-  Estruturação de buckets/pastas para o Data Lake

#### 2. Ingestão de Dados

- Extração de dados de banco SQL (Postgres/MySQL)

- Geração e carga de dados sintéticos

- Pipeline orquestrado via Airflow/Prefect

#### 3. Processamento

- Padronização inicial (Bronze)

- Limpeza, normalização e tratamento de inconsistências (Silver)

- Modelagem Dimensional com Dimensões (SCD2) e Fatos (Gold)

#### 4. Exposição Analítica

- Construção de dashboard (Power BI, Metabase etc.)

- Visualizações de KPIs e Métricas conectadas à camada Gold

#### 5. Documentação Completa

- Documentação de arquitetura, ingestão, transformações e modelo no MKDocs

- Publicação no GitHub Pages

---
## Resultado Final Esperado

#### Ao final do projeto, será entregue:

- Repositório GitHub com toda a arquitetura e código do pipeline

- Data Lake estruturado em camadas

- Pipelines orquestrados funcionando (full e incremental)

- Dashboard analítico conectado à camada Gold

- Site de documentação completo em MKDocs
