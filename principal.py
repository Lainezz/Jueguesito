import pygame
import jugador

#Inicializar los modulos de pygame
pygame.init()

#Mostramos la pantalla ppal (El Jframe)
screen = pygame.display.set_mode((800,600))

#Cargamos el icono para nuestra pantalla ppal
iconoPpal = pygame.image.load("media/ufo.png")
pygame.display.set_icon(iconoPpal)
#Cambiamos el titulo a nuestra pantalla
pygame.display.set_caption("Mi primerico marsianito")

estaCorriendo = True
while estaCorriendo:
    
    screen.fill((0,0,0))
    
    #El event.get() te devuelve la lista de los eventos que están sucendiendo en ese momento
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            estaCorriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador.posX += 5
            elif evento.key == pygame.K_LEFT:
                jugador.posX -= 5

    #Dibujamos el iconoJugador sobre screen
    screen.blit(jugador.iconoJugador, (jugador.posX, jugador.posY))
    
    pygame.display.update()