from typing import List
import pygame as pg
from Imagens import Imagem
from Personagens import Personagem


#Destinado ao controle dos slots de personagem, de acordo com o game

class Player:
    def __init__(self,posxy:list,personagem:List[Personagem],slots:list):
        #self.personagem1 = personagem[0]
        #self.personagem2 = personagem[1]
        #self.personagem2 = personagem[2]
        #self.personagem2 = personagem[3]
        #self.personagem2 = personagem[4]
        self.listslots = slots
        self.statsslot= self.blocos(slots)  #numero do slot e status(true se tiver personagem e false se nao tiver)


        self.x = posxy[0]
        self.y = posxy[1]
        self.mov_vx = 0
        self.mov_vy = 0

        self.visible= True
        self.atk = False
        self.atkEspecial = False


        #Referentes ao Personagem
        self.nome = personagem.nome
        self.hitbox = pg.Rect(self.x-8,self.y-31,31,45)
        self.sprites = personagem.sprites
        self.HBasica = personagem.habilidade[0]
        self.HEspecial = personagem.habilidade[1]
        self.timeSkills = personagem.timeSkills
        self.projeteis = []  #list projeteis
        self.teste = False
        self.stun = False
        self.timestun = 0 
        self.cooldown1= personagem.timeSkills[0]
        self.cooldown2= personagem.timeSkills[1]
        self.sequenciaATK = 0
        self.anim_mov = 0    
        self.countatk = 0
        self.countspec =  0



    

    def atualizar_estado(self):
        pass
    

    def Personagens(self):
        #usado para defir levels e pontuação dos personagens
        pass

    def blocos(self,slots):
        list = []
        num = 1
        for i in slots:
            if (num%2) == 1:
                print(i)
                bloco = [num,True,i]
                list.append(bloco)
                num+=1
            else:
                bloco = [num,False,i]
                list.append(bloco)
                num+=1
        return list

            

        #definir slots
        #no slot preciso ter informações sobre o personagem invocado nele.
        pass

    def desenhar(self,tela):
        #Sprites
        #posição do personagem, levando em referencia do x e y do slot 1
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
        '''if self.nome == 'Heitor' or self.nome == 'Jurupari': 
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
            projeteis.desenha(tela) '''
        
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


