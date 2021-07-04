#Historia
#Seba
import sys
import pygame

historia_imagen = pygame.image.load("imagenes/fondo_historia.jpg")
historia_imagen = pygame.transform.scale(historia_imagen,(650*5//3 , 650))

def ahz(pantalla, clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            elif event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada == "return":
                    return "instrucciones"
                
        pantalla.blit(historia_imagen, (0,0))
        pygame.display.flip()
        clock.tick(60)


##############################################################################

if __name__ == "__main__":
    pygame.init()
    
    pantalla = pygame.display.set_mode((650*5//3, 650))
    clock = pygame.time.Clock()
    
    try:
        ahz(pantalla, clock)
    finally:
        pygame.quit()
            
   
                
