idade = int(input("Digite sua idade: "))
tem_convite = input("Você tem convite? (s/n): ").strip().lower()

if (idade > 18 and idade <= 25) or (idade > 25 and tem_convite == 's'):
    print("Você pode entrar na festa.")
else:
    print("Você não pode entrar na festa.")
    