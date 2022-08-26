import sqlite3
import queries
from datetime import datetime

def create_db():
  connection = sqlite3.connect('test.db')
  cursor = connection.cursor()
  cursor.execute(queries.user_table)
  cursor.execute(queries.account_table)
  cursor.execute(queries.invoice_table)
  cursor.execute(queries.itens_table)
  connection.commit()
  connection.close()

def populate_db():
  connection = sqlite3.connect('test.db')
  cursor = connection.cursor()
  # cursor.execute(queries.insert_user("Josenildo","Vicente",0.0,0.0))
  # cursor.execute(queries.insert_account("MyBank","Pagamentos",1))
  # cursor.execute(queries.insert_invoice("Primeira fatura de teste",1))
  # cursor.execute(queries.insert_itens("26/08/20202","MeuNegocio", 16.5,1))
  connection.commit()
  connection.close()

def view_tables():
  connection = sqlite3.connect('test.db')
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM user")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  
  cursor.execute("SELECT * FROM account")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  
  cursor.execute("SELECT * FROM invoice")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  
  cursor.execute("SELECT * FROM itens")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  
  connection.close()

