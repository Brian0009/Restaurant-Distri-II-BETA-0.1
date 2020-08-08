#---------------------------------------------------------------------------
import pygame
from Objetos import Objeto
#---------------------------------------------------------------------------********
class Client:
#---------------------------------------------------------------------------
    def __init__(self, id, posx, posy, hambre, calma, antojo):
        self.name = id
        self.x = posx
        self.y =posy
        self.ancho = 30
        self.alto = 20
        self.color = (0,255,0)
        self.objeto = None
        self.hambre_base = hambre
        self.hambre = hambre
        self.calma_base = calma
        self.calma = calma
        self.antojo = antojo
#---------------------------------------------------------------------------
    def dibujar(self, ventana, font):
            pygame.draw.rect(ventana, self.color, (self.x,
                                                self.y,
                                                self.ancho,
                                                self.alto))
            if self.calma <= 0:
                aux = "0"
            else:
                aux = str(self.calma)                                        
            texto = font.render(aux, 1, (255, 255, 255))
            ventana.blit(texto, (self.x, self.y+ self.alto +5))
            texto = font.render(self.antojo, 1, (255, 255, 255))
            ventana.blit(texto, (self.x, self.y+ self.alto +15))
            if self.hambre <= 0:
                aux = "0"
            else:
                aux = str(self.hambre)   
            texto = font.render(aux, 1, (255, 255, 255))
            ventana.blit(texto, (self.x, self.y+ self.alto +30))                                      
            if self.objeto != None:
                self.objeto.dibujar(ventana, self.x, self.y, font)
            self.comer()                                           
#---------------------------------------------------------------------------
    def comer(self):
        if self.objeto != None:
            if self.objeto.name != "basura":
                self.hambre = -1
                self.objeto.procesar()
                return True
            else:
                self.calma = self.calma -1
        else:
            self.calma = self.calma -1           
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
#---------------------------------------------------------------------------   
    def getObjeto(self):
        return self.objeto
#---------------------------------------------------------------------------           
    def setObjeto(self, objeto):
        self.objeto = objeto   
#---------------------------------------------------------------------------********   