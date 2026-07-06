numero = int(input("Digite um número: "))
palavra = input("Digite uma palavra: ")

print("\n--- Resultado ---")

if numero > 10:
    print("O número é maior que 10.")
elif palavra == "Python":
    print("Você digitou Python.")
else:
    print("Nenhuma condição foi satisfeita.")
