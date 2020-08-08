#---------------------------------------------------------------------------
import pygame
#---------------------------------------------------------------------------********
class Objeto:
#---------------------------------------------------------------------------
    def __init__(self, nombre, coef):
        self.coef = coef
        self.name = nombre
        self.ancho = 5
        self.alto = 5
        self.color = (255,255,0)
#---------------------------------------------------------------------------
    def dibujar(self, ventana, x, y, font):
            pygame.draw.rect(ventana, self.color, (x,
                                                y,
                                                self.ancho,
                                                self.alto)) 
            texto = font.render(self.name, 1, (255, 255, 255))
            ventana.blit(texto, (x, y))
                                    
#--------------------------------------------------------------------------- 
    def get_espacio(self):
        return pygame.Rect(self.x, self.y, self.ancho, self.alto)
#--------------------------------------------------------------------------- 
    def procesar(self):
       self.coef = self.coef-1
       if self.coef <=0:
           self.name = "basura"
           print("comida acabada")        
#---------------------------------------------------------------------------********   