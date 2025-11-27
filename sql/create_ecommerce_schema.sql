-- OPCIONAL: criar schema lógico
CREATE SCHEMA IF NOT EXISTS ecommerce;
SET search_path TO ecommerce;

-- ===========================
-- TABELA CLIENTES
-- ===========================
CREATE TABLE clientes (
    cliente_id    SERIAL PRIMARY KEY,
    nome          VARCHAR(100) NOT NULL,
    sobrenome     VARCHAR(100) NOT NULL,
    cpf           VARCHAR(20),
    email         VARCHAR(150),
    data_cadastro DATE NOT NULL
);

-- ===========================
-- TABELA ENDERECOS
-- ===========================
CREATE TABLE enderecos (
    endereco_id   SERIAL PRIMARY KEY,
    cliente_id    INT NOT NULL,
    tipo_endereco VARCHAR(50) NOT NULL,
    rua           VARCHAR(150) NOT NULL,
    numero        VARCHAR(20) NOT NULL,
    cidade        VARCHAR(100) NOT NULL,
    estado        VARCHAR(2) NOT NULL,
    cep           VARCHAR(20) NOT NULL,
    CONSTRAINT fk_enderecos_clientes
        FOREIGN KEY (cliente_id)
        REFERENCES clientes (cliente_id)
);

-- ===========================
-- TABELA PRODUTOS
-- ===========================
CREATE TABLE produtos (
    produto_id   SERIAL PRIMARY KEY,
    nome_produto VARCHAR(150) NOT NULL,
    descricao    TEXT,
    categoria    VARCHAR(100),
    preco_base   NUMERIC(10,2) NOT NULL
);

-- ===========================
-- TABELA FORNECEDORES
-- ===========================
CREATE TABLE fornecedores (
    fornecedor_id   SERIAL PRIMARY KEY,
    nome_fornecedor VARCHAR(150) NOT NULL,
    cnpj            VARCHAR(20),
    telefone        VARCHAR(20)
);

-- ===========================
-- TABELA ESTOQUE
-- ===========================
CREATE TABLE estoque (
    estoque_id             SERIAL PRIMARY KEY,
    produto_id             INT NOT NULL,
    fornecedor_id          INT NOT NULL,
    quantidade_disponivel  INT NOT NULL,
    data_ultima_atualizacao TIMESTAMP NOT NULL,
    CONSTRAINT fk_estoque_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos (produto_id),
    CONSTRAINT fk_estoque_fornecedor
        FOREIGN KEY (fornecedor_id)
        REFERENCES fornecedores (fornecedor_id)
);

-- ===========================
-- TABELA TRANSPORTADORAS
-- ===========================
CREATE TABLE transportadoras (
    transportadora_id   SERIAL PRIMARY KEY,
    nome_transportadora VARCHAR(150) NOT NULL,
    cnpj                VARCHAR(20),
    servico_disponivel  VARCHAR(100)
);

-- ===========================
-- TABELA VENDAS
-- ===========================
CREATE TABLE vendas (
    venda_id            SERIAL PRIMARY KEY,
    cliente_id          INT NOT NULL,
    endereco_entrega_id INT NOT NULL,
    data_venda          TIMESTAMP NOT NULL,
    valor_total         NUMERIC(12,2) NOT NULL,
    status_venda        VARCHAR(50) NOT NULL,
    CONSTRAINT fk_vendas_clientes
        FOREIGN KEY (cliente_id)
        REFERENCES clientes (cliente_id),
    CONSTRAINT fk_vendas_endereco
        FOREIGN KEY (endereco_entrega_id)
        REFERENCES enderecos (endereco_id)
);

-- ===========================
-- TABELA ITENS_VENDA
-- ===========================
CREATE TABLE itens_venda (
    item_venda_id  SERIAL PRIMARY KEY,
    venda_id       INT NOT NULL,
    produto_id     INT NOT NULL,
    quantidade     INT NOT NULL,
    preco_unitario NUMERIC(10,2) NOT NULL,
    subtotal       NUMERIC(12,2) NOT NULL,
    CONSTRAINT fk_itens_venda_venda
        FOREIGN KEY (venda_id)
        REFERENCES vendas (venda_id),
    CONSTRAINT fk_itens_venda_produto
        FOREIGN KEY (produto_id)
        REFERENCES produtos (produto_id)
);

-- ===========================
-- TABELA ENTREGAS
-- ===========================
CREATE TABLE entregas (
    entrega_id            SERIAL PRIMARY KEY,
    venda_id              INT NOT NULL,
    transportadora_id     INT NOT NULL,
    codigo_rastreio       VARCHAR(100),
    data_envio            DATE,
    data_estimada_entrega DATE,
    status_entrega        VARCHAR(50),
    CONSTRAINT fk_entregas_venda
        FOREIGN KEY (venda_id)
        REFERENCES vendas (venda_id),
    CONSTRAINT fk_entregas_transportadora
        FOREIGN KEY (transportadora_id)
        REFERENCES transportadoras (transportadora_id)
);

-- ===========================
-- TABELA PAGAMENTOS
-- ===========================
CREATE TABLE pagamentos (
    pagamento_id     SERIAL PRIMARY KEY,
    venda_id         INT NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL,
    valor_pago       NUMERIC(12,2) NOT NULL,
    status_pagamento VARCHAR(50) NOT NULL,
    data_pagamento   TIMESTAMP NOT NULL,
    CONSTRAINT fk_pagamentos_venda
        FOREIGN KEY (venda_id)
        REFERENCES vendas (venda_id)
);

-- ===========================
-- ÍNDICES BÁSICOS
-- ===========================
CREATE INDEX idx_vendas_cliente       ON vendas (cliente_id);
CREATE INDEX idx_vendas_data          ON vendas (data_venda);
CREATE INDEX idx_itens_venda_venda    ON itens_venda (venda_id);
CREATE INDEX idx_itens_venda_produto  ON itens_venda (produto_id);
CREATE INDEX idx_pagamentos_venda     ON pagamentos (venda_id);
CREATE INDEX idx_entregas_venda       ON entregas (venda_id);
CREATE INDEX idx_estoque_produto      ON estoque (produto_id);
CREATE INDEX idx_enderecos_cliente    ON enderecos (cliente_id);
