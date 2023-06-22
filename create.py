import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raphael#24',
    database='bdpython1'
)

cursor = conexao.cursor()

nome_produto = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")
sql = f'INSERT INTO Vendas(nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
cursor.execute(sql)
conexao.commit()

print("O produto foi inserido!")