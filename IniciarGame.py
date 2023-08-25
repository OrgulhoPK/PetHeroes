import pygame as pg

from Configs import *
import sys,random
#from Inimigos import Inimigo
from Imagens import Imagem
#from Sons import Sons
from Jogador import Jogador
from Personagens import Personagem
from Slots import Player

class Game:
    def __init__(self,tela,Fase):
        #tela e configuracoes locais
        self.FPS_CLOCK = pg.time.Clock()
        self.font = pg.font.Font('Fonts/runescape_uf.ttf',52)
        self.tela = tela
        self.encerrada = False
        self.background = Imagem.Background
        self.Finais = Imagem.ListFinais
        #self.Totem = [Estrutura]
        self.NewPlayer = Player(posxy=(112,448),personagem= D_Heitor,slots=Slots) ##Jogador
        #jogadores e inimigos
        self.jogadores = Fase.Jogadores
        self.Inimigos = []
        self.ListInimigos = Fase.ListInimigos
        self.Boss = Fase.ListBoss
        self.Fase = Fase
        self.Slots = Slots
        #contador e efeitos de arena
        self.contador = 0
        self.ticks = 0
        self.tempo = [5,0]
        self.timepause = False
        self.lista = Imagem.ListaColisoes
        self.mousexy = None
        self.mouse = False
        self.teste = False
       


    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.desenha(self.tela)  
            self.timer()
            self.getmouse()
            self.fusao(self.mousexy)
            #self.FimDeJogo(self.tela)

               
    def tratamento_eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()    
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:        
                self.encerrada = True
                self.ticks = 0
                self.Fase.NumTela = 2

    def desenha(self,tela):
        # mapa
        for i in self.background:
            i.desenha(tela)
        self.contador +=1
        if self.contador +1 >= 176:
            self.contador = 0
        tela.blit(Imagem.Centro[self.contador//5],(593,234))
        '''pg.draw.rect(tela,(50,255,120),(self.Slots[0]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[1]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[2]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[3]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[4]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[5]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[6]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[7]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[8]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[9]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[10]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[11]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[12]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[13]))
        pg.draw.rect(tela,(50,255,120),(self.Slots[14]))'''

        for i in self.NewPlayer.statsslot:
            if i[1]:
                self.NewPlayer.desenhar(tela)
                a,b,c,d = i[2]
                pg.draw.rect(tela,(50,255,120),(a-8,b-31,c,d),2)
                
        text = self.font.render((f'{self.tempo[0]:02}:{self.tempo[1]:02}'), 1, (0,0,0))
        tela.blit(text,(190,2))

        pg.display.update()
        self.FPS_CLOCK.tick(30)
    
#relogio de timer do jogo tempo [min , seg]
    def timer(self):
        if not self.timepause:
            if self.tempo[1]<0:
                self.tempo[0]-=1
                self.tempo[1]=59
            if self.ticks%30 == 0:
                self.tempo[1]-=1
            self.ticks += 1

    def getmouse(self):
        for event in pg.event.get():
            mx,my = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.mousexy = (mx,my)
                    self.mouse = True
                    return self.mousexy
    def fusao(self,mousexy):
        if self.mousexy is not(None):
            for i in self.NewPlayer.statsslot:
                if i[2].collidepoint((mousexy)):
                    print(i[2])
                    a,b,c,d = i[2]
                    pg.draw.rect(tela,(50,255,120),(a-8,b-31,c,d),2)
                    self.NewPlayer.teste = True
                else:
                    self.NewPlayer.teste = False
                    mousexy = None
                    self.mouse = False
                    print(mousexy)

    '''if pg.mouse.get_pressed()[0]:
            NewPlayer.x = mx -5
            NewPlayer.y = my +12'''