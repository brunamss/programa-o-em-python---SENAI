# 1️⃣ Charada:
# O que é o que é: quanto mais você tira, maior fica?
# Resposta: Um buraco.

# 2️⃣ Charada:
# O que é o que é: tem dentes, mas não morde?
# Resposta: Um pente.

# 3️⃣ Charada:
# O que é o que é: passa diante do sol e não faz sombra?
# Resposta: O vento.

# 4️⃣ Charada:
# O que é o que é: anda com os pés na cabeça?
# Resposta: O piolho.

# 5️⃣ Charada:
# O que é o que é: vive no mar, é redondo e vive dizendo “Oi”?
# Resposta: O polvo!


import random

perguntas= [
'carregue novamente',
'O que é o que é: quanto mais você tira, maior fica?',
' que é o que é: tem dentes, mas não morde?',
'O que é o que é: passa diante do sol e não faz sombra?',
'O que é o que é: anda com os pés na cabeça?',
'O que é o que é: vive no mar, é redondo e vive dizendo “Oi”?'

]

respostas= ['','1 - um burraco', '2 - um pente', '3 - o vento', '4 - o piolho', '5 - o polvo!']

per_aleatorio = random.choice(perguntas)
indice = perguntas.index(per_aleatorio)

print (f'''
PERGUNTA...
{per_aleatorio}????

''')

resp_user = int(input(f'''
{respostas[1]}
{respostas[2]}
{respostas[3]}
{respostas[4]}
{respostas[5]}
>>>'''))

if indice == resp_user:
    print('acertou em cheio, a resposta é', indice)
else:
    print('errou feio a resposta é', indice)    






# JOGUINHO


import random 


ppt_m =  ['🪨','🧻','✂️']
ppt_usuario =  ['🪨','🧻','✂️']

maquina =  random.choice(ppt_m)
escolha =  int(input('''
0 - 🪨
1 - 🧻
2 - ✂️                                          
'''))

if maquina == ppt_usuario[escolha]:
    print('EMPATE')
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

elif maquina == '🪨'  and ppt_usuario[escolha] =='✂️':
    print('O computador ganhou')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif maquina == '✂️'   and ppt_usuario[escolha] =='🧻':
    print('O computador ganhou')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    
elif maquina == '🧻'   and ppt_usuario[escolha] =='🪨':
    print('O computador ganhou')   
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif ppt_usuario[escolha] == '🪨'   and maquina =='✂️':
    print('Você ganhou!')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)

elif ppt_usuario[escolha] == '✂️'   and maquina =='🧻':
    print('Você ganhou!')  
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

elif ppt_usuario[escolha] == '🧻'   and maquina =='🪨':
    print('Você ganhou!')
    print('Você escolheu', ppt_usuario[escolha])
    print('O computador escolheu:', maquina)    

else:
    print('Digite algo válido')    