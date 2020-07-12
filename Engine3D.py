"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR1 Points
Main
"""

from gl import Render

#valores con los que se inicializan la ventana y viewport
posX = 480
posY = 270
width=1920
height=1080
#creacion de Window
r = Render(width,height,0,0,0)

#creacion del viewport
r.glViewPort(posX, posY, width - width/2 , height - height/2)

#cambio de color con el que se hará el punto
r.glColor(1,1,1)

#se dibuja el punto en relación al viewport
r.glVertex(0, 0)

#se dibuja
r.glFinish('output.bmp')




