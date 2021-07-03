# Felipe

import sys
import pygame

escena_instrucciones = pygame.image.load("imagenes/fondo_instrucciones2.jpg")
escena_instrucciones= pygame.transform.scale(escena_instrucciones,(650*5//3 , 650))

def main(pantalla, clock):
    i = 0
    while True: 
        i += 1
        if i == 20*60:   #segundos para leer las instrucciones 20 seg
            return "tablero"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                return "tablero"  #para apretar cualquier letra y pasar a la siguiente pantalla
     
        # DIBUJO 
        pantalla.blit(escena_instrucciones, (0, 0))
        
        # ACTUALIZACION DE PANTALLA
        pygame.display.flip()
        clock.tick(60)

##############################################################################

if __name__ == "__main__":
    pygame.init()
    
    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
    
    try:
        main(pantalla, clock)
    finally:
        pygame.quit()





