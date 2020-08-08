#---------------------------------------------------------------------------
import pygame
from Objetos import Objeto
#---------------------------------------------------------------------------********
class protagonista:
#---------------------------------------------------------------------------
    def __init__(self, nombre):
        self.name = nombre
        self.x = 5
        self.y = 5
        self.ancho = 10
        self.alto = 20
        self.color = (0,0,255)
        self.objeto = None
        self.orientacion = "abajo"
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font):
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            if self.objeto != None:
                self.objeto.dibujar(ventana, self.x, self.y, font)                                         
#---------------------------------------------------------------------------
    def movimiento(self, x,y):
        if (self.x+x)>0:
            self.x = self.x + x
        if (self.y+y)>0:
            self.y = self.y + y
#---------------------------------------------------------------------------
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)  
#---------------------------------------------------------------------------
    def get_futuro_espacio(self, x, y):
        return pygame.Rect(self.x+x, self.y+y, self.ancho, self.alto)
#---------------------------------------------------------------------------   
    def getObjeto(self):
        return self.objeto
#---------------------------------------------------------------------------           
    def setObjeto(self, objeto):
        self.objeto = objeto 
#--------------------------------------------------------------------------- 
    def tieneObjeto(self):
        if self.objeto== None:
            return False
        else:
            return True                                              
#---------------------------------------------------------------------------*********