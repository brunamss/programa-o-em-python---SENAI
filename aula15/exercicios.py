import pygame

pygame.init()

tela = pygame.display.set_mode((300,200))
pygame.display.set_caption('jogo')
run = True

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    tela.fill('yellow')     
    pygame.draw.rect(tela,'purple',(150,100,30,30))
    pygame.draw.circle(tela, ('pink'), (250,200), 50)
    pygame.draw.ellipse(tela, ('blue'), (10,20,25,55))
    




    pygame.display.flip()

    

pygame.quit()

