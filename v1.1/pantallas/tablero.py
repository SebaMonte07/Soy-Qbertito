# Integrantes
# Cristian Cardenas Morales - 20.642.231-3
# Felipe Córdova Vera - 20.960.184-2
# Sebastian Cuevas Castro - 21.133.547-5
# Luciano Espinoza Sierra - 21.071.884-2
# Joaquin Flores Rivera - 21.304.741-8


import sys
import pygame
import random

import utiles
from pantallas import menu_pausa


##############################################################################


# Constantes
TAMANO_CUADRADO = 60
PADDING = 5


##############################################################################

# Funciones generales

def generar_tablero():
    
    # Genera un tablero de 10x10
    
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
    estado_tablero[x][y] = not estado_tablero[x][y] # Inversión de booleanos
    
    return estado_tablero



def coordenadas(posicion):
    
    #Devuelve la posición en coordenadas para la pantalla del juego (en px) 
    
    x, y = posicion
    
    return x*(TAMANO_CUADRADO+PADDING), y*(TAMANO_CUADRADO+PADDING)



def generar_obstaculos(estado_tablero):
    
    # Genera 3 obstaculos de 1, 2 y 3 cuadrados; devuelve una lista que contiene la posicion en 
    # el tablero de cada cuadrado
    
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
    
    # Por defecto la posicion de los obstáculos debe estar activada
    for posx, posy in obstaculos:
        estado_tablero[posx][posy] = True
        
    return obstaculos, estado_tablero



def verifica_posicion(posicion, obstaculos):
    
    # Verifica que el jugador no está en un obstáculo
    
    if posicion in obstaculos:
        return False
    
    return True





# Generación & dinámica de enemigos

def generar_enemigos(obstaculos, numero_enemigos=2):
    
    # genera enemigos (2 por defecto) con posicion aleatoria en el tablero
    
    posiciones_prohibidas = obstaculos + [[0, 0], [1, 0], [0, 1], [1, 1]] # posiciones protegidas
    enemigos = []
    
    for i in range(numero_enemigos):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        
        while [x, y] in posiciones_prohibidas: # validacion: el enemigo no esta en un obstaculo o en una posicion protegida
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            
        posiciones_prohibidas.append([x, y]) # protegemos la posicion del enemigo, así no se sobreponen
        enemigos.append([x, y])
    
    return enemigos



def mover_enemigos(enemigos, obstaculos):
    
    # Mueve a los enemigos en el tablero.
    # Para evitar bucles infinitos con enemigos atrapados, itera solo en los 4 movimientos posibles (aleatoriamente)
    # Así, un enemigo bloqueado queda en su misma ubicacion.
    
    posiciones_prohibidas = obstaculos + [[0, 0], [1, 0], [0, 1], [1, 1]]
    #posiciones_prohibidas.append([0, 0]) # posiciones especificas donde no pueden moverse los enemigos
    posibles_movimientos = [(0, -1), (0, 1), (1, -1), (1, 1)] # ( indice: vertical-horizontal , sentido de la direccion)
    
    for i, enemigo in enumerate(enemigos): # iteramos por cada enemigo y su respectiva posicion (i) en la lista
        posicion_anterior = enemigo[:] 
        
        random.shuffle(posibles_movimientos) # barajamos la lista, con tal de mantener un movimiento aleatorio
        
        for indice, movimiento in posibles_movimientos:
            enemigo[indice] += movimiento # realizacion del movimiento
            
            if enemigo[0] < 0 or enemigo[1] < 0 or enemigo[0] > 9 or enemigo[1] > 9: # esta dentro del tablero
                enemigo[:] = posicion_anterior[:]
            
            elif enemigo in posiciones_prohibidas: # no esta en un obstaculo o en la posicion protegida
                enemigo[:] = posicion_anterior[:]
                
            elif enemigo in enemigos[:i]: # no se sobrepone con un enemigo que ya se movio
                enemigo[:] = posicion_anterior[:]
                
            elif enemigo in enemigos[i+1:]: # no se sobrepone con algun otro enemigo, que tal vez este bloqueado
                enemigo[:] = posicion_anterior[:]
                
            else: # posicion disponible, deja de buscar
                break
        
    return enemigos
            

    


# Función principal

