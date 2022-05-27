import pygame

#Cargo la imagen del jugador
iconoBala = pygame.image.load("media/bullet.png")

#La posicion inicial de la bala
posX = 370
posY = 480

#Variable para la velocidad de la bala
speed = 0.3
cambiarPosicion = speed

#Estado de la bala
preparada = True

