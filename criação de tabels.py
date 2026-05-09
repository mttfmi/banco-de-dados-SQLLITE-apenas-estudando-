import sqlite3 as conector

try:
    # ABertura da conexão com o banco de dados
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    # Execução de um comando: SELECT .... CREATE....
    comando = '''ALTER TABLE Pessoa ADD COLUMN nome TEXT;'''
    
    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados: ', err)

finally:
    # Fechamento da conexão
    if conexao:
        cursor.close()
        conexao.close()