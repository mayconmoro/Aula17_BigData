# Bibliotecas
import os
import pandas as pd
from sqlalchemy import create_engine

# Limpeza do terminal 
os.system('cls')

# Variáveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_vendas'

# Variável URL de conexão
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

try:
    # lendo as tabelas
    df_cliente = pd.read_sql('tb_clientes', engine)
    #print(df_cliente)
    df_produto = pd.read_sql('tb_produtos', engine)
    #print(df_produto)
    df_item = pd.read_sql('tb_itens', engine)
    #print(df_item)
    df_pedido = pd.read_sql('tb_pedidos', engine)
    #print(df_pedido)

except Exception as e:
    print(f'Erro na conexão: {e}')

# Relacionamento entre as tabelas
# Produto + item
try:
    df_merge1 = pd.merge(
        df_produto,
        df_item,
        on='codigo_produto'
        )
    # Resultado Merge1 + pedido
    df_merge2 = pd.merge(
        df_merge1,
        df_pedido,
        on= 'codigo_pedido'
        )
    # Resultado Merge 2 + cliente
    df_vendas = pd.merge(
        df_merge2,
        df_cliente,
        on= 'codigo_cliente'
        )
    
    # Filtro
    filtro = (df_vendas['cidade'] == 'Sao Paulo')

    df_relatorio = df_vendas[filtro]

    print('\nRelatório de Pedidos')
    print(
        df_relatorio[
            ['codigo_cliente',
             'nome',
             'sobrenome',
             'cidade',
             'codigo_pedido',
             'data_pedido',
             'produto',
             'valor'
            ]
        ]

    )
except Exception as e:
    print(f'Erro de relacionamento dos Dataframes {e}')


# ATIVIDADE 01
# O gestor da empresa Comercial Atlas solicitou um relatório contendo os pedidos realizados por clientes da cidade de São Paulo. As informações deverão ser obtidas diretamente do banco de dados, usando o Python para receber os dados das tabelas.
# O relatório deverá apresentar:
    
# •	código do cliente
# •	nome do cliente; 
# •	sobrenome; 
# •	cidade;
# •	código do pedido; 
# •	data do pedido; 
# •	produto comprado; 
# •	valor do pedido. 

