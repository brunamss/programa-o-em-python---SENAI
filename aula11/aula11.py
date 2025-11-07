# def display():
#     try:
#         # n  =  1/0
#         n  = 10
#         l = []
#         print(l[10])
#         # x  = int(input('='))
#         # print(n + x)
#         # print(a)
#     except NameError as erro:
#         print(erro)   
#     except ZeroDivisionError as erro:
#         print(erro)   
#     except ValueError as erro:
#         print(erro)  
#     except IndexError as erro:
#         print(erro)            
#     else:
#         print('Ocorreu um erro não identificado')
#     finally:
#         print('fim de carregamento...')        


# display()        


# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     numero = int(input('digite um numero:'))
#     print (numero)
# except:
#     print('não e m numero inteiro')


# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# try:
#     numero1 = int(input('digite um numero:'))
#     numero2 = int(input('digite um numero:'))
#     resultado = numero1 / numero2
#     print(resultado)
# except ZeroDivisionError as error:
#     print (error)

# else:
#     print ('sem erros')

# finally:
#     print('finalizado')    

# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
 
# try:
#     lista = [1,2,3,4,89,10]
#     indice = int(input('digite numero:'))
#     print (lista[indice])

# except IndexError as error:
#     print('não existe')

# finally:
#     print('finalizado')    