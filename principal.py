import pygame
import math
import jugador
import enemy
import bullet

def check_colision(x1,x2,y1,y2) -> bool:
    distancia = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))

    if distancia < 27:
        return True
    else:
        return False

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
        if evento.type == pygame.QUIT:
            estaCorriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador.cambiarPosicion = jugador.speed
            elif evento.key == pygame.K_LEFT:
                jugador.cambiarPosicion = -jugador.speed
            elif evento.key == pygame.K_SPACE and bullet.preparada:
                    bullet.posX = jugador.posX
                    bullet.preparada = False
        elif evento.type == pygame.KEYUP and (evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT):
            jugador.cambiarPosicion = 0

    #Actualizamos la posicion del jugador
    jugador.posX += jugador.cambiarPosicion
    if jugador.posX <= 0:
        jugador.posX = 0
    elif jugador.posX >= 736:
        jugador.posX = 736

    ##gg
    
    #Actualizamos la posicion del enemigo
    enemy.posX += enemy.cambiarPosicion
    if enemy.posX <= 0 or enemy.posX >= 736:
        enemy.cambiarPosicion = -enemy.cambiarPosicion
        enemy.posY += 30

    #Actualizamos la posicion de la bala
    if bullet.preparada == False:
        bullet.posY -= bullet.cambiarPosicion
        #Comprobamos los limites de la pantalla
        if bullet.posY <= 0:
            bullet.preparada = True
            bullet.posY = 480

    #Comprobamos las colisiones
    if check_colision(bullet.posX,enemy.posX,bullet.posY,enemy.posY):
        bullet.preparada = True
        bullet.posY = 480

    #Dibujamos el jugador y el enemigo sobre screen
    screen.blit(jugador.iconoJugador, (jugador.posX, jugador.posY))
    screen.blit(enemy.iconoEnemigo, (enemy.posX, enemy.posY))
    if bullet.preparada == False:
        screen.blit(bullet.iconoBala, (bullet.posX+16, bullet.posY))
    
    pygame.display.update()