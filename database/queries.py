host_name = 'localhost'
user_name = 'root'
user_password = 'root'

user_table = """
CREATE TABLE IF NOT EXISTS user (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  balance FLOAT,
  revenue FLOAT
  );
 """
account_table = """
CREATE TABLE IF NOT EXISTS account (
  account_id INTEGER PRIMARY KEY AUTOINCREMENT,
  bank_name VARCHAR(40) NOT NULL,
  type VARCHAR(40) NOT NULL,
  account_user INT,
  FOREIGN KEY(account_user) REFERENCES user(user_id)
  );
"""
invoice_table = """
CREATE TABLE IF NOT EXISTS invoice (
  invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
  details VARCHAR(40) NOT NULL,
  invoice_user INT,
  FOREIGN KEY(invoice_user) REFERENCES user(user_id)
  );
"""
itens_table = """
CREATE TABLE IF NOT EXISTS itens (
  item_id INTEGER PRIMARY KEY AUTOINCREMENT,
  data TEXT,
  name VARCHAR(40) NOT NULL,
  value FLOAT,
  item_invoice INT,
  FOREIGN KEY(item_invoice) REFERENCES invoice(invoice_id)
  );
"""
# datetime('now') para o campo data

def insert_user(first_name, last_name, balance, revenue):
    query = f"""
    INSERT INTO user(first_name, last_name, balance, revenue)
      values('{first_name}','{last_name}',{balance},{revenue});
    """
    return query

def insert_account(bank_name, type_account, user_id):
    query = f"""
    INSERT INTO account(bank_name, type, account_user)
      values('{bank_name}','{type_account}',{user_id});
    """
    return query

def insert_invoice(details, user_id):
    query = f"""
    INSERT INTO invoice(details, invoice_user)
      values('{details}',{user_id});
    """
    return query

def insert_itens(data, name, value, invoice_id):
    query = f"""
    INSERT INTO itens(data, name, value, item_invoice)
      values('{data}','{name}',{value},{invoice_id});
    """
    return query

def select_one_user(id):
  query = f"""
  SELECT * FROM user WHERE user_id='{id}';
  """
  return query

def change_balance(id, value):
  query = f"""
    UPDATE user
    SET balance = {value}
    WHERE user_id='{id}';
  """
  return query

def select_accounts_user(id):
  query = f"""
  SELECT    *
  FROM      account
  WHERE     account_user={id};
  """
  return query

select_user = """
Select * from user;
"""

select_last_user = """
SELECT    *
FROM      user
ORDER BY  user_id DESC
LIMIT     1;
"""

select_last_accout = """
SELECT    *
FROM      account
ORDER BY  account_id DESC
LIMIT     1;
"""