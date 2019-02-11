import pygame
import sys
import os

pygame.font.init()

font = pygame.font.SysFont("Verdana", 18)
font_color = (255,255,255)
font_background = (0,0,0)
input_box = pygame.Rect(317,291,164,21)

apodo = ""

velocidad_v = 1
velocidad_h = 2

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen, num, pos=[10,10], size=(100,100)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + " camina"+str(num)+".png")
        self.image = pygame.transform.scale(self.image, size)
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (pos)

class Fondo(pygame.sprite.Sprite):
    def __init__(self, fondo, pos=[0,0], size=(800,600)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/fondos/" + fondo + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]
        
class Boton(pygame.sprite.Sprite):
    def __init__(self, boton, pos, size=(130,30)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/botones/" + boton + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]

class Pantalla:
    def __init__(self,manager):
        self.manager = manager
        self.sprites = {}
        self.canvas = pygame.display.set_mode((800, 600))
        """self.eventos =	{
        "Retroceder": False, #Pantalla anterior
        "Arriba": False,
        "Abajo": False,
        "Derecha": False,
        "Izquierda": False,
        "Salir": False,        
        "POSX": 0,
        "POSY": 0
        }"""

    def set_nombre_ventana(self, titulo):
        pygame.display.set_caption(titulo)
    
    def obtener_ultima_pantalla(self):
        pass

    def agregar_sprite(self, nombre, sprite):
        self.sprites[nombre] = sprite
        
    def handle_events(self):
        pass

    def update(self):
        pass 

    def render(self):
        pass
    
class ListaEscenarios(Pantalla):
    def __init__(self,manager):
        Pantalla.__init__(self,manager)
        #Imagenes a usar
        nom_fondos = ["fondo","palacio","aeropuerto","plaza(dia)","plaza(noche)"]
        self.fondo = "fondo"
        fuente = pygame.font.SysFont("Arial",22)
        self.texto_palacio = fuente.render("Palacio de Gobierno",0,(127,127,127))
        self.texto_aeropuerto = fuente.render("Aeropuerto Jorge Chavez",0,(127,127,127))
        self.texto_plazaD = fuente.render("Plaza de Armas (Dia)",0,(127,127,127))
        self.texto_plazaN = fuente.render("Plaza de Armas(Noche)",0,(127,127,127))
        for nom in nom_fondos:
            self.agregar_sprite(nom,Fondo(nom))

        self.set_nombre_ventana("Escoger Escenario")
        self.handle_events()
        self.update()

    def handle_events(self):
        x,y = pygame.mouse.get_pos()
        if x >=340 and x <= 495 and y >= 100 and y <= 122:
            self.fondo = "palacio"
        elif x >=317 and x <= 500 and y >= 200 and y <= 222:
            self.fondo = "aeropuerto"
        elif x >=335 and x <= 490 and y >= 300 and y <= 322:
            self.fondo = "plaza(dia)"
        elif x >=333 and x <= 500 and y >= 400 and y <= 422:
            self.fondo = "plaza(noche)"
        else:
            self.fondo = "fondo"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if x >=340 and x <= 495 and y >= 100 and y <= 122:
                    self.manager.cambiar_pantalla(PruebaJugabilidad(self.manager,self.sprites[self.fondo]))
                elif x >=317 and x <= 500 and y >= 200 and y <= 222:
                    self.manager.cambiar_pantalla(PruebaJugabilidad(self.manager,self.sprites[self.fondo]))
                elif x >=335 and x <= 490 and y >= 300 and y <= 322:
                    self.manager.cambiar_pantalla(PruebaJugabilidad(self.manager,self.sprites[self.fondo]))
                elif x >=333 and x <= 500 and y >= 400 and y <= 422:
                    self.manager.cambiar_pantalla(PruebaJugabilidad(self.manager,self.sprites[self.fondo]))

    def render(self):
        surf = pygame.Surface((self.sprites[self.fondo].ancho, self.sprites[self.fondo].alto))
        self.canvas.blit(self.sprites[self.fondo].image, surf.get_rect(topleft=(self.sprites[self.fondo].x,
        self.sprites[self.fondo].y)))
        self.canvas.blit(self.texto_palacio,(340,100))
        self.canvas.blit(self.texto_aeropuerto,(317,200))
        self.canvas.blit(self.texto_plazaD,(335,300))
        self.canvas.blit(self.texto_plazaN,(333,400))
        pygame.display.flip()    

class PruebaJugabilidad(Pantalla):
    def __init__(self,manager,fondo):
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",fondo)
        self.sprites_persona = []
        for i in range(3):
            img = pygame.image.load(os.getcwd() + "/images/personajes/belaunde/belaunde camina"+str(i+1)+".png")
            #img = pygame.transform.scale(img,(100,100))
            self.sprites_persona.append(img)
        self.id = 0
        self.imagen = self.sprites_persona[0]
        self.rect_persona = self.imagen.get_rect()
        self.rect_persona.topleft = (0,400)
        self.izquierda = False
        self.set_nombre_ventana("Prueba de jugabilidad")
        self.handle_events()
        self.update()

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect_persona.y > 265:
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.sprites_persona[self.id],True,False)
            else:
                self.imagen = self.sprites_persona[self.id]
            self.rect_persona.y -= velocidad_v
        if keys[pygame.K_s] and self.rect_persona.y < 465:
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.sprites_persona[self.id],True,False)
            else:
                self.imagen = self.sprites_persona[self.id]
            self.rect_persona.y += velocidad_v
        if keys[pygame.K_a] and self.rect_persona.x > 0:
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = pygame.transform.flip(self.sprites_persona[self.id],True,False)
            self.izquierda = True
            self.rect_persona.x -= velocidad_h
        if keys[pygame.K_d] and self.rect_persona.x < 742:
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = self.sprites_persona[self.id]
            self.izquierda = False
            self.rect_persona.x += velocidad_h

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x, self.sprites["fondo"].y)))
        self.canvas.blit(self.imagen, self.rect_persona)
        pygame.display.flip()

