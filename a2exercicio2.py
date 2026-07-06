palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print("\n--- Resultados das Comparações ---")

if palavra1 == palavra2:
    print(f'"{palavra1}" é igual a "{palavra2}".')
elif palavra1 > palavra2:
    print(f'"{palavra1}" é maior do que "{palavra2}".')
elif palavra1 < palavra2:
    print(f'"{palavra1}" é menor do que "{palavra2}".')


if palavra1 != palavra2:
    print(f'"{palavra1}" é diferente de "{palavra2}".')