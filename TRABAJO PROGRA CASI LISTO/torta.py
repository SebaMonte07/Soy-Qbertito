import turtle as t
diccio = {"Chile": 1,"Perú": 2,"Brasil":3,"Japón":4,"China":5,"Argentina":6}
colorsR = ["#ad6a6a","#45a371","#113c61"]
t.ht()#Con esto se esconde la tortuga
radius = 200 ## circumference of a circle = 2pie*r
t.up()
t.forward(radius)
t.left(90)
t.down()
t.circle(radius)
t.up()
t.home()
t.right(90)

def divideTorta(diccio,colorsR):
    perc = 0
    radius = 200
    total = sum(list(diccio.values())) # suma las claves del diccio
    contador = 0
    for percent in diccio:
        x = (diccio[percent] * 100)/total
        porciento  = (x * 360)/100
        perc += porciento
        t.color("black")
        t.setheading(perc)
        t.down()
        t.forward(radius)
        t.up()
        t.home()
        t.up()
        if(contador == len(colorsR)):
          contador = 0
        t.color(colorsR[contador])
        contador = contador + 1
        t.begin_fill()
        t.setheading(perc)
        t.forward(radius)
        t.left(-90)
        t.down()
        t.circle(-radius, porciento)
        t.end_fill()
        t.up()
        t.end_fill()
        t.home()
        t.right(-90)
        
def colocaNombresTorta(diccio):
    perc = 0
    radius = 200
    total = sum(list(diccio.values())) # suma las claves del diccio
    for percent in diccio:
        x = (diccio[percent] * 100)/total
        porciento  = (x * 360)/100
        perc += porciento
        t.color("black")
        t.setheading(perc-(porciento/2))
        t.forward(radius/1.5)
        t.write(percent, align="center", font=("arial", 15, "normal"))
        t.setheading(-40)
        t.forward(40)
        t.write(str(round(x,1))+"%", align="center", font=("arial", 18, "normal"))
        t.home()
divideTorta(diccio,colorsR)
colocaNombresTorta(diccio)
screen = t.Screen()
screen.exitonclick()
# falta colocar color, completar el posicionamieton del porcentaje, y crear el titulo.