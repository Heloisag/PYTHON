import math

cateto_oposto = float(input("Digite o valor do seu cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do seu cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f"O valor da hipotenusa neste caso é: {hipotenusa}")