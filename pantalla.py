import pygame, random, sys, os, time
from red import Red
#from cliente import listar, eliminar, insertar, actualizar

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
    def __init__(self, imagen,num):
        pygame.sprite.Sprite.__init__(self)
        self.persona_viva = []
        for i in range(3):
            self.persona_viva.append(pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + " camina"+str(i+1)+".png"))
        self.image_rect = self.persona_viva[0].get_rect()
        self.image_rect.topleft = (0,400) if num == "jugador1" else (800-self.image_rect.width,400)
        self.vida = 100
        self.score = 0

    def bajar_vida(self):
            self.vida -= 8

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
        self.lista_escenarios = ["unmsm","plaza","ulima","heroes","nazca","machu","bolognesi","aeropuerto","congreso"]
        self.ubicaciones = [(17,73),(202,74),(391,77),(581,77),(16,230),(200,231),(389,234),(582,235),(14,402)]
        self.id = None
        self.agregar_sprite("fondo",Fondo("escenarios"))
        self.set_nombre_ventana("Escoger Escenario")
        self.handle_events()
        self.update()

    def handle_events(self):
        global fondo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x >=17 and x <= 178 and y >= 73 and y <= 193:
                    self.id = 0
                elif x >=202 and x <= 362 and y >= 74 and y <= 194:
                    self.id = 1
                elif x >=391 and x <= 551 and y >= 77 and y <= 197:
                    self.id = 2
                elif x >=581 and x <= 741 and y >= 77 and y <= 197:
                    self.id = 3
                elif x >=16 and x <= 177 and y >= 230 and y <= 350:
                    self.id = 4
                elif x >=200 and x <= 360 and y >= 231 and y <= 351:
                    self.id = 5
                elif x >=389 and x <= 549 and y >= 234 and y <= 354:
                    self.id = 6
                elif x >=582 and x <= 742 and y >= 235 and y <= 355:
                    self.id = 7
                elif x >=14 and x <= 174 and y >= 402 and y <= 522:
                    self.id = 8
                elif x >=432 and x <= 591 and y >= 519 and y <= 570:
                    self.id = random.randint(0,8)
                elif x >=618 and x <= 785 and y >= 523 and y <= 564:
                    if self.id != None:
                        fondo = self.lista_escenarios[self.id]
                        self.manager.cambiar_pantalla(ListaPersonajes(self.manager))
                        
    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x,
        self.sprites["fondo"].y)))
        if self.id != None:
            pygame.draw.rect(self.canvas,(255,127,80),(self.ubicaciones[self.id][0],self.ubicaciones[self.id][1],160,120),2)
        pygame.display.flip()    

