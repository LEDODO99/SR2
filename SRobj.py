##Luis Estuardo Delgado 17187
##Tarea SR1
import struct
def char(c):
    return struct.pack("=c", c.encode('ascii'))
def word(c):
    return struct.pack("=h",c)
def dword(c):
    return struct.pack("=l",c)
def color(r,g,b):
    return bytes([b,g,r])
class image(object):
    def __init__(self):
        self.Ccolor=color(0,0,0)
        self.Vcolor=color(255,255,255)
        self.framebuffer=[]
        self.VPvx=0
        self.VPvy=0
        self.VPlf=0
        self.VPrf=0
        self.VPuf=0
        self.VPdf=0
        self.width=0
        self.height=0
    def glCreateWindow(self, width,height):
        self.width=width
        self.height=height

    def glViewPort(self,x,y,width,height):
        if((width%2)==0):
            self.VPlf=(int)(x-((width/2)-1))
            self.VPrf=(int)(x+(width/2))
        else:
            self.VPlf=(int)(x-((width/2)))
            self.VPrf=(int)(x+(width/2))
        if((height%2)==0):
            self.VPdf=(int)(y-((height/2)-1))
            self.VPuf=(int)(y+(height/2))
        else:
            self.VPdf=(int)(y-(height/2))
            self.VPuf=(int)(y+(height/2))
        
        if(self.VPlf<0):
            return 0
        elif(self.VPrf>self.width-1):
            return 0
        elif(self.VPuf>self.height-1):
            return 0
        elif(self.VPdf<0):
            return 0
        else:
            self.VPvx=x
            self.VPvy=y
            return 1
    def glClear(self):
        self.framebuffer=[
            [
                self.Ccolor
                for x in range(self.width)
                ]
            for y in range (self.height)
            ]
    def glClearColor(self,r,g,b):
        self.Ccolor=color(round(r*255),round(g*255),round(b*255))
    def glVertex(self,x,y):
        equis=0
        ye=0
        if(x<0):
            equis=(int)((x*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x>0):
            equis=(int)((x*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis=self.VPvx
        if(y<0):
            ye=(int)((y*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y>0):
            ye=(int)((y*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye=self.VPvy
        self.framebuffer[ye][equis]=self.Vcolor
    def glColor(self,r,g,b):
        self.Vcolor=color(round(r*255),round(g*255),round(b55))
    def glFinish(self):
        f = open("out.bmp", 'wb')
	#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(54+(self.width*self.height)*3))
        f.write(dword(0))
        f.write(dword(54))
	#image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()
    def glFinishNamed(self,filename):
        f = open(filename, 'wb')
	#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(54+(self.width*self.height)*3))
        f.write(dword(0))
        f.write(dword(54))
	#image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width*self.height*3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()
   
    def glLine(self,x0,y0,x1,y1):
        if(x0<0):
            equis1=(int)((x0*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x0>0):
            equis1=(int)((x0*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis1=self.VPvx
        if(y0<0):
            ye1=(int)((y0*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y0>0):
            ye1=(int)((y0*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye1=self.VPvy
        if(x1<0):
            equis2=(int)((x1*(self.VPvx-self.VPlf))+self.VPvx)
        elif(x1>0):
            equis2=(int)((x1*abs(self.VPvx-self.VPrf))+self.VPvx)
        else:
            equis2=self.VPvx
        if(y1<0):
            ye2=(int)((y1*(self.VPvy-self.VPdf))+self.VPvy)
        elif(y1>0):
            ye2=(int)((y1*abs(self.VPvy-self.VPuf))+self.VPvy)
        else:
            ye2=self.VPvy

        dy=abs(ye2-ye1)
        dx=abs(equis2-equis1)
        steep = dy>dx
        if steep:
            equis1,ye1=ye1,equis1
            equis2,ye2=ye2,equis2
            dy=abs(ye2-ye1)
            dx=abs(equis2-equis1)
        if equis1>equis2:
            equis1,equis2=equis2,equis1
            ye1,ye2=ye2,ye1
        offset = 0
        threshhold=dx
        y=ye1
        equis2+=1
        for x in range(equis1,equis2,+1):
            if steep:
                self.framebuffer[x][y]=self.Vcolor
            else:
                self.framebuffer[y][x]=self.Vcolor
            offset +=dy
            if offset>=threshhold:
                if ye1<ye2:
                    y+=1
                else:
                    y-=1
                threshhold+=dx
    def fill(self):
        for x in range(self.width):
            pintar=False
            canChange=True
            for y in range(self.height):
                if(self.framebuffer[y][x]==self.Ccolor):
                    canChange=True
                    if pintar:
                        self.framebuffer[y][x]=self.Vcolor
                else:
                    if canChange:
                        pintar = not pintar
                        if(self.framebuffer[y+1][x+1]==self.Ccolor):
                            canChange=False
    def readObj(self,filename):
        self.vertices = []
        self.faces=[]
        #Lee el archivo y separa las lineas en una lista
        with open(filename) as f:
            self.lines=f.read().splitlines()
        #Lee linea por linea
        for linea in self.lines:
            if linea:
                #revisa cual es el inicio de la linea
                prefix, valor = linea.split(" ",1)
                #inicio de linea de vertice
                if prefix=="v":
                    self.vertices.append(list(map(float,valor.split(" "))))
                #inicio de la linea de cara
                elif prefix=="f":
                    cadenas=valor.split(" ")
                    verticesAU=[]
                    for cadena in cadenas:
                        #solo toma el valor que dice que vertice se esta trabajando
                        v,r=cadena.split("/",1)
                        verticesAU.append(int(v))
                    #guarda todos los vertices que se trabajan
                    self.faces.append(verticesAU)
        #valores=[]                     \
        #valores.append(self.vertices)  |
        #valores.append(self.faces)      > Nada importante
        #return valores                 /
        for a in self.faces:
            xs=[]
            ys=[]
            p=0
            for o in a:
                xs.append(self.vertices[o-1][0])
                ys.append(self.vertices[o-1][1])
                p+=1
                
            #x0=self.vertices[a[0]-1][0]
            #y0=self.vertices[a[0]-1][1]
            #x1=self.vertices[a[1]-1][0]
            #y1=self.vertices[a[1]-1][1]
            #x2=self.vertices[a[2]-1][0]
            #y2=self.vertices[a[2]-1][1]
            #self.glLine(x0,y0,x1,y1)
            #self.glLine(x1,y1,x2,y2)
            #self.glLine(x2,y2,x0,y0)
            for o in range(0,p,+1):
                if o==0:
                    r=p-1
                else:
                    r=o-1
                self.glLine(xs[r],ys[r],xs[o],ys[o])


            
