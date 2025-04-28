"""Classes para manipulação e gerenciamento do RPG"""

# Imports.
from .erros import *
#from . import constantes as const
import random 
from abc import ABC, abstractmethod

# Dado : Classe abstrata que representa um dado de RPG. (Feito)
# lados : Número de lados do dado. (Feito)
# jogar() : Método que simula o lançamento do dado e retorna um número aleatório entre 1 e o número de lados do dado. (Feito)
class Dado(ABC):
    def __init__(self, lados):
        self._lados = lados

    @property
    def lados(self):
        return self._lados

    @lados.setter
    def lados(self, lados):
        if lados <= 1:
            raise NumeroLadosInvalido("O número de lados deve ser maior que 0")
        self._lados = lados

    def __str__(self):
        return f"{self.__class__.__name__} com {self.lados} lados"

    @abstractmethod
    def jogar(self):
        """Método que simula o lançamento do dado"""
        pass

#Subclasses para cada tipo principal de Dado:
#D4 : Subclasse de  Dado  que representa um dado de 4 lados. (Feito)
class D4(Dado):
    def __init__(self):
        super().__init__(4)

    def jogar(self):
        return random.randint(1, self.lados) # (a=inicio,b=fim do range)
    
#D6 : Subclasse de  Dado  que representa um dado de 6 lados. (Feito)
class D6(Dado):
    def __init__(self):
        super().__init__(6)

    def jogar(self):
        return random.randint(1, self.lados)
    
#D8 : Subclasse de  Dado  que representa um dado de 8 lados. (Feito)
class D8(Dado):
    def __init__(self):
        super().__init__(8)

    def jogar(self):
        return random.randint(1, self.lados)
    
#D10 : Subclasse de  Dado  que representa um dado de 10 lados. (Feito)
class D10(Dado):
    def __init__(self):
        super().__init__(10)

    def jogar(self):
        return random.randint(1, self.lados)
    
#D12 : Subclasse de  Dado  que representa um dado de 12 lados. (Feito)
class D12(Dado):
    def __init__(self):
        super().__init__(12)

    def jogar(self):
        return random.randint(1, self.lados)
    
#D20 : Subclasse de  Dado  que representa um dado de 20 lados. (Feito)
class D20(Dado):
    def __init__(self):
        super().__init__(20)

    def jogar(self):
        return random.randint(1, self.lados)
        

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
        self.nome = nome


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
            nome="Guerreiro",
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
            nome="Mago",
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
            nome="Ladino",
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
    def inventario(self):
        return self._inventario
    
    @inventario.setter 
    def inventario(self, inventario):
        self._inventario = inventario
        
# - Métodos:
#atacar(alvo : Personagem) : Método que simula um ataque do personagem,
#retornando o dano causado.
#Ao atacar, o personagem deve, antes de jogar o dado de ataque, verificar se não
#utilizará uma habilidade.
#Enquanto houver habilidades no inventário, o personagem deve ter uma chance
#de 50% de usar uma habilidade.
#O dano padrão de qualquer personagem é realizado com o dado de ataque da classe.
    def atacar(self, alvo):
        if self._inventario and random.random() < 0.5:
            return self.usar_habilidade(alvo)
        else:
            dano = self.classe.rolar_dado_ataque()
            print(f"{self._nome} atacou {alvo._nome} com dano de {dano}.")
            return dano

#usar_habilidade(alvo : Personagem) : Método que simula o uso de uma
#habilidade, retornando o dano causado.
    def usar_habilidade(self, alvo):
            """
            Usa a habilidade especial da classe e retorna o dano causado.
            Pode também ser adaptado para usar uma habilidade do inventário.
            """
            if self.inventario:
                habilidade = self.inventario.pop(0)  # remove a primeira habilidade do inventário
                print(f"{self._nome} usou a habilidade '{habilidade}' em {alvo.nome}!")
                dano = self.classe.habilidade_especial()
                return dano
            else:
                print(f"{self._nome} tentou usar uma habilidade, mas não tem nenhuma!")
                return 0


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




