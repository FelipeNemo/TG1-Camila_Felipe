"""Classes para manipulação e gerenciamento do RPG"""

# Imports.
from .errors import *
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


#Arena : Classe que representa a arena de combate.
#personagens : Lista de personagens que estão na arena. (Feito)
#adicionar_personagem() : Método que adiciona um personagem à arena. (Feito)
#remover_personagem() : Método que remove um personagem da arena. (Feito)
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
    def __init__(self, personagens=None):
        self.personagens = personagens if personagens is not None else [] # se personagem ta na lista... e se é instancia de personagem

    def adicionar_personagem(self, personagem):
        self.personagens.append(personagem)

    def remover_personagem(self, personagem):
        if personagem in self.personagens:
            self.personagens.remove(personagem)

    def combate(self):
        if len(self.personagens) < 2:
            print("Combate precisa de pelo menos dois personagens.") # Lançar erro
            return None

        vivos = self.personagens[:]

        while len(vivos) > 1:
            for atacante in vivos[:]:
                # Seleciona um oponente aleatório que não seja o próprio atacante
                oponentes = [p for p in vivos if p != atacante]
                if not oponentes:
                    break
                alvo = random.choice(oponentes) # alvo recebe escolha de oponente aleatório 
                # executar a função jogar da subclasse D20
                d20 = random.randint(1, 20) # atribui o resultado aleatório a d20 ... mas não estou usando a classe D20...
                ataque_total = d20 + atacante.ataque # soma 

                print(f"{atacante.nome} rola D20 = {d20} + ataque {atacante.ataque} = {ataque_total}")
                print(f"{alvo.nome} tem defesa {alvo.defesa}")

                if ataque_total > alvo.defesa:
                    dano = atacante.ataque
                    print(f"Ataque bem-sucedido! {alvo.nome} sofre {dano} de dano.")
                    alvo.sofrer_dano(dano)
                else:
                    print(f"{atacante.nome} errou o ataque em {alvo.nome}.")

                if alvo.pontos_vida <= 0:
                    print(f"{alvo.nome} foi derrotado!")
                    vivos.remove(alvo)

                if len(vivos) == 1:
                    break

        vencedor = vivos[0]
        print(f"\n{vencedor.nome} é o vencedor!")
        return vencedor




