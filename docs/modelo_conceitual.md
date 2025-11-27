# Modelo Conceitual

O modelo conceitual representa o domínio de negócio do e-commerce, de forma
independente de tecnologia, mostrando apenas **entidades** e **relacionamentos**.

## Entidades

- **Cliente**
- **Endereço**
- **Vendas**
- **Itens_venda**
- **Produtos**
- **Estoque**
- **Fornecedores**
- **Transportadoras**
- **Entregas**
- **Pagamentos**

## Relacionamentos (cardinalidades)

- Um **Cliente** possui **N Endereços** (1:N)
- Um **Cliente** realiza **N Vendas** (1:N)
- Uma **Venda** contém **N Itens_venda** (1:N)
- Cada **Item_venda** refere **1 Produto** (N:1)
- Um **Produto** pode ter **N registros de Estoque** e cada um está ligado a **1 Fornecedor** (Produto 1:N Estoque N:1 Fornecedores)
- Uma **Venda** gera **N Pagamentos** (1:N)
- Uma **Venda** gera **1 Entrega**, e cada **Transportadora** realiza **N Entregas** (Vendas 1:1 Entregas N:1 Transportadoras)
- Uma **Venda** usa **1 Endereço** de entrega (Vendas N:1 Endereço)

## Diagrama

Abaixo, o diagrama conceitual em notação ER utilizado no projeto:

<img src="https://github.com/luizantoniocardoso/trabalho-final-eng-dados/blob/main/assets/modelo_conceitual.jpg?raw=true" alt="Modelo Conceitual" width="800"/>