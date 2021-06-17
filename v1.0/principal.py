# Ventana principal. Programar transiciones aqui
from pantallas import menu_principal, tablero

pantalla = pygame.display.set_mode()

pantalla_actual = "menu_principal"
while True:
  if pantalla_actual == "menu_principal":
    pantalla_actual = menu_principal()
  elif pantalla_actual == "trablero":
    pantalla_actual = tablero()
