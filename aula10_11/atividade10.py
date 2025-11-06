# 1 - Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000.

# contador = 0
# while contador <= 1000:
#      print(contador)
#      contador += 1


# 2 -  Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

# c = 1
# lista = []

# while c <= 10:
#     nome = input('Nome:')
#     lista.append(nome)
#     print(lista)
#     c += 1


# Atividade2
# senha = 1234



# for chances in range(3):
#     senha_prof = int(input('Digete sua senha:'))
#     if senha_prof == senha:
#         n1 = int(input('Digite a n1: '))
#         n2 = int(input('Digite a n2: '))
#         n3 = int(input('Digite a n3: '))
#         media = (n1 + n2 + n3)/3
#         print(round(media,2))
#         if media >= 7:
#                 print('Você passou de ano')
#         else:
#                 print('Você repetiu de ano!')
#         break
#     else: 
#         print('Senha incorreta, tente novamente')
# else:
#     print('Senha bloqueada!')          

# input('Digite enter para sair')



# Atividade2 da professora



      
notas={
     'alunos':[],
     'notas_aluno':[]
}


for i in range(3):
        senha  = input('Senha: ')
        if senha  == '1234':
            acesso =  input('Deseja verifica a média de um aluno? ')
            while acesso == 'sim':


                print('Sistema de notas Escolares')
                nome = input('Nome: ')
                n1 = float(input('Nota1: '))
                n2 = float(input('Nota1: '))
                n3 = float(input('Nota1: '))
                notas['alunos'].append(nome)
                notas_aluno = notas['notas_aluno'].extend([n1, n2,n3])
                media = sum( notas['notas_aluno']) /len(notas['notas_aluno'])
                print('A Média do aluno' , nome, 'é', media)
                print(notas)
                acesso =  input('Deseja verificar outro aluno? ')
                
else:
    print('conta bloqueada') 
            


input('Digite enter para sair: ')            
      