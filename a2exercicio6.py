palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")

print("\n--- Comparação em Ordem Alfabética ---")

if palavra1 <= palavra2 and palavra1 <= palavra3:
    if palavra2 <= palavra3:
        print(palavra1, palavra2, palavra3)
    else:
        print(palavra1, palavra3, palavra2)
elif palavra2 <= palavra1 and palavra2 <= palavra3:
    if palavra1 <= palavra3:
        print(palavra2, palavra1, palavra3)
    else:
        print(palavra2, palavra3, palavra1)
else:
    if palavra1 <= palavra2:
        print(palavra3, palavra1, palavra2)
    else:
        print(palavra3, palavra2, palavra1)