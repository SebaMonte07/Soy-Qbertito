# Ventana principal. Programar transiciones aqui

import pygame
from pantallas import menu_principal, instrucciones, tablero, pantalla_resultados, menu_puntajes, historia

pygame.init()

pygame.display.set_caption("Soy Qbertito 1.0")

pantalla = pygame.display.set_mode((650*5//3, 650))
clock = pygame.time.Clock()

def qbertito(pantalla, clock):
    pantalla_actual = "menu_principal"
    puntaje = 0
    mejores_puntajes = [0, 0, 0]
    
    while True:
        if pantalla_actual == "menu_principal":
            pantalla_actual = menu_principal.menu_principal(pantalla, clock)
        
        elif pantalla_actual == "instrucciones":
            pantalla_actual = instrucciones.main(pantalla, clock)
        
        elif pantalla_actual == "historia":
            pantalla_actual = historia.ahz(pantalla, clock)
        
        elif pantalla_actual == "tablero":
            pantalla_actual, puntaje = tablero.main(pantalla, clock)
            
            mejores_puntajes.append(puntaje)
            mejores_puntajes.sort(reverse=True)
            mejores_puntajes.pop()
            
        elif pantalla_actual == "victoria":
            pantalla_actual = pantalla_resultados.victoria(pantalla, clock, puntaje)
            menu_puntajes.MejoresPuntajes(pantalla, clock, puntaje, mejores_puntajes)
            
        elif pantalla_actual == "derrota":
            pantalla_actual = pantalla_resultados.derrota(pantalla, clock)
            
            

try:
    qbertito(pantalla, clock)
    
finally:
    pygame.quit()
    

