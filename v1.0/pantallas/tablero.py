import sys
import pygame
import random

##############################################################################
posicion_jugador = [0, 0]

estado_tablero   = []
for i in range(10):
    filas = []
    for j in range(10):
        filas.append(False)
    estado_tablero.append(filas)
    
estado_tablero[5][5] = True
##############################################################################

def marcar_cuadrado(estado_tablero, posicion):
    x, y=posicion
    estado_tablero[x][y]=not estado_tablero[x][y]
    return estado_tablero

def coordenadas(posicion):
    x, y = posicion
    return x*50, y*50

def tablero(pantalla, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "w" and posicion_jugador[1]>0: # ARRIBA
                    posicion_jugador[1] -= 1
                if tecla_presionada == "s" and posicion_jugador[1]<9: # ABAJO
                    posicion_jugador[1] += 1
                if tecla_presionada == "a" and posicion_jugador[0]>0: # IZQUIERDA
                    posicion_jugador[0] -= 1
                if tecla_presionada == "d" and posicion_jugador[0]<9: # DERECHA
                    posicion_jugador[0] += 1
                marcar_cuadrado(estado_tablero, posicion_jugador)
         
        # DIBUJO
        for i in range(10):
            for j in range(10):
                if estado_tablero[i][j]:
                    pygame.draw.rect(pantalla, (141, 0, 46), pygame.Rect(*coordenadas([i, j]), 50, 50))
                else:
                    pygame.draw.rect(pantalla, (155, 225, 24), pygame.Rect(*coordenadas([i, j]), 50, 50))
                    
        pygame.draw.rect(pantalla, (0, 0, 255), pygame.Rect(*coordenadas(posicion_jugador), 50, 50))
        
        #ACTUALIZACION
        pygame.display.flip()
        clock.tick(60)
    
def generarObstaculos():
    
    return obstaculos

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    try:
        tablero(pantalla, clock)
    finally:
        pygame.quit()
