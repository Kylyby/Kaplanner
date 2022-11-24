import sqlite3

arquivo_db = "planner.db"


def conectar_db():
    conexao = None
    try:
        conexao = sqlite3.connect(arquivo_db)
    except sqlite3.Error as error:
        print(f"Erro ao conectar ao banco de dados:\n{error}")
    return conexao


def desconectar_db(conexao):
    if conexao:
        conexao.close()


def buscar_dados(conexo, busca):
    busca_q = None
    #try:
    cursor = conexo.cursor()
    cursor.execute(busca)
    busca_q = cursor.fetchall()
    return busca_q
    '''except sqlite3.Error as error:
        print(error)
    finally:
        return busca_q'''

def manipular_dados(conexao, comando):
    try:
        cursor=conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
    except sqlite3.Error as error:
        print(f'erro: {error}')



