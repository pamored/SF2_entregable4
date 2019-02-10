import pygame
import sys
import os

pygame.font.init()

font = pygame.font.SysFont("Verdana", 22)
font_color = (255,255,255)
font_background = (0,0,0)
input_box = pygame.Rect(317,293,165,21)

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen, pos=[10,10], size=(100,100)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + ".png")
        self.image = pygame.transform.scale(self.image, size)
        
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]

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
    def __init__(self):
        #self.manager = manager
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
        #for nombre in self.eventos:
        #    self.eventos[nombre]=False
            #print(self.eventos[nombre])
        pass 

    def render(self):
        for nombre, sprite in self.sprites.items():
            surf = pygame.Surface((sprite.ancho, sprite.alto))
            self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()
    
class Texto:
    def __init__(self,texto,id):
        self.texto = texto
        self.id = id

class ListaEscenarios(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #Imagenes a usar
        nom_fondos = ["fondo","palacio","aeropuerto","",""]
        fondo = nom_fondos[0]
        fuente = pygame.font.SysFont("Arial",22)
        texto_palacio = fuente.render("palacio",0,(244,255,250))
        texto_aeropuerto = fuente.render("aeropuerto",0,(244,255,250))
        texto_palacio = fuente.render("palacio",0,(244,255,250))
        texto_palacio = fuente.render("palacio",0,(244,255,250))
        for nom in nom_fondos:
            self.agregar_sprite(nom,Fondo(nom))



        self.set_nombre_ventana("Escoger Escenario")
        self.handle_events()
        self.update()

    def handle_events(self):
        x,y = pygame.mouse.get_pos()

    def render(self):
        surf = pygame.Surface((fondo.ancho, fondo.alto))
        self.canvas.blit(sprite.image, surf.get_rect(topleft=(sprite.x, sprite.y)))
        pygame.display.flip()    

class Pantalla2(Pantalla):
    def __init__(self):
        Pantalla.__init__(self)
        #Imagenes a usar
        personaje = "hero"
        fondo = "Fondo2"        
        p1 = Personaje(imagen = personaje, pos=[110,110])        
        f1 = Fondo(fondo = fondo, pos = [100, 100])        

        self.set_nombre_ventana("Prueba de jugabilidad")
        self.handle_events()
        self.update()

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
                if input_box.collidepoint(event.pos):
                    self.active = True
                elif salir_rect.collidepoint(event.pos):
                    pygame.quit(); sys.exit()
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





# Para crear una pantalla extra (o la de login) se crea una clase como Ejemplo pantalla y se llama 
# desde game.py en la clase ScreenManager

""" class Login(Pantalla):
    def __init__(self, canvas):
        Pantalla.__init__(self, canvas)
        p1 = Personaje("images/personajes/hero/hero1.png")
        self.agregar_sprite("hero1",p1)
        self.handle_events()
        self.update() """

    #def handle_events(self):
       # pass
    #def update(self):
        #self.sprites["hero1"].x += 100