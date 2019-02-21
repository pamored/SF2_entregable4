import pygame, random, sys, os
from red import Red

pygame.font.init()

font = pygame.font.SysFont("Verdana", 18)
font_color = (255,255,255)
font_background = (0,0,0)
input_box = pygame.Rect(317,291,164,21)

fondo = ""
apodo = ""
personaje1 = ""
personaje2 = ""

velocidad_v = 3
velocidad_h = 5

class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen,num,enemigo=None):
        pygame.sprite.Sprite.__init__(self)
        self.persona_viva = []
        for i in range(3):
            self.persona_viva.append(pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + " camina"+(num+1)+".png"))
        self.image_rect = self.persona_viva[0].get_rect()
        self.image_rect.topleft = (0,400) if num == "jugador1" else (800-self.image_rect.width,400)
        self.tomate = Bala("tomate")
        self.vida = 100
        self.enemigo = enemigo

    def bajar_vida(self,bala):
        if bala == "tomate":
            self.vida -= 5
        else:
            self.vida -= 15

class Bala(pygame.sprite.Sprite):
    def __init__(self,bala):
        self.bala = pygame.image.load(os.getcwd()+"images/disparos/"+bala+".png")
        self.rect_bala = self.bala.get_rect()
        self.visible = False

    def disparo(self):
        pass

class Fondo(pygame.sprite.Sprite):
    def __init__(self, fondo, pos=[0,0], size=(800,600)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/fondos/" + fondo + ".png")
        self.image = pygame.transform.scale(self.image, size)
        self.x = pos[0]
        self.y = pos[1]
        self.ancho = size[0]
        self.alto = size[1]
        self.id = fondo

class Pantalla:
    def __init__(self,manager):
        self.manager = manager
        self.sprites = {}
        self.canvas = pygame.display.set_mode((800, 600))

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
        self.lista_escenarios = ["","plaza","ulima","","nazca","machu","","aeropuerto","plaza"]
        self.ubicaciones = [(17,73),(202,74),(391,77),(581,77),(16,230),(200,231),(389,234),(582,235),(14,402)]
        self.id = None
        self.agregar_sprite("fondo",Fondo("escenarios"))
        self.set_nombre_ventana("Escoger Escenario")
        #self.rect_pos = (0,0)
        #self.rect = pygame.draw.rect(self.canvas,(255,127,80),(self.rect_pos,))
        self.handle_events()
        self.update()

    def handle_events(self):
        global fondo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                """if x >=17 and x <= 178 and y >= 73 and y <= 196:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 74 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 400 and y >= 77 and y <= 322:
                    self.id = 0
                elif x >=300 and x <= 480 and y >= 77 and y <= 422:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 230 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 231 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 234 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 235 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 402 and y <= 222:
                    self.id = 0
                elif x >=300 and x <= 500 and y >= 200 and y <= 222:
                    self.id = random.randint(0,9)
                elif x >=300 and x <= 500 and y >= 200 and y <= 222:
                    if self.id != None:
                        fondo = self.lista_escenarios[self.id]
                        """

    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x,
        self.sprites["fondo"].y)))
        if self.id != None:
            pygame.draw.rect(self.canvas,(255,127,80),(self.ubicaciones[self.id][0],self.ubicaciones[self.id][1],80,150),2)

        pygame.display.flip()    

