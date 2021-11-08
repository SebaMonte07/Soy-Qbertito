import turtle
import sys

# Errores

class Error(Exception):
    pass

class FormatoIncorrectoError(Error):
    pass

class OpcionInvalidaError(Error):
    pass



def main():
    datos, colores = cargaArchivos()
    
    paleta_colores = solicitaPaletaColores(colores)
    tipo_grafico = solicitaTipoGrafico()
    
    graficaDatos(datos, colores, tipo_grafico, paleta_colores)
        
    

def cargaArchivos():
    nombres = ["datos", "colores"]
    funcs = [verificaDatos, verificaColores]
    retorno = []
    
    print(" - Presione ENTER en cualquier momento para finalizar el programa.")
    for nom, func_validacion in zip(nombres, funcs):
        valido = False
        while(not valido):
            try:
                nombre_archivo = input(f"Ingrese el nombre del archivo de {nom}: ")
                if(nombre_archivo == ""):
                    print("\n - Programa finalizado por el usuario.")
                    sys.exit()
                    
                with open(nombre_archivo) as f:
                    retorno.append(func_validacion(f))
                    valido = True
                    
            except FileNotFoundError:
                print("No existe un archivo con ese nombre, inténtelo nuevamente.")
                    
            except (ValueError, FormatoIncorrectoError):
                print("El archivo no tiene el formato requerido, inténtelo nuevamente.")
                     
    return retorno
            

def verificaDatos(archivo):
    datos = {}
    
    for lin in archivo.readlines():
        dato, valor = lin.rstrip("\n").split(",")
        if(not valor.isdigit()):
            raise FormatoIncorrectoError
        datos[dato] = int(valor)

    return datos


def verificaColores(archivo):
        colores = {}
        lineas = archivo.readlines()
        
        # Siempre un nombre viene seguido de sus colores en formato hexadecimal
        for i in range(0, len(lineas), 2):
            key = lineas[i].rstrip("\n")
            val = lineas[i+1].rstrip("\n")
            hexas = map(lambda h: 0 <= int("0x"+h, 16) <= 16**6, val.split(","))
            f_colores = map(lambda x: len(x) == 6, val.split(","))
            
            if(not key.startswith(">") or not all(list(hexas)) or not all(f_colores)):
                raise FormatoIncorrectoError 
                
            colores[key.lstrip(">")] = tuple(val.split(","))

        return colores
    
    
def solicitaTipoGrafico():
    tipo_grafico = ["barras", "torta", "línea"]
    print("\nSelecciona el tipo de gráfico:")
    for i, tipo in enumerate(tipo_grafico):
        print(f"{i+1}) {tipo}")
    
    valido = False
    while(not valido):
        try:
            opcion = input("Ingrese opción: ")
            if(opcion == ""):
                sys.exit()
            opcion = int(opcion)
            if(opcion < 1 or opcion > len(tipo_grafico)):
                raise OpcionInvalidaError
            valido = True
            
        except:
            print("Opción no disponible")
    
    return tipo_grafico[opcion-1]


def solicitaPaletaColores(colores):
    colores_lista = list(colores.keys())
    print("\nSeleccione paleta de colores para su gráfico:")
    for i, color in enumerate(colores_lista):
        print(f"{i+1}) {color}")
        
    valido = False
    while(not valido):
        try:
            opcion = input("Ingrese opción: ")
            if(opcion == ""):
                sys.exit()
            opcion = int(opcion)
            if(opcion < 1 or opcion > len(colores_lista)):
                raise OpcionInvalidaError
            valido = True
            
        except (OpcionInvalidaError, ValueError):
            print("Opción no disponible")
    
    return colores_lista[opcion-1]


def graficaDatos(datos, colores, tipo_grafico, paleta_colores):
    print(datos)
    print(colores)
    print(tipo_grafico)
    print(paleta_colores)
        

main()