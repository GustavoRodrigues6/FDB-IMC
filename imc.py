from users import cursor

def calcular_imc(username):
    """
    This function calculates the IMT for a user based on their username.
    It retrieves the user's data (age, height, weight) from the database,
    and calculates the IMC using the formula: IMT = weight (kg) / height (m)^2.

    :param username: The name of the user (str).
    :return: The calculated IMC (float) or a message if the user is not found.
    """
    # Consulta a base de dados para obter os dados do utilizador
    cursor.execute('SELECT height, weight FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()

    if user_data:
        # Convertendo a altura (em cm) e peso (em kg) para tipos numéricos adequados
        height = float(user_data[0]) / 100  # Converte altura de cm para metros
        weight = float(user_data[1])  # Peso em kg

        # Calcula o IMC
        imc = weight / (height ** 2)

        print(f"O IMC de {username} é: {imc:.2f}")
    else:
        print(f"Error: Utilizador '{username}' não encontrado!")