# Ventana principal. Programar transiciones aqui

import pygame
from pantallas import menu_principal, instrucciones, tablero, pantalla_resultados, menu_puntajes

pygame.init()

pantalla = pygame.display.set_mode((650*5//3, 650))
clock = pygame.time.Clock()

def qbertito(pantalla, clock):
    pantalla_actual = "instrucciones"
    
    while True:
        if pantalla_actual == "menu_principal":
            break
        
        elif pantalla_actual == "instrucciones":
            pantalla_actual = instrucciones.main(pantalla, clock)
        
        elif pantalla_actual == "historia":
            break
        
        elif pantalla_actual == "tablero":
            pantalla_actual = tablero.main(pantalla, clock)
            
        elif pantalla_actual == "victoria":
            pantalla_actual = pantalla_resultados.victoria(pantalla, clock)
            
        elif pantalla_actual == "derrota":
            pantalla_actual = pantalla_resultados.derrota(pantalla, clock)
            
        elif pantalla_actual == "puntajes":
            pantalla_actual = menu_puntajes.MejoresPuntajes(pantalla, clock)
            

try:
    qbertito(pantalla, clock)
    
finally:
    pygame.quit()
    

