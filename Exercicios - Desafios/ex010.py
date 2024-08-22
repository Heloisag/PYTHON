dinheiro = float(input("Qual o valor que você tem aplicado na carteira? "))

# variaveis
dolar = 3.27
valor = dinheiro / dolar

print(
    "Com {:.2f} reais você pode comprar {:,2f} dolares para viajar".format(
        dinheiro, valor
    )
)
