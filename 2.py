# Solicita ao usuário o número a ser verificado
numero = int(input("Digite um número: "))

# Inicializa as variáveis para calcular a sequência de Fibonacci
a = 0
b = 1
fibonacci = []

# Calcula a sequência de Fibonacci até encontrar um número maior que o número informado pelo usuário
while b <= numero:
    fibonacci.append(b)
    a, b = b, a + b

# Verifica se o número informado pertence à sequência de Fibonacci
if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")