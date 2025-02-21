import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine(f'postgresql://postgres:root@localhost:5432/postgres')

dados_brutos = pd.read_sql("select * from brutos_dit.dados_ficha_a_desafio", con=engine) 
dados_brutos