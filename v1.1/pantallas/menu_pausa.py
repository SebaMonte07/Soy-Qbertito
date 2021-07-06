#Menu Pausa

import pygame
import sys

##############################################################################
def main(pantalla, clock):
    fuente_grande = pygame.font.SysFont("Papyrus", 120)
    fuente = pygame.font.SysFont("Papyrus", 56)
    
    texto_pausa = fuente_grande.render("Pausa", True, "white")
    texto_reanudar = fuente.render("[P] - Reanudar", True, "white")
    texto_reiniciar = fuente.render("[R] - Reiniciar", True, "white")
    
    imagen_congelada = pygame.display.get_surface() # Consigue la ultima imagen actualizada
    
    # Genera pseudo-transparencia. 
    # la flag multiplica pixel por pixel px1*px2//256
    imagen_congelada.fill((30, 30, 30), special_flags=pygame.BLEND_RGB_MULT) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                
                if tecla_presionada == "p":
                    return False
                
                if tecla_presionada == "r":
                    return True
                
        # DIBUJO 
        pantalla.blit(imagen_congelada, (0, 0))
        pantalla.blit(texto_pausa, (370, 50))
        pantalla.blit(texto_reanudar, (350, 350))
        pantalla.blit(texto_reiniciar, (360, 440))
        
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
