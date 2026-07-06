palavra = input("Digite uma palavra: ")
numero = palavra.isdigit()

print("\n--- Resultado ---")

if numero:
    print("Você digitou um número.")
else:
    print("Você digitou uma palavra.")  