import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raphael#24',
    database='bdpython1'
)

cursor = conexao.cursor()


id_Vendas = input("Digite o ID da venda que gostaria de editar: ")
nome_produto = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")
sql = f'UPDATE vendas SET nome_produto = "{nome_produto}", valor = "{valor}"  WHERE id_Vendas = {id_Vendas}'
cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print("O registro foi atualizado!")