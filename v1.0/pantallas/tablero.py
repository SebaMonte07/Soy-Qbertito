import sys
import pygame
import random

##############################################################################
posicion_jugador = [0, 0] #Posicion del jugador en el tablero

estado_tablero   = [] # Lista de listas que contienen el estado de cada cuadrado del tablero
for i in range(10):
    filas = []
    for j in range(10):
        filas.append(False) #False: cuadrado desactivado; True: cuadrado activado
    estado_tablero.append(filas)
    
estado_tablero[0][0] = True # Posición inicial marcada
##############################################################################

def marcar_cuadrado(estado_tablero, posicion):
    # Activa o desactiva el cuadrado donde el jugador pasa
    x, y=posicion
    estado_tablero[x][y]=not estado_tablero[x][y]
    
    return estado_tablero

def coordenadas(posicion):
    #Devuelve la posición en coordenadas para la pantalla del juego (en px) 
    x, y = posicion
    
    return x*50, y*50

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

def tablero(pantalla, clock):
    # [Inicializacion del tablero; crear funcion]
    obstaculos = generar_obstaculos() # Inicializacion de la lista de obstaculos
    
    while True: #Bucle por cada cuadro (60 fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Boton de salida presionado
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Boton de movimiento presionado
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "w" and posicion_jugador[1]>0: # ARRIBA
                    posicion_jugador[1] -= 1
                if tecla_presionada == "s" and posicion_jugador[1]<9: # ABAJO
                    posicion_jugador[1] += 1
                if tecla_presionada == "a" and posicion_jugador[0]>0: # IZQUIERDA
                    posicion_jugador[0] -= 1
                if tecla_presionada == "d" and posicion_jugador[0]<9: # DERECHA
                    posicion_jugador[0] += 1
                    
                marcar_cuadrado(estado_tablero, posicion_jugador) # Activamos o desactivamos la posicion a la que se movio el jugador
         
        # DIBUJO
        # Dibujado de cada estado del tablero
        for i in range(10): # Posicion x tablero
            for j in range(10): # Posicion y tablero
                if estado_tablero[i][j]: # Cuadrado activado
                    pygame.draw.rect(pantalla, (141, 0, 46), pygame.Rect(*coordenadas([i, j]), 50, 50))
                else: # Cuadrado desactivado
                    pygame.draw.rect(pantalla, (155, 225, 24), pygame.Rect(*coordenadas([i, j]), 50, 50))

        for posicionObstaculo in obstaculos:
            pygame.draw.rect(pantalla, (255, 255, 255), pygame.Rect(*coordenadas(posicionObstaculo), 50, 50)) #Obstaculos
                    
        pygame.draw.rect(pantalla, (0, 0, 255), pygame.Rect(*coordenadas(posicion_jugador), 50, 50)) #jugador

        # ACTUALIZACION PANTALLA
        pygame.display.flip()
        clock.tick(60) # limite 60 fps
    
def generarObstaculos():
    obstaculos=[]
    for i in range(3):
        if i==0:
            x= random.randint(2, 9)
            y= random.randint(2, 9)
            obstaculos.append([x, y])
        else:
            if i==1:
                obstaculo1= [random.randint(2, 8), random.randint(2, 8)]
                while obstaculo1 in obstaculos:
                    obstaculo1= [random.randint(2, 8), random.randint(2, 8)]
            
                obstaculo2= obstaculo1.copy()
                obstaculo2[random.randint(0, 1)]-=random.choice([-1, 1])
                while obstaculo2 in obstaculos:
                    obstaculo2= obstaculo1.copy()
                    obstaculo2[random.randint(0, 1)]-=random.choice([-1, 1])
            
                obstaculos+=[obstaculo1,obstaculo2]
            else:
                obstaculo1= [random.randint(2, 8), random.randint(2, 8)]
                while obstaculo1 in obstaculos:
                    obstaculo1= [random.randint(2, 8), random.randint(2, 8)]
            
                obstaculo2= obstaculo1.copy()
                obstaculo2[random.randint(0, 1)]-=random.choice([-1, 1])
                while obstaculo2 in obstaculos:
                    obstaculo2= obstaculo1.copy()
                    obstaculo2[random.randint(0, 1)]-=random.choice([-1, 1])
                
                obstaculo3=obstaculo2.copy()
                obstaculo3[random.randint(0, 1)]-=random.choice([-1, 1])
                while obstaculo3==obstaculo1:
                    obstaculo3[random.randint(0, 1)]-=random.choice([-1, 1])
                while obstaculo3 in obstaculos:
                    obstaculo3=obstaculo2.copy()
                    obstaculo3[random.randint(0, 1)]-=random.choice([-1, 1])
                    while obstaculo3==obstaculo1:
                        obstaculo3[random.randint(0, 1)]-=random.choice([-1, 1])
            
                obstaculos+=[obstaculo1,obstaculo2,obstaculo3]
    return obstaculos

if __name__ == "__main__": # Verdadero solo si el programa se ejecuta desde este archivo (tablero.py)
    pygame.init()
    pantalla = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    try:
        tablero(pantalla, clock)
    finally:
        pygame.quit()
