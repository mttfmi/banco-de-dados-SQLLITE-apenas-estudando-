import sqlite3 as conector
from modelo import Pessoa   # sua classe Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db", detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

# Definição do comando SQL
comando = '''SELECT * FROM Pessoa WHERE oculos=:usa_oculos;'''

# Aqui usamos 1 para "usa óculos" e 0 para "não usa"
cursor.execute(comando, {"usa_oculos": 1})

# Recuperação dos registros
registros = cursor.fetchall()
for registro in registros:
    # registro é uma tupla (nome, cpf, nascimento, oculos)
    pessoa = Pessoa(*registro)
    print("cpf:", type(pessoa.cpf), pessoa.cpf)
    print("nome:", type(pessoa.nome), pessoa.nome)
    print("nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
    print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)

# Fechamento das conexões
cursor.close()
conexao.close()