import turtle as t
diccio = {"Chile": 1,"Perú": 2,"Brasil":3,"Japón":4,"China":5,"Argentina":6}
colorsR = ["#ad6a6a","#45a371","#113c61"]
radius = 200 ## circumference of a circle = 2pie*r
t.up()
t.forward(radius)
t.left(90)
t.down()
t.circle(radius)
t.up()
t.home()
t.right(90)

def letter(diccio):
    perc = 0
    radius = 200
    total = sum(list(diccio.values())) # suma las claves del diccio
    
    for percent in diccio:
        x = (diccio[percent] * 100)/total
        letter  = (x * 360)/100
        perc += letter
        t.setheading(perc)
        t.down()
        t.forward(radius)
        t.up()
        t.home()
        t.setheading(perc-(letter/2))
        t.forward(radius/2)
        t.write(percent, align="center", font=("arial", 20, "normal"))
        t.home()
        t.setheading(perc-(letter/3))
        t.forward(radius/2)
        t.write(str(round(x,1))+"%", align="center", font=("arial", 20, "normal"))
        t.home()

letter(diccio)
screen = t.Screen()
screen.exitonclick()
# falta colocar color, completar el posicionamieton del porcentaje, y crear el titulo.