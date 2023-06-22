import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raphael#24',
    database='bdpython1'
)

cursor = conexao.cursor()

id_Vendas = input("Digite o ID da venda que gostaria de excluir: ")
sql = f'DELETE FROM Vendas WHERE id_Vendas = {id_Vendas}'
cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print("O registro foi excluído!")