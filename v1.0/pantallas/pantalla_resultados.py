# Victoria o derrota
# Cristian

import sys
import pygame

escena_victoria = pygame.image.load("imagenes/escena_victoria.png")
escena_victoria = pygame.transform.scale(escena_victoria, (650*5//3, 650))

escena_derrota = pygame.image.load("imagenes/escena_derrota.png") 
escena_derrota = pygame.transform.scale(escena_derrota, (650*5//3, 650))

##############################################################################
def victoria(pantalla, clock, puntuacion=100000):
    fuente = pygame.font.SysFont("Papyrus", 42, bold=True)
    texto_puntuacion = fuente.render("Puntuación:" + str(puntuacion), True, (0, 0, 0))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "r":
                    return "tablero"
                
                elif tecla_presionada == "m":
                    return "menu_principal"
                
        # DIBUJO 
        pantalla.blit(escena_victoria, (0, 0))
        pantalla.blit(texto_puntuacion, (530, 100))
        
        # ACTUALIZACION DE PANTALLA
        pygame.display.flip()
        clock.tick(60)
        
        
def derrota(pantalla, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "r":
                    return "tablero"
                
                elif tecla_presionada == "m":
                    return "menu_principal"
                
        # DIBUJO 
        pantalla.blit(escena_derrota, (0, 0))
        
        # ACTUALIZACION DE PANTALLA
        pygame.display.flip()
        clock.tick(60)

##############################################################################

if __name__ == "__main__":
    pygame.init()
    
    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
    
    try:
        victoria(pantalla, clock)
        derrota(pantalla, clock)
    finally:
        pygame.quit()
