import pygame
import sys
import os

pygame.font.init()

font = pygame.font.SysFont("Verdana", 18)
font_color = (255,255,255)
font_background = (0,0,0)
input_box = pygame.Rect(317,291,164,21)

fondo = ""
apodo = ""
personaje = ""

velocidad_v = 3
velocidad_h = 5

class Personaje(pygame.sprite.Sprite):
    def __init__(self, imagen, num, pos=[10,10]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.getcwd() + "/images/personajes/" + imagen + "/" + imagen + " camina"+str(num)+".png")
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (pos)
        self.id = imagen

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
        global fondo
        fondo = "fondo"
        fuente = pygame.font.SysFont("Arial",22)
        self.textos = []
        self.textos.append(fuente.render("Palacio de Gobierno",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Aeropuerto Jorge Chavez",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Plaza de Armas (Dia)",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Plaza de Armas(Noche)",0,(166,166,192),(27,27,113)))
        for nom in nom_fondos:
            self.agregar_sprite(nom,Fondo(nom))

        self.set_nombre_ventana("Escoger Escenario")
        self.handle_events()
        self.update()

    def handle_events(self):
        global fondo
        x,y = pygame.mouse.get_pos()
        if x >=300 and x <= 448 and y >= 100 and y <= 122:
            fondo = self.sprites["palacio"].id
        elif x >=300 and x <= 490 and y >= 200 and y <= 222:
            fondo = self.sprites["aeropuerto"].id
        elif x >=300 and x <= 450 and y >= 300 and y <= 322:
            fondo = self.sprites["plaza(dia)"].id
        elif x >=300 and x <= 472 and y >= 400 and y <= 422:
            fondo = self.sprites["plaza(noche)"].id
        else:
            fondo = "fondo"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if x >=300 and x <= 420 and y >= 100 and y <= 122:
                    self.manager.cambiar_pantalla(ListaPersonajes(self.manager))
                elif x >=300 and x <= 500 and y >= 200 and y <= 222:
                    self.manager.cambiar_pantalla(ListaPersonajes(self.manager))
                elif x >=300 and x <= 400 and y >= 300 and y <= 322:
                    self.manager.cambiar_pantalla(ListaPersonajes(self.manager))
                elif x >=300 and x <= 480 and y >= 400 and y <= 422:
                    self.manager.cambiar_pantalla(ListaPersonajes(self.manager))

    def render(self):
        global fondo
        surf = pygame.Surface((self.sprites[fondo].ancho, self.sprites[fondo].alto))
        self.canvas.blit(self.sprites[fondo].image, surf.get_rect(topleft=(self.sprites[fondo].x,
        self.sprites[fondo].y)))
        for i in range(len(self.textos)):
            self.canvas.blit(self.textos[i],(300,(i+1)*100))
        pygame.display.flip()    

class ListaPersonajes(Pantalla):
    def __init__(self,manager):
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo("fondo"))
        #Imagenes a usar
        nom_personajes = ["alan","belaunde","fujimori","grau","jose","ollanta","pierola","ppk","riva","toledo"]
        fuente = pygame.font.SysFont("Arial",22)
        self.textos = []
        self.textos.append(fuente.render("Alan Garcia",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Fernando Belaunde Terry",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Alberto Fujimori",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Miguel Grau",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("José Domingo Pérez",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Ollanta Humala",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Nicolás de Pierola",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Pedro Pablo Kuczynski",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("José de la Riva Agüero",0,(166,166,192),(27,27,113)))
        self.textos.append(fuente.render("Alejandro Toledo",0,(166,166,192),(27,27,113)))
        for nom in nom_personajes:
            self.agregar_sprite(nom,Personaje(nom,1,[450,250]))

        self.set_nombre_ventana("Escoger Personaje")
        self.handle_events()
        self.update()

    def handle_events(self):
        global personaje
        x,y = pygame.mouse.get_pos()
        if x >=200 and x <= 300 and y >= 50 and y <= 72:
            personaje = self.sprites["alan"].id
        elif x >=200 and x <= 300 and y >= 100 and y <= 122:
            personaje = self.sprites["belaunde"].id
        elif x >=200 and x <= 300 and y >= 150 and y <= 172:
            personaje = self.sprites["fujimori"].id
        elif x >=200 and x <= 300 and y >= 200 and y <= 222:
            personaje = self.sprites["grau"].id
        elif x >=200 and x <= 300 and y >= 250 and y <= 272:
            personaje = self.sprites["jose"].id
        elif x >=200 and x <= 300 and y >= 300 and y <= 322:
            personaje = self.sprites["ollanta"].id
        elif x >=200 and x <= 300 and y >= 350 and y <= 372:
            personaje = self.sprites["pierola"].id
        elif x >=200 and x <= 300 and y >= 400 and y <= 422:
            personaje = self.sprites["ppk"].id
        elif x >=200 and x <= 300 and y >= 450 and y <= 472:
            personaje = self.sprites["riva"].id
        elif x >=200 and x <= 300 and y >= 500 and y <= 522:
            personaje = self.sprites["toledo"].id
        else:
            personaje = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if x >=200 and x <= 300 and y >= 50 and y <= 72:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 100 and y <= 122:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 150 and y <= 172:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 200 and y <= 222:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 250 and y <= 272:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 300 and y <= 322:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 350 and y <= 372:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 400 and y <= 422:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 450 and y <= 472:
                    self.manager.cambiar_pantalla(Juego(self.manager))
                elif x >=200 and x <= 300 and y >= 500 and y <= 522:
                    self.manager.cambiar_pantalla(Juego(self.manager))

    def render(self):
        surf = pygame.Surface((self.sprites["fondo"].ancho, self.sprites["fondo"].alto))
        self.canvas.blit(self.sprites["fondo"].image, surf.get_rect(topleft=(self.sprites["fondo"].x,
        self.sprites["fondo"].y)))
        if personaje != "":
            self.canvas.blit(self.sprites[personaje].image, self.sprites[personaje].image_rect)
        for i in range(len(self.textos)):
            self.canvas.blit(self.textos[i],(200,(i+1)*50))
        pygame.display.flip()

class Juego(Pantalla):
    def __init__(self,manager):
        global personaje, fondo
        Pantalla.__init__(self,manager)
        self.agregar_sprite("fondo",Fondo(fondo))
        sprites_persona = []

        for i in range(3):
            sprites_persona.append(Personaje(personaje,(i+1)))

        self.agregar_sprite(personaje,sprites_persona)
        self.id = 0
        self.imagen = self.sprites[personaje][0].image
        self.rect_persona = self.sprites[personaje][0].image_rect
        self.rect_persona.topleft = (0,400)
        self.izquierda = False
        self.set_nombre_ventana("Prueba de jugabilidad")
        self.handle_events()
        self.update()

    def handle_events(self):
        global personaje
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect_persona.y > (400-self.rect_persona.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.sprites[personaje][self.id].image,True,False)
            else:
                self.imagen = self.sprites[personaje][self.id].image
            self.rect_persona.y -= velocidad_v
        if keys[pygame.K_s] and self.rect_persona.y < (600-self.rect_persona.height):
            self.id += 1
            if self.id > 2:
                self.id = 0
            if self.izquierda:
                self.imagen = pygame.transform.flip(self.sprites[personaje][self.id].image,True,False)
            else:
                self.imagen = self.sprites[personaje][self.id].image
            self.rect_persona.y += velocidad_v
        if keys[pygame.K_a] and self.rect_persona.x > 0:
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = pygame.transform.flip(self.sprites[personaje][self.id].image,True,False)
            self.izquierda = True
            self.rect_persona.x -= velocidad_h
        if keys[pygame.K_d] and self.rect_persona.x < (800-self.rect_persona.width):
            self.id += 1
            if self.id > 2:
                self.id = 0
            self.imagen = self.sprites[personaje][self.id].image
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
        "registrar": (597,405),
        "creditos": (597,511)}

        self.set_nombre_ventana("Login")

        #este es el fondo
        self.sprites["background"] = Fondo("login1")

        #botones del login
        for nom,cor in coordenadas.items():
            self.sprites[nom] = Boton(nom,cor)
        
    
    def handle_events(self):
        for event in pygame.event.get():
            global apodo
            if event.type == pygame.QUIT:
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
