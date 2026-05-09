import sqlite3 as conector

# Conectar ao banco
conexao = conector.connect('./meu_banco.db')
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Criar nova tabela com ordem desejada
cursor.execute('''
CREATE TABLE Pessoa_nova (
    nome TEXT,
    cpf TEXT,
    nascimento DATE,
    oculos INTEGER
);
''')

# Copiar os dados da tabela antiga para a nova
cursor.execute('''
INSERT INTO Pessoa_nova (nome, cpf, nascimento, oculos)
SELECT nome, cpf, nascimento, oculos FROM Pessoa;
''')

# Remover a tabela antiga
cursor.execute('DROP TABLE Pessoa;')

# Renomear a nova tabela para o nome original
cursor.execute('ALTER TABLE Pessoa_nova RENAME TO Pessoa;')

# Confirmar alterações
conexao.commit()

# Conferir os dados já na nova ordem
cursor.execute('SELECT nome, cpf, nascimento, oculos FROM Pessoa;')
for linha in cursor.fetchall():
    print(linha)

# Fechar cursor e conexão
cursor.close()
conexao.close()