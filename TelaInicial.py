import pygame as pg
import sys

from Configs import *
from Imagens import Imagem
#from Sons import Sons

class PrimeiraTela:
    
    def __init__(self,tela,Fase):
        self.tela = tela
        self.encerra = False
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.opcoes = 0
        self.menu = 0
        self.Fase = Fase

    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha(self.tela)
  
    def tratamento_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                

        self.opcoes = self.SelectMenu(TelaInicial)
        if self.opcoes == 3:
            self.StoryMode()

    def desenha(self,tela):

        self.contador +=1
        if self.contador +1 >= 89:
            self.contador = 0
        
        tela.blit(Imagem.telaFundo1,(0,0))
        pg.draw.rect(tela,(255,0,0),TelaInicial[0],2)
    

        self.FPS_Clock.tick(30)
        pg.display.flip()     

    def StoryMode(self):
        
        self.menu = 0
        self.encerra = True
        self.Fase.NumTela = 3
        #Sons.menu1.stop()
                    
    def SelectMenu(self,opcoes:list):
        mx,my = pg.mouse.get_pos()
        if opcoes[0].collidepoint((mx,my)):
            if pg.mouse.get_pressed()[0]:
                return 3
