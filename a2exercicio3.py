numero3 = float(input("Digite um número para comparar com uma palavra: "))
palavra1 = input("Digite uma palavra para comparar com o número: ")

print("\n--- Resultados das Comparações ---")

if palavra1 == str(numero3):
    print(f'"{palavra1}" é igual a "{numero3}".')
elif palavra1 != str(numero3):
    print(f'"{palavra1}" é diferente de "{numero3}".')


