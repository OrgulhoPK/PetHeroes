from typing import List
class Personagem:
    def __init__(self,nome:str,vida:int,speed:int,timeSkills:List[int],sprites:List[list],habilidade):
        #vida,dano,skillbasica,skillespecial,estado
        self.nome = nome
        self.vida = vida
        self.speed = speed
        self.sprites = sprites  #[Esq_dir,cima,baixo,ataque]
        self.habilidade = habilidade
        self.timeSkills = timeSkills
        
        

