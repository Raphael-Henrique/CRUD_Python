import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raphael#24',
    database='bdpython1'
)

cursor = conexao.cursor()

sql = f'SELECT * FROM vendas'
cursor.execute(sql)
resultados = cursor.fetchall()
print(resultados)

cursor.close()
conexao.close()

for resultado in resultados:
    print(resultado)