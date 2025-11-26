import psycopg2
import os
import time

DB_HOST = # HOST DO BANCO
DB_NAME = # NOME DO BANCO
DB_USER = # USUARIO DO BANCO
DB_PASS = # SENHA DO BANCO
DB_PORT = # PORTA DO BANCO


def tabela_existe(cursor, tabela):
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = %s
        );
    """, (tabela,))
    return cursor.fetchone()[0]

DDL_TABELAS = {
    "clientes": """
        CREATE TABLE clientes (
            id_cliente BIGINT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            telefone VARCHAR(20),
            data_nascimento DATE,
            created_at TIMESTAMP NOT NULL
        );
    """,
    "enderecos": """
        CREATE TABLE enderecos (
            id_endereco BIGINT PRIMARY KEY,
            id_cliente BIGINT NOT NULL,
            logradouro VARCHAR(200),
            numero VARCHAR(20),
            bairro VARCHAR(100),
            cidade VARCHAR(100),
            estado CHAR(2),
            cep VARCHAR(10),
            created_at TIMESTAMP NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        );
    """,
    "produtos": """
        CREATE TABLE produtos (
            id_produto BIGINT PRIMARY KEY,
            nome VARCHAR(150) NOT NULL,
            categoria VARCHAR(100),
            preco DECIMAL(10,2) NOT NULL,
            created_at TIMESTAMP NOT NULL
        );
    """,
    "estoque": """
        CREATE TABLE estoque (
            id_produto BIGINT PRIMARY KEY,
            quantidade INT NOT NULL,
            updated_at TIMESTAMP NOT NULL,
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        );
    """,
    "vendas": """
        CREATE TABLE vendas (
            id_venda BIGINT PRIMARY KEY,
            id_cliente BIGINT NOT NULL,
            valor_total DECIMAL(10,2) NOT NULL,
            data_venda TIMESTAMP NOT NULL,
            status_pagamento VARCHAR(30),
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        );
    """,
    "itens_venda": """
        CREATE TABLE itens_venda (
            id_item BIGINT PRIMARY KEY,
            id_venda BIGINT NOT NULL,
            id_produto BIGINT NOT NULL,
            quantidade INT NOT NULL,
            valor_unitario DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        );
    """,
    "pagamentos": """
        CREATE TABLE pagamentos (
            id_pagamento BIGINT PRIMARY KEY,
            id_venda BIGINT NOT NULL,
            metodo_pagamento VARCHAR(50),
            valor_pago DECIMAL(10,2),
            data_pagamento TIMESTAMP,
            FOREIGN KEY (id_venda) REFERENCES vendas(id_venda)
        );
    """,
    "transportadoras": """
        CREATE TABLE transportadoras (
            id_transportadora BIGINT PRIMARY KEY,
            nome VARCHAR(150),
            cnpj VARCHAR(20),
            created_at TIMESTAMP NOT NULL
        );
    """,
    "entregas": """
        CREATE TABLE entregas (
            id_entrega BIGINT PRIMARY KEY,
            id_venda BIGINT NOT NULL,
            id_transportadora BIGINT NOT NULL,
            status_entrega VARCHAR(30),
            data_envio TIMESTAMP,
            data_entrega TIMESTAMP,
            FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
            FOREIGN KEY (id_transportadora) REFERENCES transportadoras(id_transportadora)
        );
    """,
    "fornecedores": """
        CREATE TABLE fornecedores (
            id_fornecedor BIGINT PRIMARY KEY,
            nome VARCHAR(150),
            cnpj VARCHAR(20),
            telefone VARCHAR(20),
            created_at TIMESTAMP NOT NULL
        );
    """
}

COPY_MAP = [
    ("clientes.csv", "clientes", "id_cliente,nome,email,telefone,data_nascimento,created_at"),
    ("enderecos.csv", "enderecos", "id_endereco,id_cliente,logradouro,numero,bairro,cidade,estado,cep,created_at"),
    ("produtos.csv", "produtos", "id_produto,nome,categoria,preco,created_at"),
    ("estoque.csv", "estoque", "id_produto,quantidade,updated_at"),
    ("vendas.csv", "vendas", "id_venda,id_cliente,valor_total,data_venda,status_pagamento"),
    ("itens_venda.csv", "itens_venda", "id_item,id_venda,id_produto,quantidade,valor_unitario"),
    ("pagamentos.csv", "pagamentos", "id_pagamento,id_venda,metodo_pagamento,valor_pago,data_pagamento"),
    ("transportadoras.csv", "transportadoras", "id_transportadora,nome,cnpj,created_at"),
    ("entregas.csv", "entregas", "id_entrega,id_venda,id_transportadora,status_entrega,data_envio,data_entrega"),
    ("fornecedores.csv", "fornecedores", "id_fornecedor,nome,cnpj,telefone,created_at"),
]


def main():
    print("\nStart Conn")
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()
    print("Conn Ok")

    print("Checando tabelas e limpando...")

    for tabela, ddl_sql in DDL_TABELAS.items():
        if tabela_existe(cursor, tabela):
            print(f"Truncando {tabela}...")
            cursor.execute(f"TRUNCATE TABLE {tabela} RESTART IDENTITY CASCADE;")
            conn.commit()
        else:
            print(f"Criando tabela {tabela}...")
            cursor.execute(ddl_sql)
            conn.commit()
            print(f"Tabela {tabela} criada.")

    print("\n**INICIANDO IMPORTAÇÃO MASSIVA**\n")

    for csv_file, tabela, colunas in COPY_MAP:
        print(f"Importando {csv_file} -> {tabela}")

        if not os.path.exists(csv_file):
            print(f"Arquivo não encontrado: {csv_file}")
            continue

        t0 = time.time()

        with open(csv_file, "r", encoding="utf-8") as f:
            next(f)
            cursor.copy_expert(
                f"COPY {tabela} ({colunas}) FROM STDIN CSV",
                f
            )

        conn.commit()

        print(f"Importado {csv_file} em {time.time() - t0:.2f}s")

    cursor.close()
    conn.close()
    print("\n**FINALIZADO IMPORTAÇÃO MASSIVA**\n")


if __name__ == "__main__":
    main()
