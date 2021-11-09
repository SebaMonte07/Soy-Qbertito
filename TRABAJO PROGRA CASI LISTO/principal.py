# Felipe Córdova - 20.960.184-2
# Sebastian Montecinos - 21.008.887-3
# Rodrigo Erlandsen - 20.840.411-3
# Cristián Cárdenas - 20.641.231-3
import turtle as t
import sys

# Errores posibles
class Errores(Exception):
    pass

class FormatoIncorrectoError(Errores):
    pass

class OpcionInvalidaError(Errores):
    pass

class nadaOespacios (Errores):
    pass

class Invalido (Errores):
    pass

# función main() que organiza el flujo principal del programa
def main():
    diccio_datos = validaDatos()
    diccio_color = validaColor()
    paleta_colores = solicitaPaletaColores(diccio_color)
    tipo_grafico = solicitaTipoGrafico()
    titulo = solicitaTitulo()
    print("Generando gráfico...")
    opcion_color = diccio_color[paleta_colores]

    #pantalla gráfica
    t.setup(750,500,50,50)
    t.setworldcoordinates(0,0,750,500)
    t.speed("fast")
    t.ht()#Con esto se esconde la tortuga
    
    if(tipo_grafico == "barras"):
        grafBarra(diccio_datos , opcion_color , titulo)
    elif(tipo_grafico == "línea"):
        grafLinea(diccio_datos , opcion_color , titulo)
    else: ## si se salta el if y el elif anterior es porque es torta
        creaTorta(diccio_datos , opcion_color, titulo)
    
    input("Presione Enter para finalizar")
   
def validaDatos(): #valida el nombre del archivo, valida el formato y retorna lo que contiene el archivo en forma de diccionario
    condicion = True
    while(condicion):
        try:
            nom = input("Ingrese nombre completo del archivo: ").strip()
            lineasDatos = {} #diccionario
            if (nom == ""):
                raise nadaOespacios
            else:
                with open(nom) as archivo:
                    for fila in archivo:
                        fila = fila.strip("\n") 
                        #x = fila.count(',') # tal vez sea innecesario
                        y = fila.split(',')
                        if(len(y) != 2):
                            raise Invalido
                        #elif(x != 1): # Nunca pasara por aqui
                            #raise Invalido
                        #int(y[1]) # esto aparece abajo, lanzará el ValueError igual
                        lineasDatos[y[0]] = int(y[1])
                    condicion = False
        except(FileNotFoundError):
            print("   No existe un archivo con ese nombre, inténtelo nuevamente")
        except(ValueError,Invalido):
            print("   El archivo no tiene el formato requerido, inténtelo nuevamente")
        except(nadaOespacios):
            print("   Nada ingresó, intentélo nuevamente")
    return lineasDatos


def validaColor(): ##valida el nombre del archivo para los colores, valida el formato y retorna lo que contiene el archivo en forma de diccionario
    condicion = True
    while(condicion):
        try:
            nom = input("Ingrese nombre del archivo de colores: ").strip()
            cont = 0
            diccio = {}
            if (len(nom) == 0):
                raise nadaOespacios
            else:
                with open(nom) as archivo:
                    temp = archivo.readlines()
                    if(len(temp)%2 != 0): # validacion el número de filas es par
                        raise Invalido
                    for fila in temp:
                        fila = fila.strip("\n")
                        if(cont == 0):
                            if (fila[0] != '>'): 
                                raise Invalido
                            y = fila 
                            #diccio[y.lstrip('>')] = "" # esto se hace en el elif
                            cont = 1
                        elif(cont == 1):
                            x = fila.split(',')
                            for i in range(0,len(x)):
                                if(len(x[i]) != 6):
                                    raise Invalido
                                num = int(str(x[i]), 16)
                                #hex(num) # con la linea anterior ya queda claro que es hexadecimal
                            diccio[y.lstrip('>')] = tuple(x)
                            cont = 0
                    condicion = False
        except(FileNotFoundError):
            print("   No existe un archivo con ese nombre, inténtelo nuevamente")
        except(ValueError, Invalido):
            print("   El archivo no tiene el formato requerido, inténtelo nuevamente")
        except(nadaOespacios):
            print("   Nada ingresó, intentélo nuevamente")
            
    return diccio
################################################################################################################

def solicitaTipoGrafico():
    tipo_grafico = ["barras", "torta", "línea"]
    print("\nSelecciona el tipo de gráfico:")
    # Enumerate: enumera cada elemento del iterador, funciona como contador
    for i, tipo in enumerate(tipo_grafico):
        print(f"   {i+1}) {tipo}") 
    
    condicion = True
    while(condicion):
        try:
            opcion = input("Ingrese opción: ").strip()
            if(opcion == ""): # PREGUNTAR POR ESTO
                sys.exit()
            opcion = int(opcion)
            if(opcion < 1 or opcion > len(tipo_grafico)):
                raise OpcionInvalidaError
            condicion = False
            
        except:
            print("Opción no disponible")
    
    return tipo_grafico[opcion-1]


def solicitaPaletaColores(colores):
    colores_lista = list(colores.keys())
    print("\nSeleccione paleta de colores para su gráfico:")
    for i, color in enumerate(colores_lista):
        print(f"   {i+1}) {color}")
        
    condicion = True
    while(condicion):
        try:
            opcion = input("Ingrese opción: ").strip()
            if(opcion == ""): # PREGUNTAR X2
                sys.exit()
            opcion = int(opcion)
            if(opcion < 1 or opcion > len(colores_lista)):
                raise OpcionInvalidaError
            condicion = False
            
        except (OpcionInvalidaError, ValueError):
            print("Opción no disponible")
    
    return colores_lista[opcion-1]

