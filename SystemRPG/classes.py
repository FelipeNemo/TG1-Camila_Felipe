"""Classes para manipulação e gerenciamento do RPG"""

# Dado : Classe abstrata que representa um dado de RPG.
# lados : Número de lados do dado.
# jogar() : Método que simula o lançamento do dado e retorna um número aleatório
# entre 1 e o número de lados do dado.

# Imports.
#from .erros import *
#from . import constantes as const
from random import randint
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass 
class Dado(ABC):
    lado:int

    @abstractmethod
    def jogar(self):
        

#Classe : Classe abstrata que representa uma classe de personagem. Deve conter os
#seguintes atributos:
#nome : Nome da classe.
#pontos_vida : quanta vida o personagem deverá ter.
#dado_de_ataque : Dado de ataque da classe, um objeto do tipo Dado .
#pontos_ataque : Pontos de ataque da classe.
#pontos_defesa : Pontos de defesa da classe.
#limite_habilidades : Limite de habilidades que o personagem pode ter.

class Classe(ABC):
    def __init__(self, nome, pontos_vida, dado_de_ataque, pontos_ataque,pontos_defesa, limite_habilidades):
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.dado_de_ataque = dado_de_ataque # objeto criado pela classe Dado
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.limite_habilidades = limite_habilidades


#Personagem : Classe que representa um personagem do jogo.
#qntd_instancias : Atributo que representa a quantidade de objetos instanciados.
#nome : Nome do personagem.
#classe : Classe do personagem, um atributo do tipo Classe .
#inventario : Inventário do personagem, uma lista de objetos do tipo Habilidade .
#Após usar uma habilidade, ela deve ser removida do inventário.
#pontos_vida : Pontos de vida do personagem, definidos pela classe escolhida.
#dado_de_ataque : Pontos de ataque do personagem, definidos pela classe escolhida.
#pontos_ataque : Pontos de ataque do personagem, definidos pela classe escolhida.
#pontos_defesa : Pontos de defesa do personagem, definidos pela classe escolhida.
class Personagem:
    def __init__(self,nome, qntd_instancias, classe, inventario):
        self.nome = nome
        self.qntd_instancias = qntd_instancias
        self.classe = classe # objeto do tipo classe
        self.inventario = inventario
        
# - Métodos:
#atacar(alvo : Personagem) : Método que simula um ataque do personagem,
#retornando o dano causado.
#Ao atacar, o personagem deve, antes de jogar o dado de ataque, verificar se não
#utilizará uma habilidade.
#Enquanto houver habilidades no inventário, o personagem deve ter uma chance
#de 50% de usar uma habilidade.
#O dano padrão de qualquer personagem é realizado com o dado de ataque da
#classe.
#usar_habilidade(alvo : Personagem) : Método que simula o uso de uma
#habilidade, retornando o dano causado.
def usar_habilidade(self, alvo):
        """
        Usa a habilidade especial da classe e retorna o dano causado.
        Pode também ser adaptado para usar uma habilidade do inventário.
        """
        if self.inventario:
            habilidade = self.inventario.pop(0)  # remove a primeira habilidade do inventário
            print(f"{self.nome} usou a habilidade '{habilidade}' em {alvo.nome}!")
            dano = self.classe.habilidade_especial()
            return dano
        else:
            print(f"{self.nome} tentou usar uma habilidade, mas não tem nenhuma!")
            return 0

def atacar(self, alvo):
     if self.inventario and random.random() < 0.5:
        return self.usar_habilidade(alvo)
     else:
        dano = self.classe.rolar_dado_ataque()
        print(f"{self.nome} atacou {alvo.nome} com dano de {dano}.")
        return dano

#Habilidade : Classe que representa uma habilidade do personagem.
#nome : Nome da habilidade.
#descricao : Descrição da habilidade.
#pontos_ataque : Pontos de ataque da habilidade.
#usar() : Método que simula o uso da habilidade.

class Habilidade:
    def __init__(self, nome, descricao, pontos_ataque ):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

#Arena : Classe que representa a arena de combate.
#personagens : Lista de personagens que estão na arena.
#adicionar_personagem() : Método que adiciona um personagem à arena.
#remover_personagem() : Método que remove um personagem da arena.
#combate() : Método que simula o combate entre os personagens da arena,
#retornando o vencedor.
#As regras do combate serão as seguintes:
#O combate será realizado em turnos, onde cada personagem pode atacar
#um oponente aleatório (em combates com dois jogadores, será sempre o
#mesmo).
#O atacante rodará um D20 (um dado de 20 lados) e somará o resultado ao
#seu ataque.
#Se o valor final de ataque for maior que o valor de defesa do oponente, o
#ataque será bem sucedido.

class Arena:
    def __init__(self, personagens = []):
        self.personagens = personagens

#Guerreiro : Subclasse de  Classe  que representa um guerreiro.
#pontos_vida : 10 + ( pontos_defesa * 5)
#,ado_de_ataque : D12.
#pontos_ataque : 6
#pontos_defesa : 8
#limite_habilidades : 2
class Guerreiro(Arena):
    def __init__(self):
        pass


#Mago : Subclasse de  Classe  que representa um mago.
#pontos_vida : 8 + ( pontos_defesa * 2)
#dado_de_ataque : D6.
#pontos_ataque : 10
#pontos_defesa : 3
#limite_habilidades : 5
class Mago(Arena):
    def __init__(self):
        pass
#Ladino : Subclasse de  Classe  que representa um ladino.
#pontos_vida : 6 + ( pontos_defesa * 3)
#dado_de_ataque : D8.
#pontos_ataque : 8
#pontos_defesa : 5
#limite_habilidades : 3
class Ladino(Arena):
    def __init__(self):
        pass

#BolaDeFogo : Subclasse de  Habilidade  que representa uma bola de fogo.
#descricao : "Uma bola de fogo que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 10 dano.
class BolaDeFogo(Habilidade):
    def __init__(self):
        pass

#Cura : Subclasse de  Habilidade  que representa uma cura.
#descricao : "Uma cura que recupera 10 pontos de vida."
#usar() : Método que simula o uso da habilidade, recuperando 10 pontos de vida.
class Cura(Habilidade):
    def __init__(self):
        pass

#Tiro de Arco : Subclasse de  Habilidade  que representa um tiro de arco.
#descricao : "Um tiro de arco que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 6 dano.

class TiroArco(Habilidade):
    def __init__(self):
        pass
#Subclasses para cada tipo principal de Dado:
#D4 : Subclasse de  Dado  que representa um dado de 4 lados.
class D4(Dado):
    def __init__(self):
        pass
#D6 : Subclasse de  Dado  que representa um dado de 6 lados.
class D6(Dado):
    def __init__(self):
        pass
#D8 : Subclasse de  Dado  que representa um dado de 8 lados.
class D8(Dado):
    def __init__(self):
        pass
#D10 : Subclasse de  Dado  que representa um dado de 10 lados.
class D10(Dado):
    def __init__(self):
        pass
#D12 : Subclasse de  Dado  que representa um dado de 12 lados.
class D412(Dado):
    def __init__(self):
        pass
#D20 : Subclasse de  Dado  que representa um dado de 20 lados
class D20(Dado):
    def __init__(self):
        pass
