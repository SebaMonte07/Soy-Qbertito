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
    
estado_tablero[0][0] = True
##############################################################################

def marcar_cuadrado(estado_tablero, posicion):
    x, y=posicion
    estado_tablero[x][y]=not estado_tablero[x][y]
    return estado_tablero

def coordenadas(posicion):
    x, y = posicion
    return x*50, y*50

def generar_obstaculos():
    obstaculos = []
    for i in range(3):
        # CUADRADO CENTRAL
        obstaculo_c = [random.randint(2, 8), random.randint(2, 8)]
        while obstaculo_c in obstaculos:
            obstaculo_c = [random.randint(2, 8), random.randint(2, 8)]
        obstaculos.append(obstaculo_c)
        
        # CUADRADOS PERIFERICOS (largo 2 y 3)
        for j in range(i):
            obstaculo_p = obstaculo_c[:]
            obstaculo_p[random.randint(0, 1)] += random.choice([-1, 1])
            while obstaculo_p in obstaculos:
                obstaculo_p = obstaculo_c[:]
                obstaculo_p[random.randint(0, 1)] += random.choice([-1, 1])
            obstaculos.append(obstaculo_p)
        
    return obstaculos

def tablero(pantalla, clock):
    obstaculos= generarObstaculos() 
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
        for i in range(10): #Cambio cuadraditos del tablero
            for j in range(10):
                if estado_tablero[i][j]:
                    pygame.draw.rect(pantalla, (141, 0, 46), pygame.Rect(*coordenadas([i, j]), 50, 50))
                else:
                    pygame.draw.rect(pantalla, (155, 225, 24), pygame.Rect(*coordenadas([i, j]), 50, 50))

        for posicionObstaculo in obstaculos:
            pygame.draw.rect(pantalla, (255, 255, 255), pygame.Rect(*coordenadas(posicionObstaculo), 50, 50)) #Obstaculo
                    
        pygame.draw.rect(pantalla, (0, 0, 255), pygame.Rect(*coordenadas(posicion_jugador), 50, 50)) #jugador

        #ACTUALIZACION
        pygame.display.flip()
        clock.tick(60)
    
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

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    try:
        tablero(pantalla, clock)
    finally:
        pygame.quit()