def solicitaTitulo():
    t = input("Ingrese un título para el gráfico: ").strip()
    while(t == ""):
        t = input("Error, Ingrese título nuevamente: ").strip()
        
    return t

####Grafico de barras####
def grafBarra(diccio,colors,titulo):#Hay que llamar a esta funcion
  t.up()
  t.goto(100,100)
  t.down()
  pos = 0
  cont = 0
  for pais in diccio:
    if(pos == len(colors)):
      pos = 0
    creaBarra(pais,diccio[pais],colors[pos])
    pos += 1
    cont += 1
  t.up()
  t.goto(80,400)
  t.down()
  t.setheading(270)
  t.color("black")
  t.write("600",False,"center")
  t.fd(300)
  t.left(90)
  t.fd(cont*65)
  t.up()
  xtitle = ((cont*65)/2)+80
  t.goto(xtitle,410)
  t.write(titulo,False,"center",font=("Verdana",13,"normal"))
#
def creaBarra(pais,alt,clr):
  alt = int(alt)/2
  t.begin_fill()
  t.color("#"+clr)
  t.setheading(90)
  #Escribe nombre del pais
  t.up()
  t.bk(20)
  t.color("black")
  t.write(pais)
  t.color("#"+clr)
  t.fd(20)
  t.down()
  #Crea barra
  t.fd(alt)
  t.right(90)
  t.color("black")
  t.write(int(alt)*2,False)
  t.color("#"+clr)
  t.fd(40)
  t.right(90)
  t.fd(alt)
  t.left(90)
  t.penup()
  t.fd(20)
  t.pendown()
  t.end_fill()

######Grafico de lineas#####
def grafLinea(diccio,colors,titulo):#Se llama a esta funcion para crear el grafico
  t.up()
  t.goto(80,100)
  t.down()
  cont = 0
  x = 120
  for pais in diccio:
    if(cont == 0):
      y = int(diccio[pais])/2
      #Grafica del primer pais, para evitar que salga una linea del origen
      t.begin_fill()
      t.up()
      t.goto(x,y+100)
      t.color("black")
      #Escribe el valor y el circulo
      t.up()
      t.goto(x,y+80)
      t.write(diccio[pais],False,"center")
      t.goto(x,y+100)
      t.down()
      t.color("#"+colors[0])
      t.circle(4)
      t.end_fill()
      #Escribe pais 1
      t.up()
      t.color("black")
      t.goto(x,80)
      t.write(pais,False,"center")
      t.goto(x,y+100)
    else:
      creaLinea(pais,diccio[pais],colors[0],x)
    x += 60
    cont += 1
  t.up()
  t.goto(90,400)
  t.down()
  t.setheading(270)
  t.color("black")
  t.write("600",False,"center")
  t.fd(300)
  t.left(90)
  t.fd(cont*65)
  t.up()
  xtitle = ((cont*65)/2)+90 #titulo
  t.goto(xtitle,410)
  t.write(titulo,False,"center",font=("Verdana",13,"normal"))
#
def creaLinea(pais,alt,clr,x):
  #la esquina inferior izquierda es 0,0
  alt = int(alt)/2
  t.down()
  t.begin_fill()
  t.color("#"+clr)
  #Crea linea y circulito
  t.goto(x,alt+100)
  t.circle(4)
  t.end_fill()
  #escribe el valor
  t.up()
  t.goto(x,alt+80)
  t.down()
  t.color("black")
  t.write(int(alt*2),False,"center")
  t.up()
  t.goto(x,alt + 100)
  #escribe pais
  t.up()
  t.goto(x,80)
  t.write(pais,False,"center")
  t.goto(x,alt+100)

def creaTorta(diccio, colorsR,titulo):
    t.ht()#Con esto se esconde la tortuga
    radius = 200 ## circumference of a circle = 2pi*r
    t.up()
    t.forward(radius)
    t.down()
    t.circle(radius)
    t.up()
    t.setheading(90)
    t.forward(radius)
    divideTorta(diccio ,colorsR)
    colocaNombresTorta(diccio)
    xtitle = (((3)*65)/2)+105 #titulo
    t.goto(xtitle,410)
    t.write(titulo,False,"center",font=("Verdana",13,"normal"))

def divideTorta(diccio,colorsR):
    perc = 0
    radius = 200
    total = sum(list(diccio.values())) # suma las claves del diccio
    contador = 0
    for percent in diccio:
        x = (diccio[percent] * 100) / total
        porciento  = (x * 360)/100
        perc += porciento
        t.color("black")
        t.setheading(perc)
        t.down()
        t.forward(radius)
        t.forward(-radius)
        t.up()
        t.up()
        if(contador == len(colorsR)):
          contador = 0
        t.color("#" + colorsR[contador])
        contador += 1
        t.begin_fill()
        t.setheading(perc)
        t.forward(radius)
        t.left(-90)
        t.down()
        t.circle(-radius, porciento)
        t.end_fill()
        t.setheading(perc-porciento)
        t.forward(-radius)
        t.up()
        t.right(-90)
        
def colocaNombresTorta(diccio):
    perc = 0
    radius = 200
    total = sum(list(diccio.values())) # suma las claves del diccio
    for percent in diccio:
        x = (diccio[percent] * 100) / total
        porciento  = (x * 360) / 100
        perc += porciento
        t.color("black")
        t.setheading(perc-(porciento/2))
        t.forward(radius/1.5)
        t.write(percent, align="center", font=("arial", 15, "normal"))
        t.setheading(-40)
        t.forward(40)
        t.write(str(round(x,1))+"%", align="center", font=("arial", 18, "normal"))
        t.forward(-40)
        t.setheading(perc-(porciento/2))
        t.forward(-radius/1.5)




































main()
