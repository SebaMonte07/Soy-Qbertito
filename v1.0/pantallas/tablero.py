# Integrantes
# Cristian Cardenas Morales - 20.642.231-3
# Felipe Córdova Vera - 20.960.184-2
# Sebastian Cuevas Castro - 21.133.547-5
# Luciano Espinoza Sierra - 21.071.884-2
# Joaquin Flores Rivera - 21.304.741-8


import sys
import pygame
import random

##############################################################################

TAMANO_CUADRADO = 60
PADDING = 5

##############################################################################
def generar_tablero():
    estado_tablero   = [] # Lista de listas que contienen el estado de cada cuadrado del tablero
    for i in range(10):
        filas = []
        for j in range(10):
            filas.append(False) #False: cuadrado desactivado; True: cuadrado activado
        estado_tablero.append(filas)
        
    estado_tablero[0][0] = True # Posición inicial marcada
    
    return estado_tablero

def marcar_cuadrado(estado_tablero, posicion):
    # Activa o desactiva el cuadrado donde el jugador pasa
    x, y=posicion
    estado_tablero[x][y] = not estado_tablero[x][y]
    
    return estado_tablero

def coordenadas(posicion):
    #Devuelve la posición en coordenadas para la pantalla del juego (en px) 
    x, y = posicion
    
    return x*(TAMANO_CUADRADO+PADDING), y*(TAMANO_CUADRADO+PADDING) # Tamaño cuadrado + Padding

def generar_obstaculos():
    # Genera 3 obstaculos de 1, 2 y 3 cuadrados; devuelve una lista que contiene la posicion en el tablero de cada cuadrado
    obstaculos = [] #lista con la posicion de los obstaculos
    for i in range(3): 
        # CUADRADO CENTRAL
        obstaculo_c = [random.randint(2, 8), random.randint(2, 8)] # Posicion aleatoria
        while obstaculo_c in obstaculos: # Validación que ningún cuadrado aparezca encima de otro
            obstaculo_c = [random.randint(2, 8), random.randint(2, 8)]
        obstaculos.append(obstaculo_c)
        
        # CUADRADOS PERIFERICOS (solo para largos 2 y 3)
        for j in range(i):
            obstaculo_p = obstaculo_c[:] # copiamos solo el contenido de la lista
            obstaculo_p[random.randint(0, 1)] += random.choice([-1, 1]) # el cuadrado aparece en una posicion aleatoria adyacente al cuadrado central (prob. 0.25 cada posición)
            while obstaculo_p in obstaculos: # Validación que el cuadrado no aparezca sobre otro
                obstaculo_p = obstaculo_c[:]
                obstaculo_p[random.randint(0, 1)] += random.choice([-1, 1])
            obstaculos.append(obstaculo_p)
        
    return obstaculos

def verifica_posicion(posicion, obstaculos):
    if posicion in obstaculos:
        return False
    
    return True
    
def main(pantalla, clock):
    # [Inicializacion del tablero; crear funcion]
    estado_tablero = generar_tablero()
    obstaculos = generar_obstaculos() # Inicializacion de la lista de obstaculos
    
    while True: #Bucle por cada cuadro (60 fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Boton de salida presionado
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Boton de movimiento presionado
                tecla_presionada = pygame.key.name(event.key)
                posicion_anterior = posicion_jugador[:]
                
                if tecla_presionada == "w" and posicion_jugador[1]>0: # ARRIBA
                    posicion_jugador[1] -= 1
                if tecla_presionada == "s" and posicion_jugador[1]<9: # ABAJO
                    posicion_jugador[1] += 1
                if tecla_presionada == "a" and posicion_jugador[0]>0: # IZQUIERDA
                    posicion_jugador[0] -= 1
                if tecla_presionada == "d" and posicion_jugador[0]<9: # DERECHA
                    posicion_jugador[0] += 1
                
                if verifica_posicion(posicion_jugador, obstaculos) and posicion_jugador != posicion_anterior: 
                    marcar_cuadrado(estado_tablero, posicion_jugador) # Activamos o desactivamos la posicion a la que se movio el jugador
                    
                else:
                    posicion_jugador[:] = posicion_anterior[:]
         
        # DIBUJO
        # Dibujado de cada estado del tablero
        for i in range(10): # Posicion x tablero
            for j in range(10): # Posicion y tablero
                if estado_tablero[i][j]: # Cuadrado activado
                    pygame.draw.rect(pantalla, "#B266FF", pygame.Rect(*coordenadas([i, j]), TAMANO_CUADRADO, TAMANO_CUADRADO))
                else: # Cuadrado desactivado
                    pygame.draw.rect(pantalla, "light blue", pygame.Rect(*coordenadas([i, j]), TAMANO_CUADRADO, TAMANO_CUADRADO))

        for posicionObstaculo in obstaculos:
            pygame.draw.rect(pantalla, "#404040", pygame.Rect(*coordenadas(posicionObstaculo), TAMANO_CUADRADO, TAMANO_CUADRADO)) #Obstaculos
                    
        pygame.draw.rect(pantalla, "orange", pygame.Rect(*coordenadas(posicion_jugador), TAMANO_CUADRADO, TAMANO_CUADRADO)) #jugador

        # ACTUALIZACION PANTALLA
        pygame.display.flip()
        clock.tick(60) # limite 60 fps
    
# TABLERO (PROGRAMA PRINCIPAL)
posicion_jugador = [0, 0] # Posicion del jugador en el tablero
pygame.init()
pantalla = pygame.display.set_mode(((TAMANO_CUADRADO+PADDING)*10, (TAMANO_CUADRADO+PADDING)*10))
clock = pygame.time.Clock()
    
try:
    main(pantalla, clock)
finally:
    pygame.quit()
