

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

numero = int(input('digite um numero: '))

if numero > 0:
   print ('positivo')
elif numero < 0:
   print ('negativo')
else:
   print ('nulo')   

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade= int(input('digite sua idade:'))

if idade >=16: 
  print ('pode votar')
else:
   print ('não pode votar')  


# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

numero = int(input('digite um numero: '))

if numero %2==0:
  print ('é um numero par!')
else:
   print('é um numero impar!')
   

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1== n2 == n3 == n1:
   print ('é um triangulo equilatero')
elif n1 != n2 != n3 != n1:
   print ('é um triangulo escaleno')
else:
   print ('é um triangulo isosceles')   
   
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

numero = int(input('digite um numero:'))

if numero %5 == 0:
   print('este numero é mutiplo por 5')
elif numero %7 ==0:
   print ('este numero é mutiplo de 7')
else:
   print ('não e mutiplo por nenhum')


# 6*

# Verifique se um número é positivo e maior que 10

numero = int(input('digite um numero: '))

if numero >0 and numero >10:
   print ('este numero é positivo e maior que 10')
else:
    print ('este numero não e positivo é nem maior que 10 ')   

# 7*

# Verifique se um número é divisível por 3 ou 5.

numemro = int(input('digite um numero: '))

if numero %3 == 0:
   print('este numero é divisivel por 3')
elif  numero %5 ==0:
   print('este numero é divisivel por 5')
else:
   ('este numero não é divisivel')   