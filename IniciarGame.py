import pygame as pg

from Configs import *
import sys,random
#from Inimigos import Inimigo
from Imagens import Imagem
#from Sons import Sons
from Jogador import Jogador
from Personagens import Personagem


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
        self.NewPlayer = Jogador(posxy=(112,448),personagem= D_Heitor)
        #jogadores e inimigos
        self.jogadores = Fase.Jogadores
        self.Inimigos = []
        self.ListInimigos = Fase.ListInimigos
        self.Boss = Fase.ListBoss
        self.Fase = Fase
        #contador e efeitos de arena
        self.contador = 0
        self.ticks = 0
        self.tempo = [5,0]
        self.timepause = False
        self.lista = Imagem.ListaColisoes
       


    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.desenha(self.tela)  
            self.timer()
            self.movimentos(self.NewPlayer)
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
        pg.draw.rect(tela,(50,255,120),(pg.Rect(112,448,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(176,448,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(240,448,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(304,448,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(368,448,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(112,512,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(176,512,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(240,512,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(304,512,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(368,512,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(112,576,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(176,576,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(240,576,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(304,576,16,16)))
        pg.draw.rect(tela,(50,255,120),(pg.Rect(368,576,16,16)))

        self.NewPlayer.desenhar(tela)
        text = self.font.render((f'{self.tempo[0]:02}:{self.tempo[1]:02}'), 1, (0,0,0))
        tela.blit(text,(190,2))

        pg.display.update()
        self.FPS_CLOCK.tick(120)
    
#relogio de timer do jogo tempo [min , seg]
    def timer(self):
        if not self.timepause:
            if self.tempo[1]<0:
                self.tempo[0]-=1
                self.tempo[1]=59
            if self.ticks%30 == 0:
                self.tempo[1]-=1
            self.ticks += 1
    def movimentos(self,NewPlayer):
        mx,my = pg.mouse.get_pos()
        if NewPlayer.hitbox.collidepoint((mx,my)):
            if pg.mouse.get_pressed()[0]:
                NewPlayer.x = mx -5
                NewPlayer.y = my +12