import sqlite3

conn = sqlite3.connect("tabelafornecedores.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS fornecedores(
               id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
               data_do_pedido DATETIME NOT NULL,
               status TEXT NOT NULL,
               total_do_pedido FLOAT NOT NULL,
               
               )""")