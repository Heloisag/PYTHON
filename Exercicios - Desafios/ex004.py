a = input("Digite algo: ")

# Verificações - metódos
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um numero? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("É maísculo? ", a.isupper())
print("É minúscilo?", a.islower())
print("É capitalicada? ", a.istitle())

# se eu fizer a função usando TYPE em tudo, não vai funcionar as demais verificações, pois o comando TYPE é para verificar o tipo do valor digitado, ou seja anula as demais verificações.
