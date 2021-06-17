import sys
import pygame

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
                if tecla_presionada == "w": # ARRIBA
                    posicion_jugador[1] -= 1
                if tecla_presionada == "s": # ABAJO
                    posicion_jugador[1] += 1
                if tecla_presionada == "a": # IZQUIERDA
                    posicion_jugador[0] -= 1
                if tecla_presionada == "d": # DERECHA
                    posicion_jugador[0] += 1
         
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
    

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    try:
        tablero(pantalla, clock)
    finally:
        pygame.quit()

    
