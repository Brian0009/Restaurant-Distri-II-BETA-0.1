#---------------------------------------------------------------------------
import pygame
from Protagonista import protagonista
from Clientes import Client
from Hornitos import Horno
from Objetos import Objeto
#---------------------------------------------------------------------------
def colision(objA, objB, nx, ny):
    if objA.get_futuro_espacio(nx, ny).colliderect(objB.get_espacio()):
        return True
    else:
        return False    
#---------------------------------------------------------------------------
def revisar_colisiones_prota(prota, objetos, nx, ny):
    contador = 0
    llave = False
    while contador < len(objetos) and llave!=True:
        if colision(prota, objetos[contador], nx, ny) == True:
            print("no te puedes mover, hay un objeto!")
            return False
        contador = contador +1
    return True    
#---------------------------------------------------------------------------
def interaccion(prota, clientes, hornos): #,basuras
    if prota.orientacion == "arriba":
        nx =0
        ny = -10 
    elif prota.orientacion == "abajo":
        nx = 0
        ny = 10
    elif prota.orientacion == "derecha":
        nx = 10
        ny = 0
    elif prota.orientacion == "izquierda":
        nx = -10
        ny = 0
    contador = 0  
    llave = True        
    while contador < len(clientes) and llave == True:
        if colision(prota, clientes[int(contador)], nx, ny) == True:
            print("interacicion con:!"+clientes[int(contador)].name)
            llave = False
            if (clientes[int(contador)].objeto == None):
                if prota.objeto != None:
                    if prota.objeto.name == clientes[int(contador)].antojo:
                        clientes[int(contador)].setObjeto(prota.getObjeto())
                        prota.setObjeto(None)
                    else:
                        print("sonar feo")
                else:
                    print("sonar feo")                        
            else:
                if clientes[int(contador)].objeto.name == "basura":
                        prota.setObjeto(clientes[int(contador)].objeto)
                        clientes[int(contador)].setObjeto(None)
                else:
                    print("sonar feo")        
        contador = contador +1     
    contador = 0 
    llave = True           
    while contador < len(hornos) and llave == True:
        if colision(prota, hornos[int(contador)], nx, ny) == True:
            print("interacicion con:!"+hornos[int(contador)].name)
            if hornos[int(contador)].objeto != None and hornos[int(contador)].comida_lista  and prota.objeto == None:
                prota.setObjeto(hornos[int(contador)].getObjeto())
                hornos[int(contador)].setObjeto(None)
                llave = False
            else:
                print("sonar feo")    
        contador = contador +1       
#---------------------------------------------------------------------------
pygame.init()
limite_X_m = 0
limite_Y_m = 0
limite_X = 1000
limite_y = 500
ventana = pygame.display.set_mode((limite_X, limite_y))
pygame.display.set_caption("RESTAURANT DISTRI II")
myfont = pygame.font.SysFont("textos", 13)
run = True
#---------------------------------------------------------------------------
prota = protagonista("Brian") 
clientes = [ ]
hornos = [ ]
lista_comidas = ["Cheescake", "Salchipapa", "Momazo"]
clientes.append(Client("cliente 1", 60, 200, 500, 3500, lista_comidas[0]))
clientes.append(Client("cliente 2", 200, 200, 750, 4000, lista_comidas[1]))
clientes.append(Client("cliente 3", 400, 200, 100, 6000, lista_comidas[2]))
hornos.append(Horno("horno de cheescake", 30, 30, lista_comidas[0], 30))
hornos.append(Horno("horno de salchipapas",  90, 30, lista_comidas[1], 200))
hornos.append(Horno("horno de momazos",170, 30, lista_comidas[2], 500))
#---------------------------------------------------------------------------
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se sale del juego
            run = False  
    #Controles:
    #----------------------------------------
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and prota.y > limite_Y_m:
        prota.orientacion = "arriba"
        if revisar_colisiones_prota(prota, clientes+ hornos, 0, -10):
            prota.movimiento(0,-10)
    if key[pygame.K_DOWN] and prota.y < limite_y:
        prota.orientacion = "abajo"
        if revisar_colisiones_prota(prota, clientes + hornos, 0, 10):
            prota.movimiento(0,10)
    if key[pygame.K_LEFT] and prota.x > limite_X_m:
        prota.orientacion = "izquierda"
        if revisar_colisiones_prota(prota, clientes + hornos, -10, 0):
            prota.movimiento(-10,0)             
    if key[pygame.K_RIGHT] and prota.x < limite_X:
        prota.orientacion = "derecha"   
        if revisar_colisiones_prota(prota, clientes + hornos, 10, 0):
            prota.movimiento(10,0)
    #interaccion         
    if key[pygame.K_SPACE]:
        print("...")
        interaccion(prota, clientes, hornos)   
    #funciones de interaccion BETA
     #----------------------------------------
    if key[pygame.K_z]:
        prota.setObjeto(None)
    if  key[pygame.K_x]: 
        hornos[0].cocinar()
    if  key[pygame.K_w]:
        hornos[1].cocinar()                 
    #----------------------------------------
    ventana.fill((0, 0, 0))
    prota.dibujar(ventana, myfont)
    contador =0
    while contador < len(clientes):
        clientes[int(contador)].dibujar(ventana, myfont)
        contador = contador+1.
    contador =0
    while contador < len(hornos):
        hornos[int(contador)].dibujar(ventana, myfont)
        hornos[int(contador)].cocinar()
        contador = contador+1.        
    pygame.display.update()  
#---------------------------------------------------------------------------    
pygame.quit()  # Se cierra pygame     
#---------------------------------------------------------------------------          
