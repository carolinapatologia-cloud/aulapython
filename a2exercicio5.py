palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print("\n--- Comparação em Ordem Alfabética ---")

if palavra1 == palavra2:
    print(f'As palavras "{palavra1}" e "{palavra2}" são iguais.')
elif palavra1 < palavra2:
    print(f'A palavra "{palavra1}" vem antes de "{palavra2}" na ordem alfabética.')
else:
    print(f'A palavra "{palavra2}" vem antes de "{palavra1}" na ordem alfabética.')