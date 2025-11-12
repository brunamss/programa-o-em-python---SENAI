import statistics as st

def estatistica (lista_notas):
    
    moda1 = st.mode(lista_notas)
    print( 'A moda é', moda1)

    media = st.mean (lista_notas)
    print('A media é', media)

    mediana = st.median(lista_notas)
    print ('a mediana é', mediana)

    maior_nota = max (lista_notas)
    print ('maior nota é', maior_nota)

    menor_nota = min (lista_notas)
    print ('menor nota é', menor_nota)
