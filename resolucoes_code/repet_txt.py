# Vamos solicitar como entrada um texto e um número e repetir o texto o número de vezes que a pessoa informou

# Solicitar o texto e o número ao usuário
texto = input("Digite um texto: ")
quantidade = int(input("Digite um número: "))

# Repetir o texto o número de vezes informado
resultado = (texto + " ") * quantidade

# Exibir o resultado
print(f"\nTexto repetido:\n{resultado}")