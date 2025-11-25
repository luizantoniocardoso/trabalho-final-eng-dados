import csv
from faker import Faker
import random
from datetime import timedelta
import os

fake = Faker('pt_BR')

output_dir = "./"

def write_csv(file, header, rows):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

print("Gerando dados...")

# 1. Clientes (5000)
clientes = []
for i in range(1, 5001):
    clientes.append([
        i,
        fake.name(),
        fake.unique.email(),
        fake.phone_number(),
        fake.date_of_birth(minimum_age=18, maximum_age=85),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("clientes.csv",
          ["id_cliente","nome","email","telefone","data_nascimento","created_at"],
          clientes)

# 2. Endereços (7000)
enderecos = []
for i in range(1, 7001):
    enderecos.append([
        i,
        random.randint(1, 5000),
        fake.street_name(),
        fake.building_number(),
        fake.bairro(),
        fake.city(),
        fake.estado_sigla(),
        fake.postcode(),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("enderecos.csv",
          ["id_endereco","id_cliente","logradouro","numero","bairro","cidade","estado","cep","created_at"],
          enderecos)

# 3. Produtos (2000)
produtos = []
for i in range(1, 2001):
    produtos.append([
        i,
        fake.word().capitalize(),
        fake.word(),
        round(random.uniform(10, 2000), 2),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("produtos.csv",
          ["id_produto","nome","categoria","preco","created_at"],
          produtos)

# 4. Estoque (2000)
estoque = []
for i in range(1, 2001):
    estoque.append([
        i,
        random.randint(0, 500),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("estoque.csv",
          ["id_produto","quantidade","updated_at"],
          estoque)

# 5. Vendas (140000)
vendas = []
for i in range(1, 140001):
    vendas.append([
        i,
        random.randint(1, 5000),
        round(random.uniform(20, 5000), 2),
        fake.date_time_between(start_date="-3y", end_date="now"),
        random.choice(["Pago","Pendente","Cancelado"])
    ])
write_csv("vendas.csv",
          ["id_venda","id_cliente","valor_total","data_venda","status_pagamento"],
          vendas)

# 6. Itens Venda (270000)
itens_venda = []
for i in range(1, 270001):
    itens_venda.append([
        i,
        random.randint(1, 140000),
        random.randint(1, 2000),
        random.randint(1, 5),
        round(random.uniform(10, 2000), 2)
    ])
write_csv("itens_venda.csv",
          ["id_item","id_venda","id_produto","quantidade","valor_unitario"],
          itens_venda)

# 7. Pagamentos (140000)
pagamentos = []
for i in range(1, 140001):
    pagamentos.append([
        i,
        i,
        random.choice(["PIX","Cartão Crédito","Cartão Débito","Boleto"]),
        round(random.uniform(20, 5000), 2),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("pagamentos.csv",
          ["id_pagamento","id_venda","metodo_pagamento","valor_pago","data_pagamento"],
          pagamentos)

# 8. Transportadoras (50)
transportadoras = []
for i in range(1, 51):
    transportadoras.append([
        i,
        fake.company(),
        fake.cnpj(),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("transportadoras.csv",
          ["id_transportadora","nome","cnpj","created_at"],
          transportadoras)

# 9. Entregas (140000)
entregas = []
for i in range(1, 140001):
    dt_envio = fake.date_time_between(start_date="-3y", end_date="now")
    entregas.append([
        i,
        i,
        random.randint(1, 50),
        random.choice(["Enviado","Em transporte","Entregue","Atrasado"]),
        dt_envio,
        dt_envio + timedelta(days=random.randint(1, 15))
    ])
write_csv("entregas.csv",
          ["id_entrega","id_venda","id_transportadora","status_entrega","data_envio","data_entrega"],
          entregas)

# 10. Fornecedores (500)
fornecedores = []
for i in range(1, 501):
    fornecedores.append([
        i,
        fake.company(),
        fake.cnpj(),
        fake.phone_number(),
        fake.date_time_between(start_date="-3y", end_date="now")
    ])
write_csv("fornecedores.csv",
          ["id_fornecedor","nome","cnpj","telefone","created_at"],
          fornecedores)

print("CSV gerados com sucesso!")
