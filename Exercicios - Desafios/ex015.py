quantidadeDeDias = float(input("Quantos dias você permaneceu com o veiculo?: "))
quantidadeDeKm = float(input("Quantos KM você percorreu com o veiculo?: "))

valorDias = 60 * quantidadeDeDias
valorKM = 0.15 * quantidadeDeKm

totalPagamento = valorDias + valorKM

print(
    "O valor total a ser pago pelo aluguel do veiculo por {} dias e {} KM é de R${:.2f}".format(
        quantidadeDeKm, quantidadeDeDias, totalPagamento
    )
)
