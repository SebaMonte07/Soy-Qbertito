import turtle as t

def main():
  diccio = {"Chile":"195","Perú":"285","Brasil":"580","Japón":"283","China":"100","Argentina":"600"}
  colorsR = ["#ad6a6a","#45a371","#113c61"]
  t.setup(700,500,50,50)
  t.setworldcoordinates(0,0,750,500)
  t.speed("fast")
  grafBarra(diccio,colorsR)

  t.done()
#
def grafBarra(diccio,colors):
  t.up()
  t.goto(100,100)
  t.down()
  pos = 0
  cont = 0
  for pais in diccio:
    if(pos == len(colors)):
      pos=0
    creaBarra(pais,diccio[pais],colors[pos])
    pos += 1
    cont += 1
  t.up()
  t.goto(80,400)
  t.down()
  t.setheading(270)
  t.color("black")
  t.write("600",False,"right")
  t.fd(300)
  t.left(90)
  t.fd(cont*65)
#
def creaBarra(pais,alt,clr):
  alt=int(alt)/2
  t.begin_fill()
  t.color(clr)
  t.setheading(90)
  #Escribe nombre del pais
  t.up()
  t.bk(20)
  t.color("black")
  t.write(pais)
  t.color(clr)
  t.fd(20)
  t.down()
  #Crea barra
  t.fd(alt)
  t.right(90)
  t.color("black")
  t.write(int(alt)*2,False)
  t.write
  t.color(clr)
  t.fd(40)
  t.right(90)
  t.fd(alt)
  t.left(90)
  t.penup()
  t.fd(20)
  t.pendown()
  t.end_fill()

#
main()