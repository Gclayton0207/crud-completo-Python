import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `bridgehub`;")

cursor.execute("CREATE DATABASE `bridgehub`;")

cursor.execute("USE `bridgehub`;")

# criando tabelas
TABLES = {}
TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `email` varchar(40) NOT NULL,
      `telefone` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, email, telefone) VALUES (%s, %s, %s)'
usuarios = [
      ("Giovanni Clayton", "giovanni.gcda@gmail.com", "(11)98527-9146"),
      ("Juliana Melo", "juliana.melo@gmail.com", "(11)98660-0268"),
      ("Bartolomeu", "barto.gmail.com", "(11)98527-9146")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from bridgehub.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])


# commitando se não nada tem efeito
conn.commit()
cursor.close()
conn.close()