class ListaPersonajes(Pantalla):
    def __init__(self,manager):
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo("jugadores"))
        #Imagenes a usar
        self.nom_personajes = ["alan","belaunde","fujimori","grau","jose","ollanta","pierola","ppk","riva","toledo"]
        self.ubicaciones = [(56,134),(144,134),(232,134),(320,134),(408,134),(0,342),(85,342),(175,342),(263,342),(352,342)]
        self.id = None

        self.set_nombre_ventana("Escoger Personaje")
        self.handle_events()
        self.update()

    def handle_events(self):
        global personaje
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                print (x)
                if x >=56 and x <= 134 and y >= 135 and y <= 285:
                    self.id = 0
                elif x >=144 and x <= 222 and y >= 135 and y <= 285:
                    self.id = 1
                elif x >=232 and x <= 310 and y >= 135 and y <= 285:
                    self.id = 2
                elif x >=320 and x <= 398 and y >= 135 and y <= 285:
                    self.id = 3
                elif x >=408 and x <= 486 and y >= 135 and y <= 285:
                    self.id = 4
                elif x >=0 and x <= 77 and y >= 342 and y <= 492:
                    self.id = 5
                elif x >=85 and x <= 165 and y >= 342 and y <= 492:
                    self.id = 6
                elif x >=175 and x <= 255 and y >= 342 and y <= 492:
                    self.id = 7
                elif x >=263 and x <= 342 and y >= 342 and y <= 492:
                    self.id = 8
                elif x >=352 and x <= 432 and y >= 342 and y <= 492:
                    self.id = 9
                elif x >=208 and x <= 375 and y >= 544 and y <= 600:
                    self.id = random.randint(0,9)
                elif x >=30 and x <= 199 and y >= 544 and y <= 600:
                    if self.id != None:
                        personaje = self.nom_personajes[self.id]
                        self.manager.cambiar_pantalla(Juego(self.manager))
                else:
                    self.id = None

    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x,
        self.sprites["fondo"].y)))
        if self.id != None:
            pygame.draw.rect(self.canvas,(255,127,80),(self.ubicaciones[self.id][0],self.ubicaciones[self.id][1],80,150),2)
        pygame.display.flip()

class Juego(Pantalla):
    def __init__(self,manager):
        self.net = Red()
        global personaje1, personaje2, fondo
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo(fondo))
        jugador = "jugador1" if self.net.id == "0" else "jugador2"
        jugador2 = "jugador2" if jugador == "jugador1" else "jugador1"
        personaje2 = self.parse_data(self.net.send(str(self.net.id) + ":" + personaje1))
        self.jugador1 = Jugador(personaje1,jugador)
        self.jugador2 = Jugador(personaje2,jugador2)
        self.jugador1.enemigo = self.jugador2
        self.jugador2.enemigo = self.jugador1

        self.id = 0
        self.imagen = self.jugador1.persona_viva[0]
        self.rect_persona = self.jugador1.image_rect
        self.izquierda = False if self.net.id == "0" else True
        self.set_nombre_ventana("Jugando")
        self.handle_events()
        self.update()

    @staticmethod
    #Los une y lo hace por cada host
    def parse_data(data):
        try:
            d = data.split(":")[1]
            return d
        except:
            return ""

    def handle_events(self):
        global personaje
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect_persona.y > (400-self.rect_persona.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.jugador1.persona_viva[self.id],True,False)
            else:
                self.imagen = self.jugador1.persona_viva[self.id]
            self.rect_persona.y -= velocidad_v
        if keys[pygame.K_s] and self.rect_persona.y < (600-self.rect_persona.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.jugador1.persona_viva[self.id],True,False)
            else:
                self.imagen = self.jugador1.persona_viva[self.id]
            self.rect_persona.y += velocidad_v
        if keys[pygame.K_a] and self.rect_persona.x > 0:
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = pygame.transform.flip(self.jugador1.persona_viva[self.id],True,False)
            self.izquierda = True
            self.rect_persona.x -= velocidad_h
        if keys[pygame.K_d] and self.rect_persona.x < (800-self.rect_persona.width):
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = self.jugador1.persona_viva[self.id]
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

        self.set_nombre_ventana("Login")

        #este es el fondo
        self.sprites["background"] = Fondo("login")
        
    
    def handle_events(self):
        for event in pygame.event.get():
            global apodo
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if input_box.collidepoint(event.pos):
                    self.active = True
                elif x>=74 and x<=204 and y>=508 and y<=537:
                    pygame.quit(); sys.exit()
                elif x>=335 and x<=465 and y>=320 and y<=350:
                    if self.text != "":
                        apodo = self.text
                        self.manager.cambiar_pantalla(ListaEscenarios(self.manager))
                else:
                    self.active = False
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        if self.text != "":
                            apodo = self.text
                            self.manager.cambiar_pantalla(ListaEscenarios(self.manager))
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
