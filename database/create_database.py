import sqlite3
try:
  import queries 
except ImportError:
  import database.queries as queries
# from datetime import datetime

db_name = 'test.db'

def create_db():
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.user_table)
  cursor.execute(queries.account_table)
  cursor.execute(queries.invoice_table)
  cursor.execute(queries.itens_table)
  connection.commit()
  connection.close()

def populate_db():
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  # cursor.execute(queries.insert_user("Josenildo","Vicente",0.0,0.0))
  # cursor.execute(queries.insert_account("MyBank","Pagamentos",1))
  # cursor.execute(queries.insert_invoice("Primeira fatura de teste",1))
  # cursor.execute(queries.insert_itens("26/08/20202","MeuNegocio", 16.5,1))
  connection.commit()
  connection.close()

def view_tables():
  connection = sqlite3.connect(db_name)
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

def view_users():
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM user")
  rows = cursor.fetchall()
  for row in rows:
    print(row)
  connection.close()

def select_user_name(id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.select_one_user(id))
  rows = cursor.fetchall()
  connection.close()
  return rows

def create_user(user_name, user_lastname):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.insert_user(user_name,user_lastname,0.0,0.0))
  connection.commit()
  cursor.execute(queries.select_last_user)
  rows = cursor.fetchall()
  connection.close()
  return rows

def new_account(bank_name,bank_type,user_id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.insert_account(bank_name,bank_type,user_id))
  connection.commit()
  cursor.execute(queries.select_last_accout)
  rows = cursor.fetchall()
  connection.close()
  print(rows)
  return rows

def new_invoice(details,user_id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.insert_invoice(details,user_id))
  connection.commit()
  connection.close()

def new_item(data,product_name,value,invoice_id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.insert_itens(data,product_name,value,invoice_id))
  connection.commit()
  connection.close()

def change_balance(id,value):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.change_balance(id,value))
  connection.commit()
  connection.close()

def select_user_accounts(user_id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.select_accounts_user(user_id))
  rows = cursor.fetchall()
  connection.close()
  return rows

def delete_user_account(user_id,bank_name,bank_id):
  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()
  cursor.execute(queries.delete_account(user_id,bank_id))
  connection.commit()
  rows = cursor.rowcount
  connection.close()
  return rows