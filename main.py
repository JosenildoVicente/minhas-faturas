from operator import truediv
from sys import flags
from unicodedata import name
from database.create_database import select_user_name, view_users, create_user, change_balance

def create_new_user_option():
    name = input("Escreva seu nome: ")
    lastname = input("Escreva seu sobrenome: ")
    new_user = create_user(name, lastname)
    print(f"Olá, {new_user[0][1]} seu id é {new_user[0][0]}")

def add_balance(id,balance,value):
    val = float(balance) + float(value)
    change_balance(id,val)
    print('Valor adicionado!')

def sub_balance(id,balance,value):
    val = float(balance) + float(value)
    if val>=0:
        change_balance(id,val)
        print('Valor subtraído!')
    else:
        print("Saldo insuficiente para subtrair!")

def login():
    my_id = input("Escreva seu id: ")
    my_user = select_user_name(my_id)
    my_user_name = my_user[0][1]
    my_user_lastname = my_user[0][2]
    my_user_balance = my_user[0][3]
    my_user_revenue = my_user[0][4]
    print(f"Olá, {my_user_name} seu saldo é {my_user_balance} e receita de {my_user_revenue}")
    while True:
        print('Escolha a opção de acordo com a sua necessidade:\n           01 - Adicionar ao saldo\n           02 - Remover do saldo\n           99 - Deslogar')
        opt = input("Escolha: ")
        if opt == '01':
            vl = input('Quanto você quer adicionar: ')
            add_balance(my_id,my_user_balance,vl)
        elif opt == '02':
            vl = input('Quanto você quer tirar: ')
            sub_balance(my_id,my_user_balance,vl)
        elif opt == '99':
            print("Deslogando...")
            break
        else:
            print('Opção inválida')




if __name__ == "__main__":
    print("Olá, bem vindo(a) ao sistema de gerenciamento de contas...")
    while True:
        print('Escolha de acordo com a sua necessidade:\n           01 - Fazer login\n           02 - Consultar usuários\n           03 - Cadastrar usuário novo\n           99 - Sair')
        opt = input("Escolha: ")
        if opt == '01':
           login()
        elif opt == '02':
            view_users()
        elif opt == '03':
            create_new_user_option()
        elif opt == '99':
            print("\n\n\n             Tchau!!!\n\n\n")
            break
        else:
            print('Opção inválida')


    