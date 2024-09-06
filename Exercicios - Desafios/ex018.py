import math

angulo_graus = float(input("Digite o valor do ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno de {angulo_graus}°: {seno:.4f}")
print(f"Cosseno de {angulo_graus}°: {cosseno:.4f}")
print(f"Tangente de {angulo_graus}°: {tangente:.4f}")
