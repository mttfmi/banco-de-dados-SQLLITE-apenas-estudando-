import sqlite3 as conector

try:
    # ABertura da conexão com o banco de dados
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    # Execução de um comando: SELECT .... CREATE....
    comando = '''CREATE TABLE Veiculo (
                   placa CHARACTER(7) NOT NULL,
                   ano INTEGER NOT NULL,
                   proprietario INTEGER NOT NULL,
                   marca INTEGER NOT NULL,
                   PRIMARY KEY (placa),
                   FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
                   FOREIGN KEY (marca) REFERENCES Marca(id)
                   );'''
    
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