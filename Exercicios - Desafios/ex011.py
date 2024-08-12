altura = int(input("Qual a altura da sua parede?"))
largura = int(input("Qual a largura da sua parede?"))
tinta = int(input("Quantos litros de tinta tem a sua lata?"))
rendimentoDaTinta = int(
    input("Qual o rendimento da sua lata de tinta por m^2 por litro?")
)
quantidadeDeDemoes = int(input("Quantas demoes de tinta você pretende realizar?\n"))

area = altura * largura
pintura = area / (rendimentoDaTinta / tinta)
demao = pintura * quantidadeDeDemoes


print(
    "A altura dessa parede é de {} metros e a lagura de {} metros. Totalizando uma area de {} m^2".format(
        altura, largura, area
    )
)
print(
    "Para você pintar sua parede inteira você precisara de {} litros de tinta\n".format(
        pintura
    )
)

if demao == 0:
    demao = False
elif demao == 1:
    print(
        "Para realizar mais {} demão de pintura, você precisa de {} litros\n".format(
            quantidadeDeDemoes, demao
        )
    )
else:
    print(
        "Para realizar {} demoes de pintura, você precisa de {} litros\n".format(
            quantidadeDeDemoes, demao
        )
    )
