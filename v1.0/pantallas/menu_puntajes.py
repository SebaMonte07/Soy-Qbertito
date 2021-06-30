#Mejores Puntajes 
#Joaco                 #faltaa kskdskdksdks

import sys
import pygame

escena_puntajes= pygame.image.load("c:/Users/joaco/Desktop/Carpetas/Algoritmos/Juego/Mi pantalla/fondo_juego.jpeg")
escena_puntajes= pygame.transform.scale(escena_puntajes, (650*5//3, 650))

#############################################################################
def MejoresPuntajes(pantalla, clock, puntuacion=10000, lista=[300000,200000,100000]):
    fuente = pygame.font.SysFont("Papyrus", 60, bold=True)
    fuente2= pygame.font.SysFont("Papyrus", 42, bold=True)
    fuente3= pygame.font.SysFont("Papyrus", 30, bold=True)

    texto_puntuacion = fuente.render("Puntuación:" + str(puntuacion), True, (0, 0, 0))
    texto_puntuacion2= fuente2.render("Mejores puntuaciones:", True, (0, 0, 0))
    texto_puntuacion3= fuente2.render(str(lista[0]), True, (0, 0, 0))
    texto_puntuacion4= fuente2.render(str(lista[1]), True, (0, 0, 0))
    texto_puntuacion5= fuente2.render(str(lista[2]), True, (0, 0, 0))
    texto_puntuacion6= fuente3.render("presione [m] para ir al menu principal", True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "m":
                    return "menu_principal"

                
        # DIBUJO 
        pantalla.blit(escena_puntajes, (0, 0))
        pantalla.blit(texto_puntuacion, (250, 60))
        pantalla.blit(texto_puntuacion2, (300, 180))
        pantalla.blit(texto_puntuacion3, (445, 260))
        pantalla.blit(texto_puntuacion4, (450, 320))
        pantalla.blit(texto_puntuacion5, (450, 380))
        pantalla.blit(texto_puntuacion6, (260, 500))
    
        # ACTUALIZACION DE PANTALLA
        pygame.display.flip()
        clock.tick(60)


#############################################################################

if __name__=="__main__":
    pygame.init()

    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
    
    try:
        MejoresPuntajes(pantalla, clock)
    finally:
        pygame.quit()
