string1 = input("Digite a primeira palavra: ")
string2 = input("Digite a segunda palavra: ")

print("\n--- Comparação Lexicográfica ---")

if string1 == string2:
    print(f'As palavras "{string1}" e "{string2}" são iguais.')
elif string1 < string2:
    print(f'A primeira palavra "{string1}" vem antes de "{string2}" na ordem lexicográfica.')
else:
    print(f'A primeira palavra "{string1}" vem depois de "{string2}" na ordem lexicográfica.')
