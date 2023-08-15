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
        self.timeSkills = personagem.timeSkills
        self.projeteis = []  #list projeteis

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

    def esquerda(self):
        self.x -= self.speed
    def direita(self):
        self.x += self.speed
    def cima(self):
        self.y -= self.speed
    def baixo(self):
        self.y  += self.speed
    def parar(self):
        self.mov_vy = 0
        self.mov_vx = 0

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
            if self.mov_vx == 1 or (self.mov_vx ==1 and 
                (self.mov_vy == 1 or self.mov_vy == -1)):                
                tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(posx,posy))
            elif self.mov_vx == -1 or (self.mov_vx == -1 and
                (self.mov_vy == 1 or self.mov_vy == -1)):   
                tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(posx,posy))
            elif self.mov_vy == -1:
                tela.blit(pg.transform.scale(cima[self.anim_mov//4], (64,64)),(posx,posy))  
            elif self.mov_vy == 1:
                tela.blit(pg.transform.scale(baixo[self.anim_mov//4], (64,64)),(posx,posy))
            if self.anim_mov+1 >= 28:
                self.anim_mov = 0
            self.anim_mov +=1
            self.parar()

        if self.stun:
            tela.blit(Imagem.starStun1[self.timestun//5],(self.x+5,self.y-10))
        #atualizar posicao do hitbox e barra de vida
        self.hitbox = pg.Rect(self.x-8,self.y-31,31,45)
        pg.draw.rect(tela,(50,255,120),(self.hitbox),2)
        #projeteis
        for projeteis in self.projeteis:      
            projeteis.desenha(tela) 

#Desenha e chama as habilidades de ataque
def desenhar_Ataques(self,tela,ataque:list):
    #Duelista
    if self.nome == 'Ida':            
            if self.mov_vx == -1:
                if self.countatk > 13:
                    self.HBasica.Basica(self.nome,self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x-64,self.y-64))
            else:
                if self.countatk > 13:
                    self.HBasica.Basica(self.nome,self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                tela.blit(ataque[self.countatk//2],(self.x-64,self.y-64))
            
            if self.countatk +1 >= 16:
                self.countatk = 0
                self.atk = False
                self.cooldown1 = 0
            self.countatk +=1
    #Tanker
    if self.nome == 'Guaraci':            
        if self.mov_vx == -1:
            if self.countatk >10: 
                self.x -= self.speed*2
            if self.countatk == 15:
                    self.HBasica.BasicaGuaraci(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy),self.speed)
            tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x,self.y))
        else:
            if self.countatk >10: 
                self.x += self.speed*2
            if self.countatk == 15:
                self.HBasica.BasicaGuaraci(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy),self.speed)
            tela.blit(ataque[self.countatk//2],(self.x,self.y))
        
        if self.countatk +1 >= 16:
            self.countatk = 0
            self.cooldown1 = 0
            self.atk = False
            
        self.countatk +=1

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
