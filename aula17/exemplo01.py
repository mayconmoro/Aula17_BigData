# Etapas do processo
# Criação do ambiente virtual
# Importação das bibliotecas necessárias
# Verificar arquivos de backup (requirement se houver) para agilizar
# pip install python-dotenv

# Bibliotecas
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Limpeza do terminal 
os.system('cls')

# Criação de uma função de conexão com SQL
def conecta_banco():
    # Variáveis de conexão
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # Variável URL de conexão -> ordem dos argumentos tem que ser exatamento igual abaixo descrita.
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{database}'
    )
    return engine

 # Função de carregar as informações
load_dotenv()

engine = conecta_banco()

# Otendo os dados do banco
try:
    # lendo as tabelas
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    # print(df_usuarios)
    df_livros = pd.read_sql('tb_livros', engine)
    # print(df_livros)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)
    # print(df_itens_alugados)
    df_alugados = pd.read_sql('tb_alugados', engine)
    # print(df_alugados)
except Exception as e:
    print(f'Erro na conexão: {e}')

# Relacionando os dataframes
    
    # livros com itens
try:
    df_merge1 = pd.merge(
        df_livros, 
        df_itens_alugados,
        on='id_livro' # on somente quando as colunas/série tiverem mesmo nome entre as tabelas. 
                      # Caso esteja diferente, usar left_on='codigo da serie a esquerda', right_on='codigo da serie a direita'
    )
    #print(df_merge1)

    # resultado anterior com alugados
    df_merge2 = pd.merge(
        df_alugados,
        df_merge1,
        on='id_aluguel'
    )
    #print(df_merge2)

    # resultado anterior com usuarios
    df_dados = pd.merge(
        df_usuarios,
        df_merge2,
        on= 'id_usuario'
    )
    # print(df_dados)

    # Filtros
    filtro = (
        (df_dados['data_devolucao'] >= '2024-11-01') & # AND no SQL | pipe = OU  no SQL
        (df_dados['data_devolucao'] <= '2024-11-30')
    )

    df_novembro = df_dados[filtro]

    # ou

    # df_novembro = df_dados.query(
    #     'data_devolucao >= "2024-11-01" AND data_devolucao <= "2024-11-30"' # aspas no python precisam ser diferentes quando estiverem na mesma sintaxe
    #)

    print('\nRelatório de Livros alugados em Novembro ')
    print(
        df_novembro[
            ['id_usuario',
            'nome',
            'cidade',
            'id_aluguel',
            'data_aluguel',
            'data_devolucao',
            'valor',
            'id_livro',
            'titulo'
            ]
        ]
    )

except Exception as e:
    print(f'Erro de relacionamento {e}')


