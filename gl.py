import struct

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h',w)

def dword(d):
    # 4 bytes
    return struct.pack('=l',d)

def color(r, g, b):
    return bytes([b, g, r])


BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Render(object):
    def __init__(self, width, height, red, green, blue):
        self.width = width
        self.height = height
        self.curr_color = WHITE
        self.curr_color_bg=BLACK
        self.glClearColor(red, green, blue)
        self.glClear()
    
    def glClearColor(self, red, green, blue):
        nred=int(255*red)
        ngreen=int(255*green)
        nblue=int(255*blue)
        self.curr_color_bg = color(nred, ngreen, nblue)

    def glClear(self):
        self.pixels = [ [ self.curr_color_bg for x in range(self.width)] for y in range(self.height) ]

    


    

    def glVertex(self, x, y):
        self.pixels[y][x] = self.curr_color

    def glColor(self, red, green, blue):
        nred=int(255*red)
        ngreen=int(255*green)
        nblue=int(255*blue)
        

        self.curr_color = color(nred, ngreen, nblue)

    def glfinish(self, filename):
        archivo = open(filename, 'wb')

        # File header 14 bytes
        #archivo.write(char('B'))
        #archivo.write(char('M'))

        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))

        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # Image Header 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))

        # Pixeles, 3 bytes cada uno

        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])


        archivo.close()











