import sqlite3

def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def inserir_pessoas(conexao):
    cursor = conexao.cursor()

    novas_pessoas = [
       ('Lucas', '12345678900', '1990-01-01', 0),
       ('Maria', '98765432100', '1995-05-05', 1),
       ('Moises', '55555555555', '1980-10-10', 6),
       ('Fernando', '99999999999', '1975-12-12', 1)
    ]

    cursor.executemany(
        'INSERT INTO Pessoa (nome, cpf, nascimento, oculos) VALUES (?, ?, ?, ?)',
        novas_pessoas
    )
    
    conexao.commit()
    cursor.close()

def inserir_clientes(conexao):
    cursor = conexao.cursor()

    novos_clientes = [
        ('Fernando', 'fernando@example.com'),
        ('Maria', 'maria@example.com'),
        ('Joao', 'joao@example.com')
    ]

    cursor.executemany(
        'INSERT INTO Clientes (nome, email) VALUES (?, ?)',
        novos_clientes
    )

    conexao.commit()
    cursor.close()



if __name__ == '__main__':
    conexao = conectar_banco('meu_banco.db')
    inserir_pessoas(conexao)
    inserir_clientes(conexao)
    conexao.close()
