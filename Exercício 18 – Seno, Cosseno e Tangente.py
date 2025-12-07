from math import radians, sin, tan, cos
angulo = float(input('Digite o ângulo que você deseja: '))
angulo_radians = radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {sin(angulo_radians):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(angulo_radians):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(angulo_radians):.2f}')