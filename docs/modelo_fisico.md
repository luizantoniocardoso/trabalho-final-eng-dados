## Modelo Físico (DDL)

Este documento apresenta o modelo físico do banco de dados relacional utilizado como
fonte do pipeline de dados deste projeto. O banco foi implementado em **PostgreSQL**
e contém as tabelas relacionadas ao domínio de vendas de e-commerce.

O script completo de criação das tabelas pode ser encontrado em:

`sql/create_ecommerce_schema.sql`

## Entidades do modelo físico

| Tabela | Descrição |
|--------|-----------|
| clientes | Informações dos clientes cadastrados |
| enderecos | Endereços associados aos clientes |
| vendas | Informações gerais das vendas |
| itens_venda | Itens pertencentes a cada venda |
| produtos | Catálogo de produtos |
| estoque | Disponibilidade de produtos por fornecedor |
| fornecedores | Informações dos fornecedores |
| transportadoras | Transportadoras parceiras |
| entregas | Rastreamento e status de envio |
| pagamentos | Dados de pagamento das vendas |

## Trecho ilustrativo do DDL

```sql
CREATE TABLE clientes (
    cliente_id     SERIAL PRIMARY KEY,
    nome           VARCHAR(100) NOT NULL,
    sobrenome      VARCHAR(100) NOT NULL,
    cpf            VARCHAR(14)  NOT NULL UNIQUE,
    email          VARCHAR(150) NOT NULL UNIQUE,
    data_cadastro  DATE         NOT NULL
);
