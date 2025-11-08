# 1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

# def comparar():
#     n1 =  int(input('Digite um número: '))
#     n2 =  int(input('Digite um número: '))

#     if n1 % 2 == 0 and n2 % 2 == 0:
#         print('Ambos são pares')
#     elif n1 % 2 == 0 or n2 % 2 == 0:
#         print('Um deles é par')
#     else:
#         print('Ambos impares')

# comparar ()

# 2 CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

# def multiplicação():
#     n1 = int(input('digite um numero:'))
#     n2 = int(input('digite um numero:'))
#     n3 = int(input('digite um numero:')) 
#     resultado = n1 * n2 * n3
#     print (resultado)

# multiplicação()



# 3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

# def elevado():
#   n  = 10
#   n2 = int(input('valor elevado: '))
#   print(n**n2)

# elevado()


#  4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

# def verificar_idade():
#     idade =  int(input('idade: '))
#     if idade == 18:
#         print('18  anos')
#     else:
#         print('Não tem 18')

# verificar_idade ()       

# 5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

# def mostrar_ano():
#     ano_atual = 2025
#     ano_nascimento = int(input('Ano nascimento:'))
#     mes =  int(input('digite o numero do mês 1: '))
#     cal  =  2025 - ano_nascimento

#     if mes <=6:
#         print('Ano nascimento', cal)
#     else:

#          print('Ano nascimento', cal - 1)

# mostrar_ano()

# 6 DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

# def verificar():
#     copas = [1958,1962,1970,1994,2002]

#     ano =  int(input('Digite o ano que vc acha que o br granhou: '))
#     if ano in copas:
#         print('ganhou!')
#     else:
#         print('Não ganhou!')

# verificar()

# 7 DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.

# 1 - Função -  cumprimentar o cliente

# 2 - Função - restaurante

# 3 - Sugestão utilize listas  e loops

# def cumprimento():

#     print('Seja bem-vindo!')

# def restaurante():
#     pergunta = input('Deseja pedir?')
#     carrinho = []
#     while pergunta == "sim":
#         cumprimento()
#         lista = ['','salada', 'macarronada', 'sanduiche', 'sorvete']
#         print(lista)
        
#         carrinho.append(lista[int(input('Escolha o id do produto: 1 - Salada, 2 - Macarronada, 3 - Sanduiche, 4 - Sorvete '))])
#         print('Escolheu', carrinho)
#         pergunta = input('Deseja continuar?')
#     else:
#         print('Obrigada volte sempre!')
    

# restaurante()
