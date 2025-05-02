"""Classes para manipulação e gerenciamento de usuários e saus ações"""

# Imports.
from .gaming import *
from .errors import *
#from . import constantes as const
from abc import ABC, abstractmethod

#Classe : Classe abstrata que representa uma classe de personagem. Deve conter os seguintes atributos: (Feito) 
#nome : Nome da classe. (Feito)
#pontos_vida : quanta vida o personagem deverá ter. (Feito)
#dado_de_ataque : Dado de ataque da classe, um objeto do tipo Dado. (Feito)
#pontos_ataque : Pontos de ataque da classe. (Feito)
#pontos_defesa : Pontos de defesa da classe. (Feito)
#limite_habilidades : Limite de habilidades que o personagem pode ter. (Feito)

class Classe(ABC):
    def __init__(self, nome, pontos_vida, dado_de_ataque, pontos_ataque,pontos_defesa, limite_habilidades):
        self._nome = nome
        self._pontos_vida = pontos_vida
        self._dado_de_ataque = dado_de_ataque # objeto criado pela classe Dado
        self._pontos_ataque = pontos_ataque
        self._pontos_defesa = pontos_defesa
        self._limite_habilidades = limite_habilidades

    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, nome):
        self._nome = nome


    @property
    def pontos_vida(self):
        return self._pontos_vida
    
    @pontos_vida.setter 
    def pontos_vida(self, pontos_vida):
        self.nompontos_vida = pontos_vida


    @property
    def dado_de_ataque(self):
        return self._dado_de_ataque
    
    @dado_de_ataque.setter 
    def dado_de_ataque(self, dado_de_ataque):
        self.dado_de_ataque = dado_de_ataque


    @property
    def pontos_ataque(self):
        return self._pontos_ataque
    
    @pontos_ataque.setter 
    def _pontos_ataque(self, _pontos_ataque):
        self._pontos_ataque = _pontos_ataque


    @property
    def pontos_defesa(self):
        return self._pontos_defesa
    
    @pontos_defesa.setter 
    def pontos_defesa(self, pontos_defesa):
        self.pontos_defesa = pontos_defesa


    @property
    def limite_habilidades(self):
        return self._limite_habilidades
    
    @limite_habilidades.setter 
    def limite_habilidades(self, limite_habilidades):
        self.limite_habilidades = limite_habilidades

        
#Guerreiro : Subclasse de  Classe  que representa um guerreiro. (Feito)
#pontos_vida : 10 + ( pontos_defesa * 5). (Feito)
#dado_de_ataque : D12. (Feito)
#pontos_ataque : 6 (Feito)
#pontos_defesa : 8 (Feito)
#limite_habilidades : 2 (Feito)
class Guerreiro(Classe):
    def __init__(self):
        super().__init__(
            #nome="Guerreiro",
            pontos_vida=10 + (8 * 5),  # 10 + (pontos_defesa * 5)
            dado_de_ataque=D12(),      # Dado de ataque é um D12
            pontos_ataque=6,
            pontos_defesa=8,
            limite_habilidades=2
        )

#Mago : Subclasse de  Classe  que representa um mago.
#pontos_vida : 8 + ( pontos_defesa * 2)
#dado_de_ataque : D6.
#pontos_ataque : 10
#pontos_defesa : 3
#limite_habilidades : 5
class Mago(Classe):
    def __init__(self):
        super().__init__(
            #nome="Mago",
            pontos_vida=8 + (3 * 2),  
            dado_de_ataque=D6(),
            pontos_ataque=10,
            pontos_defesa=3,
            limite_habilidades=5
        )
#Ladino : Subclasse de  Classe  que representa um ladino.
#pontos_vida : 6 + ( pontos_defesa * 3)
#dado_de_ataque : D8.
#pontos_ataque : 8
#pontos_defesa : 5
#limite_habilidades : 3
class Ladino(Classe):
    def __init__(self):
        super().__init__(
            #nome="Ladino",
            pontos_vida=6 + (5 * 3),  
            dado_de_ataque=D8(),
            pontos_ataque=8,
            pontos_defesa=5,
            limite_habilidades=3
        )