class ListaPersonajes(Pantalla):
    def __init__(self,manager):
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo("jugadores"))
        #Imagenes a usar
        self.nom_personajes = ["alan","toledo","fujimori","ollanta","ppk","grau","jose","pierola","belaunde","riva"]
        self.ubicaciones = [(56,134),(144,134),(232,134),(320,134),(408,134),(0,342),(85,342),(175,342),(263,342),(352,342)]
        self.id = None

        self.set_nombre_ventana("Escoger Personaje")
        self.handle_events()
        self.update()

    def handle_events(self):
        global personaje1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
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
                        personaje1 = self.nom_personajes[self.id]
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
        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.getcwd()+"/sonidos/fondo_batalla.mp3")
        pygame.mixer.music.play(-1)
        self.net = Red()
        global personaje1, personaje2, fondo
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo(fondo))
        jugador = "jugador1" if self.net.id == "0" else "jugador2"
        self.jugador2 = "jugador2" if jugador == "jugador1" else "jugador1"
        self.jugador1 = Jugador(personaje1,jugador)

        self.id = 0
        self.ide = 0
        self.izquierda = False if self.net.id == "0" else True
        self.op_izquierda = True if self.izquierda == False else False
        personaje2 = self.jugador_data(self.net.send(
                str(self.net.id)+":"+ str(self.jugador1.image_rect.x)+","+str(self.jugador1.image_rect.y)))
        if personaje2 != "":
            self.jugador2 = Jugador(personaje2,self.jugador2)
        else:
            self.jugador2 = None
        
        self.set_nombre_ventana("Jugando")
        self.handle_events()
        self.update()
        #self.num = insertar(apodo,0)

    
    @staticmethod
    def jugador_data(data):
        try:
            return data.split(":")[1].split(",")[2]
        except:
            return ""

    @staticmethod
    def parse_data(data):
        try:
            d = data.split(":")[1].split(",")
            bol = True if d[3] == "si" else False
            return int(d[0]), int(d[1]), d[2], bol, int(d[4]), int(d[5])
        except:
            return 0,0,"",True,0,100

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.jugador1.image_rect.y > (400-self.jugador1.image_rect.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.jugador1.image_rect.y -= velocidad_v
        if keys[pygame.K_s] and self.jugador1.image_rect.y < (600-self.jugador1.image_rect.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.jugador1.image_rect.y += velocidad_v
        if keys[pygame.K_a] and self.jugador1.image_rect.x > 0:
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.izquierda = True
            self.jugador1.image_rect.x -= velocidad_h
        if keys[pygame.K_d] and self.jugador1.image_rect.x < (800-self.jugador1.image_rect.width):
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.izquierda = False
            self.jugador1.image_rect.x += velocidad_h

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.jugador2 != None:
                        if self.jugador1.image_rect.colliderect(self.jugador2.image_rect) and self.jugador1.image_rect.y >= (self.jugador2.image_rect.y-10) and self.jugador1.image_rect.y <= (self.jugador2.image_rect.y+10):
                            s = pygame.mixer.Sound(os.getcwd() + "/sonidos/golpe.mp3")
                            pygame.mixer.Sound.play(s)
                            self.jugador2.bajar_vida()
                            self.jugador1.score += 5
                        

    def determinar_fin(self):
        if self.jugador1.vida <= 0:
            time.sleep(10)
            fuente = pygame.font.SysFont("Verdana", 30)
            texto = fuente.render("PERDISTE, "+apodo,0,(0,0,0))
            self.canvas.blit(texto,(350,0))
            time.sleep(10)
            self.manager.cambiar_pantalla(Login(self.manager))
            #print(actualizar(self.num,apodo,self.jugador1.score))
        elif self.jugador2.vida <= 0:
            fuente = pygame.font.SysFont("Verdana", 30)
            texto = fuente.render("GANASTE, "+apodo,0,(0,0,0))
            self.canvas.blit(texto,(350,0))
            time.sleep(10)
            self.manager.cambiar_pantalla(Login(self.manager))
            #print(actualizar(self.num,apodo,self.jugador1.score))

    def update(self):
        global personaje2
        izq = "si" if self.izquierda == True else "no"
        vida = 100 if self.jugador2 == None else self.jugador2.vida
        x,y,personaje2,izquierda,self.ide,self.jugador1.vida = self.parse_data(self.net.send(
                str(self.net.id)+":"+str(self.jugador1.image_rect.x)+","+str(self.jugador1.image_rect.y)+","+personaje1+","+izq+","+str(self.id)+","+str(vida)))
        if self.jugador2 == None and personaje2 != "":
            self.jugador2 = Jugador(personaje2,self.jugador2)
        elif personaje2 != "":
            self.jugador2.image_rect.x = x
            self.jugador2.image_rect.y = y
        self.op_izquierda = izquierda

    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x, self.sprites["fondo"].y)))
        if self.izquierda == True:
            self.canvas.blit(pygame.transform.flip(self.jugador1.persona_viva[self.id],True,False),self.jugador1.image_rect)
        else:
            self.canvas.blit(self.jugador1.persona_viva[self.id], self.jugador1.image_rect)
        if self.op_izquierda == True and self.jugador2 != None:
            self.canvas.blit(pygame.transform.flip(self.jugador2.persona_viva[self.ide],True,False),self.jugador2.image_rect)
        elif self.jugador2 != None:
            self.canvas.blit(self.jugador2.persona_viva[self.ide], self.jugador2.image_rect)
        if self.jugador2 != None:
            self.determinar_fin()
        pygame.display.flip()

class Login(Pantalla):
    def __init__(self,manager):
        #pygame.mixer.music.load(os.getcwd()+"/sonidos/fondo_inicio.mp3")
        #pygame.mixer.music.play(-1)
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