def main(pantalla, clock):
    
    # Implementa las mecánicas del juego con todas sus reglas.
    #  - Cada vez que qbertito se mueve, el puntaje disminuye en 100
    #  - Cada vez que un zombie toca a qbertito, pierde una vida y el puntaje disminuye en 1000
    #  - El puntaje minimo es 100
    # Devuelve la próxima pantalla a mostrar
    
    # Inicializacion y creación de fuentes
    
    fuente = pygame.font.SysFont("Papyrus", 42, bold=True)
    
    texto_vidas = fuente.render("Vidas restantes", True, "white")
    texto_puntuacion = fuente.render("Puntuación", True, "white")
    texto_pausa = fuente.render("[P] - Pausa", True, "white")
    
    
    # Inicialización de tablero y posiciones de cada objeto
    
    posicion_jugador = [0, 0] # Posicion inicial jugador
    estado_tablero = generar_tablero()
    obstaculos, estado_tablero = generar_obstaculos(estado_tablero) # Inicializacion de la lista de obstaculos
    enemigos = generar_enemigos(obstaculos)
    
    
    # Inicialización de vida y puntaje
    vidas = 3 
    puntaje = 100000 
    
    
    # Bucle por cada cuadro (60 fps)
    
    while True: 
        
        # Eventos de pygame & dinámicas del juego
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Boton de salida presionado
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN: # Boton de movimiento presionado
                tecla_presionada = pygame.key.name(event.key)
                posicion_anterior = posicion_jugador[:]
                
                # Botones de movimiento
                
                if tecla_presionada == "w" and posicion_jugador[1]>0: # ARRIBA
                    posicion_jugador[1] -= 1
                    
                if tecla_presionada == "s" and posicion_jugador[1]<9: # ABAJO
                    posicion_jugador[1] += 1
                    
                if tecla_presionada == "a" and posicion_jugador[0]>0: # IZQUIERDA
                    posicion_jugador[0] -= 1
                    
                if tecla_presionada == "d" and posicion_jugador[0]<9: # DERECHA
                    posicion_jugador[0] += 1
                    
                    
                # Boton de pausa
                
                if tecla_presionada == "p": 
                    
                    reinicia = menu_pausa.main(pantalla, clock) # llama al menu pausa
                    
                    if reinicia: # verifica si se presiona [R]
                        main(pantalla, clock) # llama nuevamente a la funcion y por tanto, reinicia el juego
                        
                        
                # Si el jugador realiza un movimiento válido
 
                if verifica_posicion(posicion_jugador, obstaculos) and posicion_jugador != posicion_anterior: 
                    
                    puntaje -= 100 # Disminucion por movimiento
                    
                    
                    # El jugador toca a un enemigo
                    
                    if posicion_jugador in enemigos:
                        puntaje -= 1000
                        vidas -= 1
                        posicion_jugador[:] = [0, 0]
                        
                        
                    # actualización de posiciones y tablero
                        
                    marcar_cuadrado(estado_tablero, posicion_jugador) # Activamos o desactivamos la posicion a la que se movio el jugador
                    enemigos = mover_enemigos(enemigos, obstaculos)
                    
                    
                    # Un enemigo toca al jugador
                    
                    if posicion_jugador in enemigos:
                        puntaje -= 1000
                        vidas -= 1
                        posicion_jugador[:] = [0, 0]
                        marcar_cuadrado(estado_tablero, posicion_jugador)
                    
                    
                    # Validacion de derrota
                    if vidas < 1:
                        return "derrota", 0
                   
                    
                    # Limitación de puntaje
                    
                    puntaje = max(puntaje, 100)
                    
                    
                # Movimiento invalido
                
                else:
                    # qbertito no se mueve
                    posicion_jugador[:] = posicion_anterior[:]

        
        # Validacion de victoria
        # Verifica que cada cuadro está activado
        
        victoria = True
        
        for fila in estado_tablero:
            for estado in fila:
                
                if not estado: # Un cuadrado está desactivado
                    victoria = False
                    
        if victoria:
            return "victoria", puntaje
        
        
        # Imagen numero vidas y puntuacion
        
        imagen_n_vidas = fuente.render(str(vidas), True, "white")
        imagen_puntuacion = fuente.render(str(puntaje), True, "white")
        
        
        
        # DIBUJO
        
        # Fondo del tablero
        
        pantalla.fill("black")
        
        
        # Dibujado de cada estado del tablero
        
        for i in range(10): # Posicion x tablero
            for j in range(10): # Posicion y tablero
            
                # Cuadrado activado
                
                if estado_tablero[i][j]:
                    pygame.draw.rect(pantalla, "#B266FF", pygame.Rect(*coordenadas([i, j]), TAMANO_CUADRADO, TAMANO_CUADRADO))
                
                
                # Cuadrado desactivado
                
                else: 
                    pygame.draw.rect(pantalla, "light blue", pygame.Rect(*coordenadas([i, j]), TAMANO_CUADRADO, TAMANO_CUADRADO))


        # Dibujado de obstáculos 
        
        for posicionObstaculo in obstaculos:
            pygame.draw.rect(pantalla, "#404040", pygame.Rect(*coordenadas(posicionObstaculo), TAMANO_CUADRADO, TAMANO_CUADRADO))
         
            
        # Dibujado del jugador
        
        pygame.draw.rect(pantalla, "orange", pygame.Rect(*coordenadas(posicion_jugador), TAMANO_CUADRADO, TAMANO_CUADRADO))


        # Dibujado de los enemigos
        
        for posicion_enemigo in enemigos:
            pygame.draw.rect(pantalla, "dark green", pygame.Rect(*coordenadas(posicion_enemigo), TAMANO_CUADRADO, TAMANO_CUADRADO))
        
        
        # Dibujado de textos
        
        pantalla.blit(texto_vidas, (715, 30))
        pantalla.blit(imagen_n_vidas, utiles.centro_topleft(imagen_n_vidas, 870, 100))
        pantalla.blit(texto_puntuacion, utiles.centro_topleft(texto_puntuacion, 870, 200))
        pantalla.blit(imagen_puntuacion, utiles.centro_topleft(imagen_puntuacion, 870, 250))
        pantalla.blit(texto_pausa, (760, 500))
        
        
        
        # ACTUALIZACION PANTALLA
        
        pygame.display.flip()
        clock.tick(60) # limite 60 fps
        
        
        
        
##############################################################################
    
# TABLERO (PROGRAMA PRINCIPAL)

if __name__ == "__main__":
    posicion_jugador = [0, 0] # Posicion del jugador en el tablero
    pygame.init()
    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
        
    try:
        main(pantalla, clock)
    finally:
        pygame.quit()
