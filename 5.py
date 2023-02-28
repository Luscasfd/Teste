# Define a string a ser invertida
string_original = "Hello World!"

# Inicializa a string invertida vazia
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original)-1, -1, -1):
    # Adiciona cada caractere na string invertida
    string_invertida += string_original[i]

# Imprime a string original e a invertida
print("String original:", string_original)
print("String invertida:", string_invertida)