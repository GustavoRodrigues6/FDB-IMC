import users
import imc
from users import *
from imc import *

# Solicita os dados para criar um utilizador
print("--------------------------- Registo ---------------------------")
username = input("Nome do utilizador: ")
age = int(input("Idade do utilizador: "))
height = str(input("Altura do utilizador: "))
weight = str(input("Peso do utilizador: "))

# Chama a função para criar o utilizador com os dados fornecidos
create_user(username, age, height, weight)

# Pergunta o nome do utilizador
username_input = input("Digite o nome do utilizador para calcular o seu IMC: ")

# Chama a função para calcular o IMC com o nome fornecido
calcular_imc(username_input)

