from cgitb import text
from curses import window
from time import sleep
import tkinter
from tkinter import CENTER, INSERT, Button, Entry, Label, scrolledtext
from tkinter import ttk
from ttkthemes import ThemedTk


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math
import pygame
from pygame.locals import *
from sys import exit

var_rec = False
posx_init_robo = 0
posy_init_robo = 0

def enviadados(): #Função que é chamada ao clicar no Botão Enviar
    global var_rec, posx_init_robo, posy_init_robo, window
    
    posx_init_robo = float(entradax.get())
    posy_init_robo = float(entraday.get())
    
    var_rec = True
    window.quit()



#Funçoes de gráficos#

window = tkinter.Tk()
window.title("Posições do robô")
window.config(bg='black')
window.geometry("800x600")

entradax = Entry(window, width=5)
entradax.place(anchor=CENTER, relx=0.48, rely= 0.1)
entradax.insert(0, "X")

entraday = Entry(window, width=5)
entraday.place(anchor=CENTER, relx=0.52, rely= 0.1)
entraday.insert(0, "Y")

botaoenvia = Button(window, text="Enviar", width=10, bg="gray", fg="black", command=enviadados)
botaoenvia.place(anchor=CENTER, relx=0.5, rely=0.15)

window.mainloop()

def grafico(x=0, y=0, titulo="Gráfico", cor='blue', xlabel="CX", ylabel="CY"):
        plt.show(block=False)
        figure = plt.figure(figsize=(6, 4.5), dpi=100)
        figure.add_subplot(111).plot(x, y, color=cor)
        chart = FigureCanvasTkAgg(figure, janela)
        chart.get_tk_widget().place(anchor=CENTER, relx=0.5, rely=0.55)
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.close("all")

def grafico1():
    grafico(posx_bola, posy_bola, "Trajetória da Bola", 'red', "Px", "Py")

def grafico2():
    grafico(tempo_robo, posx_bola, "Posição(x) da Bola", 'blue', "t/s", "x")

def grafico3():
    grafico(tempo_robo, posy_bola, "Posição(y) da Bola", 'green', "t/s", "y")

def grafico4():
    grafico(tempo_robo, velx_bola, "Velocidade(x) da Bola", 'green', "t/s", "y")

def grafico5():
    grafico(tempo_robo, vely_bola, "Velocidade(y) da Bola", 'green', "t/s", "y")

def grafico6():
    grafico(tempo_robo, acelx_bola, "Aceleracao(x) da Bola", 'green', "t/s", "y")

def grafico7():
    grafico(tempo_robo, acely_bola, "Aceleracao(y) da Bola", 'green', "t/s", "y")

def grafico8():
    grafico(posx_robo, posy_robo, "Trajetoria do robo", 'purple', "x", "y")

def grafico9():
    grafico(tempo_robo, posx_robo, "Posição(x) do Robô", 'red', "t/s", "x")

def grafico10():
    grafico(tempo_robo, posy_robo, "Posição(y) do Robo", 'green', "t/s", "y")

def grafico11():
    grafico(tempo_robo, velx_robo, "Velocidade(x) do Robo", 'green', "t/s", "v(x)")

def grafico12():
    grafico(tempo_robo, vely_robo, "Velocidade(y) do Robo", 'green', "t/s", "v(y)")

def grafico13():
    grafico(tempo_robo, acelx_robo, "Aceleracao(x) do Robo", 'green', "t/s", "a(x)")

def grafico14():
    grafico(tempo_robo, acely_robo, "Aceleracao(y) do Robo", 'green', "t/s", "a(y)")

def grafico15():
    grafico(tempo_robo, distancias, "Distancia entre o robo e a bola", 'red', "t/s", "m")




