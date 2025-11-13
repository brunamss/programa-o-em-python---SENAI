# 1 - Crie um número aleatório de 5,10
import random
def aleatorio():
    return random.randint(5,10)


    

# 2 - Crie 3 números aleatórios

def aleatorio2():
    return random.randint(0,17), random.randint(0,17), random.randint(0,17)


# 3 - Crie um número aleatório entre 10 a 30 utilize o range()

def aleatorio3():
    return random.randrange(10,30)

# 4 - Contagem regressiva simples
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)

def contagem():
    for numero in range(10,0,-1):
      print(numero)
    else:
        print('fogo!')

# 5 - Soma de números pares

# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

def numero():
    numero = int(input('digite um numero inteiro:' ))
    soma = 0 
    for i in range (2, numero, 2):
        soma = soma + numero
    print (soma)
              

# 6 - Tabuada de multiplicação

# Utilize print() na saída

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.

# (while ou for )

def multiplicação():
    n1 = int(input('digite um numero: '))
    
    for n in range (1,11):
        c = n * n1
        print(n1,'x',n,'=',c)


# 7 -  Números ímpares reversos

# Exiba uma contagem regressiva de números ímpares de 99 a 1.

def contagem1():
    for numero in range(99,0,-2):
      print(numero)
    