class Login(Pantalla):
    def __init__(self,manager):
        Pantalla.__init__(self,manager)
        self.text = ""
        self.active = False
        coordenadas = {
        "salir": (74,508),
        "jugar": (335,320),
        #"olvide": (597,445),
        "registrar": (597,405),
        "creditos": (597,511)}

        self.set_nombre_ventana("Login")

        #este es el fondo
        self.sprites["background"] = Fondo("login1")

        #botones del login
        for nom,cor in coordenadas.items():
            self.sprites[nom] = Boton(nom,cor)
        
        #self.sprites["olvide"].alto = 40
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #self.eventos["Salir"]=True
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                salir_rect = self.sprites["salir"].image.get_rect()
                salir_rect.topleft = (self.sprites["salir"].x,self.sprites["salir"].y)
                jugar_rect = self.sprites["jugar"].image.get_rect()
                jugar_rect.topleft = (self.sprites["jugar"].x,self.sprites["jugar"].y)
                if input_box.collidepoint(event.pos):
                    self.active = True
                elif salir_rect.collidepoint(event.pos):
                    pygame.quit(); sys.exit()
                elif jugar_rect.collidepoint(event.pos):
                    if self.text != "":
                        apodo = self.text
                        self.manager.cambiar_pantalla(ListaEscenarios(self.manager))
                else:
                    self.active = False
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if len(self.text) < 14:
                            self.text += event.unicode
    def render(self):
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho, sprite.alto))
            self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        
        pygame.draw.rect(self.canvas,font_background,input_box,0)
        txt_surface = font.render(self.text, True, font_color)
        self.canvas.blit(txt_surface, (input_box.x+3, input_box.y+3))
        pygame.display.flip()
