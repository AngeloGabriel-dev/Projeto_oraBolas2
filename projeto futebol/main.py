import tkinter
from tkinter import CENTER, INSERT, Button, scrolledtext
from turtle import pos, update
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math
import pygame
from pygame.locals import *
from sys import exit


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

class Robo:
    def __init__(self, posx_init, posy_init):
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

    def grafico(x, y, titulo="Gráfico", cor='blue', xlabel="CX", ylabel="CY"):
        plt.show(block=False)
        figure = plt.figure(figsize=(6, 4.5), dpi=100)
        figure.add_subplot(111).plot(x, y, color=cor)
        chart = FigureCanvasTkAgg(figure, janela)
        chart.get_tk_widget().place(anchor=CENTER, relx=0.5, rely=0.47)
        plt.title(titulo)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.close("all")
    
    def perseguir(self):
        #multiplica a aceleracao por 20 milésimos de segundo pq esse é o tempo de cada posicao da bola
        self.aceleracao = 2.8*tempo[1]
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

        #multiplica a aceleracao pelo cos e o seno pra encontrar os componentes do vetor de aceleracao
        self.ax = self.cos*self.aceleracao
        self.ay = self.sen*self.aceleracao

        #essas estruturas condicionais servem pra impedir que a velocidade ultrapasse a velocidade final de 2.8m/s
        if (2.8*tempo[1] >= (self.velx + self.ax)):
            self.velx = self.ax
        
        elif (-2.8*tempo[1] <= (self.velx + self.ax)):
            self.velx = self.ax
        
        elif (2.8*tempo[1] < (self.velx + self.ax)):
            self.velx = 2.8*tempo[1]
        
        elif (-2.8*tempo[1] > (self.velx + self.ax)):
            self.velx = -1*(2.8*tempo[1])
        
        if (2.8*tempo[1] >= (self.vely + self.ay)):
            self.vely = self.ay
        
        elif (-2.8*tempo[1] <= (self.vely + self.ay)):
            self.vely = self.ay
        
        elif (2.8*tempo[1] < (self.vely + self.ay)):
            self.vely = 2.8*tempo[1]
        
        elif (-2.8*tempo[1] > (self.vely + self.ay)):
            self.vely = -1*(2.8*tempo[1])
        
        #soma a velocidade nas posicoes
        self.posx += self.velx
        self.posy += self.vely

todas_as_sprites = pygame.sprite.Group()
campo = Campo()
todas_as_sprites.add(campo)

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

        des_robo = pygame.draw.rect(tela, (255,0,0), (100*posx_robo[robo.i], -100*posy_robo[robo.i]+altura, (180/1000)*100, (180/1000)*100))
        des_bola = pygame.draw.rect(tela, (0,255,0), (100*pos_x[robo.i], -100*pos_y[robo.i]+altura, (21/1000)*500, (21/1000)*500))

        

        robo.i+=1
        pygame.display.update()



def grafico1():
    Robo.grafico(pos_x, pos_y, "Trajetória da Bola", 'red', "Px", "Py")


def grafico2():
    Robo.grafico(tempo, pos_x, "Posição(x) da Bola", 'blue')


def grafico3():
    Robo.grafico(tempo, pos_y, "Posição(y) da Bola", 'green')

def grafico4():
    Robo.grafico(posx_robo, posy_robo, "Trajetoria do robo", 'purple')

def grafico5():
    Robo.grafico(tempo_robo, posx_robo, "Posição(x) do Robô", 'red')

def grafico6():
    Robo.grafico(tempo_robo, posy_robo, "Posição(y) do Robo", 'green')


# Criação da Janela + Interface #

janela = tkinter.Tk()

janela.title("Robo artilheiro")

janela.geometry("800x600")

# campo_pos = scrolledtext.ScrolledText(janela, width=95, height=4)
# campo_pos.place(relx=0.5, rely=0.93, anchor=CENTER)

botao1 = Button(janela, text="Gráfico da Trajetória", width=14, bg="red", fg='white', command=grafico1)
botao1.place(anchor=CENTER, relx=0.1, rely=0.05)

botao2 = Button(janela, text="Pos(x) da bola", width=14, bg="blue", fg='white', command=grafico2)
botao2.place(anchor=CENTER, relx=0.25, rely=0.05)

botao3 = Button(janela, text="Pos(y) da bola", width=14, bg="green", fg='white', command=grafico3)
botao3.place(anchor=CENTER, relx=0.4, rely=0.05)

botao4 = Button(janela, text="Trajetoria robo", width=14, bg="purple", fg="white", command=grafico4)
botao4.place(anchor=CENTER, relx=0.55, rely=0.05)

botao5 = Button(janela, text="Pos(x) do Robo", width=14, bg="purple", fg="white", command=grafico5)
botao5.place(anchor=CENTER, relx=0.7, rely=0.05)

botao6 = Button(janela, text="Pos(y) do robo", width=14, bg="purple", fg="white", command=grafico6)
botao6.place(anchor=CENTER, relx=0.85, rely=0.05)

botao7 = Button(janela, text="Animacao", width=14, bg="purple", fg="white", command=anim)
botao7.place(anchor=CENTER, relx=0.5, rely= 0.5)


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


#CRIACAO DO ROBO
robo = Robo(1, 5)

posx_robo = []
posy_robo = []

#essa estrutura de repeticao vai passando as posicoes que o robo toma pra dentro de listas
while True:
    posx_robo.append(robo.posx)
    posy_robo.append(robo.posy)
    tempo_robo.append(tempo[robo.i])
    
    robo.perseguir()
    robo.i+=1
    
    if ((robo.posx + 0.09 >= pos_x[robo.i]-(21/2000) and robo.posx - 0.09 <= pos_x[robo.i]+(21/2000)) and (robo.posy + 0.09 >= pos_y[robo.i]-(21/2000) and robo.posy - 0.09 <= pos_y[robo.i]+(21/2000))):
        break

    if robo.i >= len(pos_x)-1:
        break

# for line in lista_pos:
#     campo_pos.insert(INSERT, line)

print(robo.posx, robo.posy, pos_x[robo.i], pos_y[robo.i], tempo[robo.i], robo.velx, robo.vely)

robo.i = 0





janela.mainloop()