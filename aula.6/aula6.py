# VAMOS PRATICAR COM VARIÁVEIS:

# Multiplique 4 por 6 e divida o resultado 
# por 2. (Concatene com a palavra resultado)

print('Resultado', (4 * 6)/2)


# Calcule a soma de 5 e 7.
# (Concatene com a palavra resultado)

print('Resultado',5 + 7)

# Eleve 3 à potência de 4.
# (Concatene com a palavra resultado)

print('Resultado',3 ** 4)

# Calcule a média de 8, 12 e 15.


media =  (8 + 12 + 15)/3
print('Resultado', media)



# (Concatene com a palavra resultado)


# Subtraia 10 de 2 e multiplique o resultado por 5.
# # (Concatene com a palavra resultado)


print('Resultado',(2 - 10) * 5)



# Divida 27 por 3 e some 5.(Concatene com a palavra resultado)


print('Resultado', 27/3 + 5)


# Exercícios com variáveis
#  / print() / input()(opcional):



# Calcule o módulo ( % ) de 17 por 4.

modulo = 17 % 4
print(modulo)



# Multiplique 9 por 3 e, em seguida, 
# eleve o resultado ao quadrado.

print((9*3)**2)



# Calcule a raiz quadrada de 81.


quadrada = 81  ** 0.5
print(quadrada)


# Adicione 20 a 3 vezes 4.

n1 = 3
n2 = 4
n3 = 20

print((n2*n2)+n3)


# Multiplique 15 por 2 e, em seguida, subtraia 7.

n1 = 15
n2 = 2
n3 = 7 

print(n1*n2-n3)


# Eleve 5 ao cubo.
n1 = 5
n2 = 3
print(n1**n2)
# Calcule a média de 17, 21 e 25.

media  =  (17 + 21 + 25)/3

# Multiplique 11 por 2 e adicione 7.

n1 =  11
n2 =  2
n3 =  7

print(n1 * n2 + n3)



# Subtraia 15 de 3 vezes 8 e divida o resultado por 2.

n1 = 15
n2 = 3
n3 = 8
n4 = 2

print(((n2 * n3) - n1)/n4 )


# Eleve 2 à potência de 10.


n1  = 2
n2  = 10

print(n1 ** n2 )







# nome  =  estrutura dado ou objeto 

# estrutura composta
# pode ser iteravel - percorrivel

# lista vazia
lista_vazia  =  []
print(lista_vazia)

# lista com valores inteiros
#         -3-2-1 # indices negativos
 
#          0 1 2 # indices positivos
# print(lista[0]) # acessei indice

# atribuindo a variáveis
# n1 =  lista[0] 
# n2 =  lista[1]
# print(n1 + n2)
# x = 10
# métodos de listas:

lista   =  [8,1,2,3,1, 500,500]
lista_t = ['z','a','b']

# append  -  adicionar 1 valor no final

lista.append(100)
# print(lista)

# insert - add no indice que vc quiser 
lista.insert(0,250)
# print(lista)

# count -  conta a quantidade do dado
# print(lista.count(8))

# extend -  add varios dados de um vez no final
lista.extend([10,2,3,6,5,410])
# print(lista)

# +=() -  add varios dados
lista +=(10,3,6,5,10,150,'texto')
print(lista)

# adicionando manualmente -  substituição
lista[0] = 500
print(lista)

# removendo dados da lista através do valor

lista.remove(500)
print(lista)

# del  -  deleta de dentro para fora 

del lista[0]
print(lista)

# pop -  com indice ou sem indice

lista.pop()
print(lista)

lista.pop(4)
print(lista)

# sort -  ordenar a lista

lista.sort()
print(lista)

lista.sort(reverse = True)
print(lista)

#copy -  copia lista 

x  =  lista.copy()
print(x)

# print(dir(lista))

# index -  verifica a posição do valor

indice = lista.index(410)
print(indice)

# split -  transfroma os caracteres numa lista
x  = 'texto'
print(x.split())

# clear -  limpar dados da lista

lista.clear()
print(lista)


# funções das listas:
# nome_função(lista)
lista  =  [8,1,2,3,]
lista_t = ['z','a','b']
print(lista)
# len()  -  tamanho 
print(len(lista))
# sum() - somar lista numerica
print(sum(lista))
# max() - maio numero da lista
print(max(lista))
# min() - menor numero da lista
print(min(lista)) 
# sorted() - ordenar númerica
print(sorted(lista_t))




# range() com o list()
lista_0_10 = list(range(11))
print(lista_0_10)
lista_1_10 = list(range(1,11))
print(lista_1_10)
lista_1_10_2 = list(range(1,11,2))
print(lista_1_10_2)


#ATIVIDADE


# Exercício 0: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
lista_2_20_2 = list(range(2,22,2))
print (lista_2_20_2)


# **Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
numeros = list(range(1,11))
print (numeros)



# **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
print(numeros[2])

# **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
numeros.append(9)
print(numeros)

# **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
numeros.remove(5)
print(numeros)

# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.
carros = ['Porsche', 'BMW', 'Audi']
print (carros, numeros)
