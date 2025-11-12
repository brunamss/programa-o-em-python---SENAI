def mercado_ (lista_prod, lista_valores, forma_pag):
    carrinho=[]
    meus_valores=[]
    per = input('deseja pedir? ')
    while per == 'sim ':
        produto = int(input(f'''
                1 {lista_prod[1]} - R$ {lista_valores [1]}
                2 {lista_prod[2]} - R$ {lista_valores [2]}
                3 {lista_prod[3]} - R$ {lista_valores [3]}
                4 {lista_prod[4]} - R$ {lista_valores [4]}
                5 {lista_prod[5]} - R$ {lista_valores [5]}
                   
                '''))
        carrinho.append(lista_prod[produto])
        meus_valores.append(lista_valores[produto])
        print(carrinho)
        print (meus_valores)
        per = input ('deseja continuar? ')

    else:
        print ('obrigado volte sempre! ')

def  pagamento (forma_pag):
    print (forma_pag)
    escolha = int (input( 'escolha a forma de pagamento'))
    print ('sua forma de pagamento é ', forma_pag[escolha])


def despedir (nome):
    return f' obrigado volte sempre {nome}'
