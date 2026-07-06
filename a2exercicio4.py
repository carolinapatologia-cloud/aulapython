palavra1=input("Digite a primeira palavra: ")
palavra2=input("Digite a segunda palavra: ")

print("\n--- Resultados das Comparações ---")

if len(palavra1) > len(palavra2):
    print(f'"{palavra1}" tem mais caracteres que "{palavra2}".')
elif len(palavra1) < len(palavra2):
    print(f'"{palavra1}" tem menos caracteres que "{palavra2}".')
else:
    print(f'"{palavra1}" tem a mesma quantidade de caracteres que "{palavra2}".')
 