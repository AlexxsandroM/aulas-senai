"""import mysql ConnectionAbortedError
#configurações da conexão  com o banco de dados
config = {
    'user": se_usuario,'
    'password': 'sua senha',
    'host': 'localhost',
    'database': 'nome_do_banco_de_dados'}
#estabelecer  a conexão com o banco de dados
conexão = mysql.conne""""


import mysql.connector

config = {
    'user': 'root',
    'password': 'senai',
    'host': 'localhost',
    'database': 'loja_ii'
}

# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(**config)

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo de consulta SQL
#selecionarDB= "use loja_ii;"
consulta = "SELECT * FROM clientes"
consultaII= "SELECT * FROM produtos"


# Executar a consulta
#cursor.execute(selecionarDB)
cursor.execute(consulta)
cursor.execute(consultaII)
# Recuperar os resultados
resultados = cursor.fetchall()

# Imprimir os resultados
for linha in resultados:
    print(linha,"\n")

# Fechar o cursor e a conexão
cursor.close()
conexao.close()