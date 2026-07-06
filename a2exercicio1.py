numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\n--- Resultados das Comparações ---")

if numero1 > numero2:
    print("O primeiro número é maior que o segundo.")
elif numero1 < numero2:
    print("O primeiro número é menor que o segundo.")
else:
    print("Os números são iguais.")

if numero1 >= numero2:
    print("O primeiro número é maior ou igual ao segundo.")
else:
    print("O primeiro número é menor ou igual que o segundo.")
    
if numero1 != numero2:
    print("Os números são diferentes.")
