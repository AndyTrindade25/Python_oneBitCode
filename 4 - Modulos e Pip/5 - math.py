import math

# 1 - Acessando o número Pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessando o número de Euler
print(math.e)
print(f"{math.e:.2f}")
 
# 3 - Arredondando números para cima e baixo
num1 = 10.1
print(math.ceil(num1))
print(math.floor(num1))

# 4 - Fatorial de um número
num2 = int(input("Digite um número para o fatorial \n"))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(5,5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC
mdc = math.gcd(25, 100) # 25 / 100 = 1 / 4
print(mdc)