import pygame
import random

#Cargo la imagen del enemigo
iconoEnemigo = pygame.image.load("media/space-ship.png")

#La posicion inicial del enemigo
posX = random.randint(50,700)
posY = random.randint(1,100)

#Variable para la velocidad del enemigo
speed = 0.3
cambiarPosicion = speed