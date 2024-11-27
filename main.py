import users
import imc
from users import *
from imc import *

def main():
    while True:
        print("--------------------------- Menu ---------------------------")
        print("1. Registar Utilizador")
        print("2. Calcular IMC")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            print("--------------------------- Registo ---------------------------")
            username = input("Nome do utilizador: ")
            age = int(input("Idade do utilizador: "))
            height = int(input("Altura do utilizador (em cm): "))
            weight = int(input("Peso do utilizador (em kg): "))
            create_user(username, age, height, weight)
        elif choice == '2':
            print("--------------------------- Calculo ---------------------------")
            username_input = input("Insira o nome do utilizador: ")
            calcular_imc(username_input)
        elif choice == '3':
            print("A Sair...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()