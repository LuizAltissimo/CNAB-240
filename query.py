import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão com o banco de dados
servidor = ''
database = ''
usuario = ''
senha_database = ''

# String de conexão para o SQLAlchemy
string = f'mssql+pyodbc://{usuario}:{senha_database}@{servidor}/{database}?driver=SQL+Server'

# Criar uma conexão usando SQLAlchemy
conexao = create_engine(string)

# Consulta SQL para a leitura do Pandas
query_segmento_e = ''' '''#insira sua query com os lançamentos

df = pd.read_sql_query(query_segmento_e, conexao)

query_header_lote = ''' ''' #insira sua query com as informações do banco de dados

dataf = pd.read_sql_query(query_header_lote, conexao)