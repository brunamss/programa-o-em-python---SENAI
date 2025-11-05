#loop usando while

# import random


# per = input('Dseseja jogar? sim ou não')


# while per == 'sim':
#     print('DIVINHE O NÚMERO: 🔢❓ ')
#     numero = random.randrange(1,20000)
#     escolha1 =  int(input('ecolha um número de 1 à 2000 --> '))


#     if numero == escolha1:
#         print('Você ganhou o jogo!🫵 😁 ')
#         print('O numero aleatrorio é ', numero)
#         break
#     else:
#         print('Errou feio! ☠️🧐')    
#         print('O numero aleatrorio é ', numero)
#         per = input('Deseja continuar? sim ou não')
        
# else:
#     print('Até logo ')        



#atividades

# contador = 0

# while contador  <=1000:
#     print (contador)
#     contador += 1


# c = 1
# lista= []

# while c <=10:
#      nome = input('nome:')
#      lista.append(nome)
#      print(lista)
#      c += 1



## ***ATIVIDADE 2***

senha = 123


for chances in range (3):
    senha_prof = int(input('digite senha:'))

    if senha_prof == senha:
        
        n1 = int(input('digite nota:'))
        n2 = int (input('digite nota:'))
        n3 = int (input('digite nota:'))
        media = (n1 + n1 +n3)/3
        print (media)
        break
    else: 
         print('senha incorreta')
else:
    print('conta bloqueada')

input('digite enter para sair')    



