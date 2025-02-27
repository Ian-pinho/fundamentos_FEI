distancia=float(input("Digite a distância a ser percorrida em km: "))

if distancia < 200:
    print("O preço da passagem é: ", distancia*0.5)
else:
    print("O preço da passagem é: ", 0.50*200 + (distancia-200)*0.45)
