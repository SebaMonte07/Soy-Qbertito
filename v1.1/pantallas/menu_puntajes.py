#Mejores Puntajes 
#Joaco                 

import sys
import pygame
import utiles

escena_puntajes= pygame.image.load("imagenes/fondo_puntajes.jpeg")
escena_puntajes= pygame.transform.scale(escena_puntajes, (650*5//3, 650))

#############################################################################
def MejoresPuntajes(pantalla, clock, puntuacion=10000, lista=[300000,200000,100000]):
    fuente = pygame.font.SysFont("Papyrus", 60, bold=True)
    fuente2= pygame.font.SysFont("Papyrus", 42, bold=True)

    texto_puntuacion = fuente.render("Puntuación:" + str(puntuacion), True, (0, 0, 0))
    texto_puntuacion2= fuente2.render("Mejores puntuaciones:", True, (0, 0, 0))
    texto_puntuacion3= fuente2.render(str(lista[0]), True, (0, 0, 0))
    texto_puntuacion4= fuente2.render(str(lista[1]), True, (0, 0, 0))
    texto_puntuacion5= fuente2.render(str(lista[2]), True, (0, 0, 0))

    i = 0
    while True:
        i += 1
        if i == 10*60:
            return
        texto_segundos = fuente.render(f"- {10-i//60} -", True, "white")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                return
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "return":
                    return

                
        # DIBUJO 
        pantalla.blit(escena_puntajes, (0, 0))
        pantalla.blit(texto_puntuacion, utiles.centro_topleft(texto_puntuacion, 541, 100))
        pantalla.blit(texto_puntuacion2, utiles.centro_topleft(texto_puntuacion2, 541, 180))
        pantalla.blit(texto_puntuacion3, utiles.centro_topleft(texto_puntuacion3, 541, 260))
        pantalla.blit(texto_puntuacion4, utiles.centro_topleft(texto_puntuacion4, 541, 320))
        pantalla.blit(texto_puntuacion5, utiles.centro_topleft(texto_puntuacion5, 541, 380))
        pantalla.blit(texto_segundos, utiles.centro_topleft(texto_segundos, 541, 500))
    
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
