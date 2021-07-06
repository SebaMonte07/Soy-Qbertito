# MenÃº principal
#Luciano

import sys
import pygame

fondo_menu = pygame.image.load("imagenes/menu_principal.png")
fondo_menu = pygame.transform.scale(fondo_menu, (650*5//3, 650))


############################################################################3333

def menu_principal(pantalla, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "return":
                    return "historia"

        #DIBUJO 
        pantalla.blit(fondo_menu, (0, 0))
        
        #ACTUALIZACION DE PANTALLA
        pygame.display.flip()
        clock.tick(60)







######################################################################################3





if __name__== "__main__":
    pygame.init()

    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
    
    try:
        menu_principal(pantalla, clock)
    finally:
        pygame.quit()
    

