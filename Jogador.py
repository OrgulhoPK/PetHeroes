import pygame as pg
from Imagens import Imagem
from Personagens import Personagem
class Jogador:
    def __init__(self,posxy:list,personagem:Personagem): #(self, x, y, widht, height)
        #posição e speed
        self.x = posxy[0]
        self.y = posxy[1]
        self.mov_vx = 0
        self.mov_vy = 0
        self.speed = personagem.speed
        #Dados dos inimigos
        self.dados = []   

        #Atributos e skills de personagens
        #separei para ter uma visao melhor dos atributos
        self.nome = personagem.nome
        self.vida = personagem.vida
        self.hpmax = personagem.vida #orientacao para barra hp e heal
        self.hitbox = pg.Rect(self.x-8,self.y-31,31,45)
        self.sprites = personagem.sprites
        self.HBasica = personagem.habilidade[0]
        self.HEspecial = personagem.habilidade[1]

        self.projeteis = []  #list projeteis
        self.teste = False

        #estado e  condições
        self.mousexy = None  #posicao do mouse para habilidade
        self.visible= True
        self.atk = False
        self.atkEspecial = False
        self.acao = True     
        self.mouse = False
         #controle de grupo
        self.slow = False
        self.stun = False
        self.timestun = 0 
        self.timeslow = 0
        self.status = self.speed
        #Contadores de animação e  efeitos
        self.cooldown1= personagem.timeSkills[0]
        self.cooldown2= personagem.timeSkills[1]
        self.sequenciaATK = 0
        self.anim_mov = 0    
        self.countatk = 0
        self.countspec =  0


    #Funcao de dano sofrido
    def hit(self,dano:int):
        if self.vida>0:
            self.vida -= dano
        else:
            self.visible = False
    
#Desenha e gerencia os ataques(atualiza hitbox e barra de vida)
    def desenhar(self,tela):
        #Sprites
        posx = self.x - 23
        posy = self.y - 48
        esq_Dir,cima,baixo,ataque,especial = self.sprites[0],self.sprites[1],self.sprites[2],self.sprites[3],self.sprites[4]
        if not self.atk and not self.atkEspecial:
            if self.mov_vx == 0 and self.mov_vy == 0:
                tela.blit(pg.transform.scale(baixo[0], (64,64)),(posx,posy))
        #atualizar posicao do hitbox e barra de vida
        self.hitbox = pg.Rect(self.x-8,self.y-31,31,45)
        if self.teste:
            pg.draw.rect(tela,(50,255,120),(self.hitbox),2)
        
        #projeteis
        if self.nome == 'Heitor' or self.nome == 'Jurupari': 
            if self.mov_vx == -1:
                tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(posx,posy))
            else:
                tela.blit(ataque[self.countatk//2],(posx,posy))  
                                                
            if self.countatk +1 >= 16:
                self.countatk = 0
                self.atk = False
                projetil = self.HBasica.BasicaRange(self.nome,posx,posy,(self.mov_vx,self.mov_vy))
                self.projeteis.append(projetil) 
                self.cooldown1 = 0
            self.countatk +=1


        for projeteis in self.projeteis:        
            projeteis.desenha(tela) 

#Desenha e chama as habilidades de ataque
def desenhar_Ataques(self,tela,ataque:list):

    #Clerigo e Shaman
    if self.nome == 'Heitor' or self.nome == 'Jurupari': 
        if self.mov_vx == -1:
            tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x,self.y))
        else:
            tela.blit(ataque[self.countatk//2],(self.x,self.y))  
                                            
        if self.countatk +1 >= 16:
            self.countatk = 0
            self.atk = False
            projetil = self.HBasica.BasicaRange(self.nome,self.x,self.y,(self.mov_vx,self.mov_vy))
            self.projeteis.append(projetil) 
            self.cooldown1 = 0
        self.countatk +=1
