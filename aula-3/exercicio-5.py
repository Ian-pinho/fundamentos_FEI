ano=int(input("Digite o ano atual: "))
nasc=int(input("Digite o seu ano de nascimento: "))
idade=ano-nasc
if idade >= 18:
    print("Você já pode tirar sua CNH!")