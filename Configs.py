import pygame as pg
import random
from Personagens import Personagem
from Imagens import Imagem
from Habilidades import Skill

#Configuracoes padroes
S_HEIGHT = 800
S_WIDHT = 480

tela = pg.display.set_mode((S_WIDHT, S_HEIGHT))


#caixa de selecao do menu 1
TelaInicial = [pg.Rect(149,357,184,33),
                pg.Rect(508,441,263,37)]


#Blocos centrais, para orientação dos campos de ataque.

Slots = [pg.Rect(112,448,31,45),pg.Rect(176,448,31,45),pg.Rect(240,448,31,45),pg.Rect(304,448,31,45),
        pg.Rect(368,448,31,45),pg.Rect(112,512,31,45),pg.Rect(176,512,31,45),pg.Rect(240,512,31,45),
        pg.Rect(304,512,31,45),pg.Rect(368,512,31,45),pg.Rect(112,576,31,45),pg.Rect(176,576,31,45),
        pg.Rect(240,576,31,45),pg.Rect(304,576,31,45),pg.Rect(368,576,31,45)]

#Lista de habilidades Aliadas
SkillsIda = [Skill(5,Imagem.hitDamage),Skill(5,Imagem.hitDamage)]
SkillsHeitor = [Skill(20,Imagem.tornado),Skill(92,Imagem.C_Stun1)]
SkillsJurupari = [Skill(5,Imagem.S_fireball1),Skill(92,Imagem.S_CirculoFogo)]
SkillsGuaraci = [Skill(5,Imagem.hitDamage),Skill(35,Imagem.circuloTotem)]


#Lista de personagens

#Personagem = Personagem (vida,dano, Sprites:list , Skills: list)
D_Heitor = Personagem('Heitor',30,4,[6,150],Imagem.Sprites_Clerigo,SkillsHeitor)
Ida = Personagem('Ida',35,5,[20,150],Imagem.Sprites_Duelista,SkillsIda)
Jurupari = Personagem('Jurupari',20,4,[3,450],Imagem.Sprites_Shaman,SkillsJurupari)
Guaraci = Personagem('Guaraci',50,3,[54,210],Imagem.Sprites_Tanker,SkillsGuaraci)



class setup:
    NumTela = 0
    Jogadores = [()]
    ListInimigos = []
    ListBoss = []
#Define a quantidade de monstros no jogo
#    def adicionarInimigos(self):
#        if not self.ListBoss and not self.ListInimigos:
#            self.ListBoss.append(Inimigo(posxy=(500,300),personagem=Boss))
#            for i in range (0,15):
#                x = random.randint(525,750)
#                y = random.randint(200,370)
#                self.ListInimigos.append(Inimigo(posxy=(x,y),personagem=Soldadinho))




