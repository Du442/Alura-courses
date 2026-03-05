import sqlite3

conn = sqlite3.connect("tabelafornecedores.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alura_course(
               ID_Cliente INT PRIMARY KEY NOT NULL,
               Nome_Cliente VARCHAR(255) NOT NULL,
               Informações_do_cliente VARCHAR(20) NOT NULL
               );""")

cursor.execute("""
    """)