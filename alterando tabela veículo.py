import sqlite3 as conector

try:
    # ABertura da conexão com o banco de dados
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    # Execução de um comando: SELECT .... CREATE...
    comando1 = '''DROP TABLE IF EXISTS Veiculo;'''
    
    cursor.execute(comando1)

    comando2 = '''CREATE TABLE Veiculo(
                   placa CHARACTER(7) NOT NULL,
                   ano INTEGER NOT NULL,
                   cor TEXT NOT NULL,
                   motor REAL NOT NULL,
                   proprietario INTEGER NOT NULL,
                   Marca INTEGER NOT NULL,
                   PRIMARY KEY (placa),
                   FOREIGN KEY(Marca) REFERENCES Marca(id)
                   );'''
    
    cursor.execute(comando2)
    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados: ', err)

finally:
    # Fechamento da conexão
    if conexao:
        cursor.close()
        conexao.close()