def anim():
    pygame.init()
    largura = 900
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    relogio = pygame.time.Clock()

    while True:
        if robo.i >= len(posx_robo)-1:
            break
        relogio.tick(60)
        tela.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        todas_as_sprites.draw(tela)
        todas_as_sprites.update()

        # des_robo = pygame.draw.rect(tela, (255,0,0), (100*posx_robo[robo.i], -100*posy_robo[robo.i]+altura, (180/1000)*100, (180/1000)*100))
        des_bola = pygame.draw.circle(tela, (255,255,255), (100*pos_x[robo.i], -100*pos_y[robo.i]+altura), 5)

        

        robo.i+=1
        pygame.display.update()






# Criação da Janela + Interface #
if var_rec == True:
    janela = tkinter.Tk()
    janela.title("Projeto Ora Bolas")
    janela.config(bg='black')
    janela.geometry("1200x600")

# campo_pos = scrolledtext.ScrolledText(janela, width=95, height=4)
# campo_pos.place(relx=0.5, rely=0.93, anchor=CENTER)

botao1 = Button(janela, text="Trajetória bola", width=10, bg="red", fg='white', command=grafico1)
botao1.place(anchor=CENTER, relx=0.1, rely=0.05)

botao2 = Button(janela, text="Pos(x) da bola", width=10, bg="blue", fg='white', command=grafico2)
botao2.place(anchor=CENTER, relx=0.2, rely=0.05)

botao3 = Button(janela, text="Pos(y) da bola", width=10, bg="green", fg='white', command=grafico3)
botao3.place(anchor=CENTER, relx=0.3, rely=0.05)

botao4 = Button(janela, text="Velocidade(x) da Bola", width=10, bg="purple", fg="white", command=grafico4)
botao4.place(anchor=CENTER, relx=0.4, rely=0.05)

botao5 = Button(janela, text="Velocidade(y) da Bola", width=10, bg="purple", fg="white", command=grafico5)
botao5.place(anchor=CENTER, relx=0.5, rely=0.05)

botao6 = Button(janela, text="Aceleracao(x) da Bola", width=10, bg="purple", fg="white", command=grafico6)
botao6.place(anchor=CENTER, relx=0.6, rely=0.05)

botao7 = Button(janela, text="Aceleracao(y) da Bola", width=10, bg="purple", fg="white", command=grafico7)
botao7.place(anchor=CENTER, relx=0.7, rely=0.05)

botao8 = Button(janela, text="Trajetoria robo", width=10, bg="purple", fg="white", command=grafico8)
botao8.place(anchor=CENTER, relx=0.8, rely=0.05)

botao9 = Button(janela, text="Pos(x) do Robo", width=10, bg="purple", fg="white", command=grafico9)
botao9.place(anchor=CENTER, relx=0.9, rely=0.05)

botao10 = Button(janela, text="Pos(y) do robo", width=10, bg="purple", fg="white", command=grafico10)
botao10.place(anchor=CENTER, relx=0.1, rely=0.09)

botao11 = Button(janela, text="Velocidade (x) do robo", width=10, bg="red", fg='white', command=grafico11)
botao11.place(anchor=CENTER, relx=0.2, rely=0.09)

botao12 = Button(janela, text="Velocidade (y) do robo", width=10, bg="blue", fg='white', command=grafico12)
botao12.place(anchor=CENTER, relx=0.3, rely=0.09)

botao13 = Button(janela, text="Aceleracao (x) do robo", width=10, bg="green", fg='white', command=grafico13)
botao13.place(anchor=CENTER, relx=0.4, rely=0.09)

botao14 = Button(janela, text="Aceleracao (y) do robo", width=10, bg="purple", fg="white", command=grafico14)
botao14.place(anchor=CENTER, relx=0.5, rely=0.09)

botao15 = Button(janela, text="Animacao", width=10, bg="purple", fg="white", command=anim)
botao15.place(anchor=CENTER, relx=0.6, rely= 0.09)

botao16 = Button(janela, text="Distancia", width=10, bg="red", fg="blue", command=grafico15)
botao16.place(anchor=CENTER, relx=0.7, rely=0.09)

# texto = Label(janela, text="Coordenadas do robô", bg="white", fg="black", )
# texto.place(anchor=CENTER, relx=0.5, rely= 0.05)