#Personagem : Classe que representa um personagem do jogo. (Feito)
#qntd_instancias : Atributo que representa a quantidade de objetos instanciados. (Feito)
#nome : Nome do personagem. (Feito)
#classe : Classe do personagem, um atributo do tipo Classe. (Feito)
#inventario : Inventário do personagem, uma lista de objetos do tipo Habilidade. (Feito)
#Após usar uma habilidade, ela deve ser removida do inventário. Fazer
#pontos_vida : Pontos de vida do personagem, definidos pela classe escolhida. (Feito)
#dado_de_ataque : Pontos de ataque do personagem, definidos pela classe escolhida. (Feito)
#pontos_ataque : Pontos de ataque do personagem, definidos pela classe escolhida. (Feito)
#pontos_defesa : Pontos de defesa do personagem, definidos pela classe escolhida. (Feito)
class Personagem:
    qntd_instancias = 0
    def __init__(self,nome, classe, inventario):
        self._nome = nome
        self._classe = classe
        self._inventario = inventario
        Personagem.qntd_instancias += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, nome):
        self._nome = nome

    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, nova_classe):
        if isinstance(nova_classe, Classe):  # Aqui garante que é uma instância válida
            self._classe = nova_classe
        else:
            raise TypeError("classe deve ser uma instância de Classe")

    @property
    def inventario(self):
        return self._inventario
    
    @inventario.setter 
    def inventario(self, inventario):
        self._inventario = inventario
        
# - Métodos:
# criar_personagem()
# cria o objeto personagem
    @staticmethod 
    def criar_personagem(nome, nome_classe, habilidades_raw):
        # Criação do inventário com base nas habilidades passadas
        inventario = [Habilidade(habilidade) for habilidade in habilidades_raw]

        # Criação da classe do personagem com base no nome da classe
        if nome_classe == "Guerreiro":
            classe = Guerreiro()
        elif nome_classe == "Mago":
            classe = Mago()
        elif nome_classe == "Ladino":
            classe = Ladino()
        else:
            raise ValueError(f"Classe '{nome_classe}' não reconhecida.")

        # Criação e retorno do personagem
        return Personagem(nome, classe, inventario)

        
#atacar(alvo : Personagem) : Método que simula um ataque do personagem,
#retornando o dano causado.
#Ao atacar, o personagem deve, antes de jogar o dado de ataque, verificar se não
#utilizará uma habilidade.
#Enquanto houver habilidades no inventário, o personagem deve ter uma chance
#de 50% de usar uma habilidade.
#O dano padrão de qualquer personagem é realizado com o dado de ataque da classe.


#usar_habilidade(alvo : Personagem) : Método que simula o uso de uma
#habilidade, retornando o dano causado.





#Habilidade : Classe que representa uma habilidade do personagem.
#nome : Nome da habilidade.
#descricao : Descrição da habilidade.
#pontos_ataque : Pontos de ataque da habilidade.
#usar() : Método que simula o uso da habilidade.

class Habilidade:
    def __init__(self, nome, descricao, pontos_ataque):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    def usar(self):
        print(f"{self.nome} usada! Causa {self.pontos_ataque} de dano.")

    def __str__(self):
        return f"Habilidade: {self.nome}\nDescrição: {self.descricao}\nPontos de Ataque: {self.pontos_ataque}"

#BolaDeFogo : Subclasse de  Habilidade  que representa uma bola de fogo.
#descricao : "Uma bola de fogo que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 10 dano.
    
class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__(
            nome="Bola de Fogo",
            descricao="Uma bola de fogo que causa dano em área.",
            pontos_ataque=10
        )

    def usar(self):
        print(f"{self.nome} lançada! {self.descricao} Causa {self.pontos_ataque} de dano.")
  


#Cura : Subclasse de  Habilidade  que representa uma cura.
#descricao : "Uma cura que recupera 10 pontos de vida."
#usar() : Método que simula o uso da habilidade, recuperando 10 pontos de vida.
class Cura(Habilidade):
    def __init__(self):
        super().__init__(
            nome="Cura",
            descricao="Uma magia de que regenera danos em área.",
            pontos_ataque=-10 # -10 pois recupera dano hmm mas é tudo ataque ... 
        )                     # to recuperando a vida... a habilidade deve adicionar pontos de vida caso a hida não esteja cheia

    def usar(self):
        print(f"{self.nome} lançada! {self.descricao} Causa {self.pontos_ataque} de cura.")
  

#Tiro de Arco : Subclasse de  Habilidade  que representa um tiro de arco.
#descricao : "Um tiro de arco que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 6 dano.

class TiroArco(Habilidade):
    def __init__(self):
        super().__init__(
            nome="Tiro do Arco",
            descricao="Tiro de arco no oponente.",
            pontos_ataque=6 
        )

    def usar(self):
        print(f"{self.nome} lançado! {self.descricao} Causa {self.pontos_ataque} de dano.")