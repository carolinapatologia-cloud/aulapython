palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print("\n--- Comparação Lexicográfica ---")

if palavra1 == palavra2:
    print(f'As palavras "{palavra1}" e "{palavra2}" são iguais.')
elif palavra1 < palavra2:
    print(f'A primeira palavra "{palavra1}" vem antes de "{palavra2}" na ordem lexicográfica.')
else:
    print(f'A primeira palavra "{palavra1}" vem depois de "{palavra2}" na ordem lexicográfica.')