# entradax = Entry(window, width=5, text="x")
# entradax.place(anchor=CENTER, relx=0.48, rely= 0.1)
# entradax.insert(0, "X")

# entraday = Entry(window, width=5,text="y")
# entraday.place(anchor=CENTER, relx=0.52, rely= 0.1)
# entraday.insert(0, "Y")

# botaoenvia = Button(window, text="Enviar", width=10, bg="gray", fg="black", command=enviadados)
# botaoenvia.place(anchor=CENTER, relx=0.5, rely=0.15)

# Criação de classes e funções #

class Campo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_campo = []
        self.sprite_campo.append(pygame.image.load('campo.png'))
        self.image = self.sprite_campo[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0
    
    def update(self):
        self.image = self.sprite_campo[0]

class Robo(pygame.sprite.Sprite):
    def __init__(self, posx_init, posy_init):
        pygame.sprite.Sprite.__init__(self)
        self.distancia = 0
        self.sprite_robo = []
        self.angulo = 0
        self.sprite_robo.append(pygame.image.load('robo1.png'))
        self.image = self.sprite_robo[0]
        
        # self.image = pygame.transform.scale(self.image, (18*10, 18*10))
        self.rect = self.image.get_rect()
        self.rect.center = (100*posx_init, -100*posy_init+600)
        #variaveis de aceleracao normal, no eixo x e y
        self.aceleracao = 0
        self.ax = 0
        self.ay = 0
        #variaveis de velocidade no eixo x e y
        self.velx = 0
        self.vely = 0
        #variaveis de posicao
        self.posy = posy_init
        self.posx = posx_init
        #indice pra acessar as listas
        self.i = 0

    def update(self):
        self.rect.center = (100*posx_robo[robo.i], -100*posy_robo[robo.i]+600)
        self.image = self.sprite_robo[0]
        
        self.image = pygame.transform.rotate(self.image, angulos_robo[robo.i])
        # self.image = pygame.transform.scale(self.image, (18*10, 18*10))
    
    def perseguir(self):
        #multiplica a aceleracao por 20 milésimos de segundo pq esse é o tempo de cada posicao da bola
        
        #encontra o delta x 
        self.deltax = abs(pos_x[self.i] - self.posx)**2
        
        #encontra o delta y
        self.deltay = abs(pos_y[self.i] - self.posy)**2
        
        #soma os deltas pra encontrar a distancia entre o robo e a bola
        somaDeltas = (self.deltax) + (self.deltay)
        self.distancia = math.sqrt(somaDeltas)
        
        
        #encontra o cos e seno
        self.cos = (pos_x[self.i] - self.posx)/self.distancia
        self.sen = (pos_y[self.i] - self.posy)/self.distancia
        self.angulo = math.degrees(math.atan(self.sen/self.cos))
        
        


        #multiplica a aceleracao pelo cos e o seno pra encontrar os componentes do vetor de aceleracao
        self.velx = self.cos*0.056
        self.vely = self.sen*0.056

        if self.distancia < 1:
            
            self.velx -= 0.005*(1/self.distancia)
            self.vely -= 0.005*(1/self.distancia)
            
        #essas estruturas condicionais servem pra impedir que a velocidade ultrapasse a velocidade final de 2.8m/s
        # if (2.8*tempo[1] >= (self.velx + self.ax)):
        #     self.velx = self.ax
        
        # elif (-2.8*tempo[1] <= (self.velx + self.ax)):
        #     self.velx = self.ax
        
        # elif (2.8*tempo[1] < (self.velx + self.ax)):
        #     self.velx = 2.8*tempo[1]
        
        # elif (-2.8*tempo[1] > (self.velx + self.ax)):
        #     self.velx = -1*(2.8*tempo[1])
        
        # if (2.8*tempo[1] >= (self.vely + self.ay)):
        #     self.vely = self.ay
        
        # elif (-2.8*tempo[1] <= (self.vely + self.ay)):
        #     self.vely = self.ay
        
        # elif (2.8*tempo[1] < (self.vely + self.ay)):
        #     self.vely = 2.8*tempo[1]
        
        # elif (-2.8*tempo[1] > (self.vely + self.ay)):
        #     self.vely = -1*(2.8*tempo[1])
        
        #soma a velocidade nas posicoes
        self.posx += self.velx
        self.posy += self.vely

todas_as_sprites = pygame.sprite.Group()


robo = Robo(posx_init_robo, posy_init_robo)
campo = Campo()
todas_as_sprites.add(campo)
todas_as_sprites.add(robo)

posx_robo = []
posy_robo = []
velx_robo = []
vely_robo = []
acelx_robo = []
acely_robo = []
angulos_robo = []
posx_bola = []
posy_bola = []
velx_bola = []
vely_bola = []
acelx_bola = []
acely_bola = []
distancias = []


# Código (Lógica) responsável pelos dados #

trajetoria = open('trajetoriaMeio.txt', 'r')
lista_pos = []
pos_x = []
pos_y = []
tempo = []
tempo_robo = []

for line in trajetoria:
    linha = line.replace("\t"," ").replace("\n"," ").replace(",", ".")
    linha2 = linha.split(" ")
    lista_pos.append(linha)
    tempo.append(linha2[0])
    pos_x.append((linha2[1]))
    pos_y.append((linha2[2]))

del pos_y[0], pos_x[0], tempo[0]

for indice in range(len(pos_x)):
    pos_x[indice] = float(pos_x[indice])
    pos_y[indice] = float(pos_y[indice])
    tempo[indice] = float(tempo[indice])

trajetoria.close()


posx_robo = []
posy_robo = []

#essa estrutura de repeticao vai passando as posicoes que o robo toma pra dentro de listas
while True:
    posx_bola.append(pos_x[robo.i])
    posy_bola.append(pos_y[robo.i])
    velx_bola.append((pos_x[robo.i]-pos_x[robo.i-1])/((tempo[robo.i])-(tempo[robo.i-1])))
    vely_bola.append((pos_y[robo.i]-pos_y[robo.i-1])/((tempo[robo.i])-(tempo[robo.i-1])))
    acelx_bola.append((velx_bola[robo.i]-velx_bola[robo.i-1])/(tempo[robo.i]-tempo[robo.i-1]))
    acely_bola.append((vely_bola[robo.i]-vely_bola[robo.i-1])/(tempo[robo.i]-tempo[robo.i-1]))

    posx_robo.append(robo.posx)
    posy_robo.append(robo.posy)
    velx_robo.append((posx_robo[robo.i]-posx_robo[robo.i-1])/((tempo[robo.i])-(tempo[robo.i-1])))
    vely_robo.append((posy_robo[robo.i]-posy_robo[robo.i-1])/((tempo[robo.i])-(tempo[robo.i-1])))
    acelx_robo.append(velx_robo[robo.i]/(tempo[robo.i]))
    acely_robo.append(vely_robo[robo.i]/(tempo[robo.i]))

    distancias.append(robo.distancia)
    
    tempo_robo.append(tempo[robo.i])
    if robo.posx > pos_x[robo.i]:
        robo.angulo -= 180
    angulos_robo.append(robo.angulo)
    
    robo.perseguir()
    robo.i+=1
    
    if ((robo.posx + 0.09 >= pos_x[robo.i]-(2.1/200) and robo.posx - 0.09 <= pos_x[robo.i]+(21/2000)) and (robo.posy + 0.09 >= pos_y[robo.i]-(21/2000) and robo.posy - 0.09 <= pos_y[robo.i]+(21/2000))):
        
        break

    if robo.i >= len(pos_x)-1:
        break

# for line in lista_pos:
#     campo_pos.insert(INSERT, line)

print(robo.posx, robo.posy, pos_x[robo.i], pos_y[robo.i], tempo[robo.i], robo.velx/0.056, robo.vely/0.056)

robo.i = 0


janela.mainloop()
