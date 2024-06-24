import sqlite3

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
#cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')
#conexao.commit()

cursor.execute('INSERT INTO pessoas VALUES ("Maria", "22", "maria@gmail.com")')
conexao.commit()
