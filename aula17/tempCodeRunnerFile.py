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

# Variável URL de conexão -> ordem dos argumentos tem que ser exatamento igual abaixo descrita.
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

try:
    # lendo as tabelas
    df_cliente = pd.read_sql('tb_clientes', engine)
    print(df_cliente)
    df_produto = pd.read_sql('tb_produtos', engine)
    print(df_produto)
    df_item = pd.read_sql('tb_itens', engine)
    print(df_item)
    df_pedido = pd.read_sql('tb_pedidos', engine)
    print(df_pedido)

except Exception as e:
    print(f'Erro na conexão: {e}')