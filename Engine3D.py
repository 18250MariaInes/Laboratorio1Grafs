"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR1 Points
"""

from gl import Render, color

r = Render(1920,1080,1,0,0)

r.glColor(0,1,1)
#r.glClearColor(1,0,0)



posX = 10
posY = 10

for x in range(100):
    r.glVertex( posX, posY )
    posX += 1
    posY += 1

#r.glVertex(posX, posY)


r.glfinish('output.bmp')

#r.set_color(color(255,0,0))


