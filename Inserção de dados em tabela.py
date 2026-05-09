import sqlite3 as conector

#abertura da conexão com o banco de dados
conexao = conector.connect('./meu_banco.db')
cursor = conexao.cursor()

#execução de um comando: SELECT .... CREATE...
comando = '''UPDATE Pessoa
SET nome = 'joao'
WHERE cpf = 12345678900;'''

cursor.execute(comando)


#Efetivação do comando
conexao.commit()

#fechamento da conexão
cursor.close()
conexao.close()