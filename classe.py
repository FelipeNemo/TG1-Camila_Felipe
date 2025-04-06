# classe CLasse 05/04/2025 - Camila
from abc import ABC
from dado import Dado, D4, D6, D8, D10, D12, D20

class Classe(ABC):
    def __init__(self, nome, pontos_vida, dado_ataque, pontos_ataque, pontos_defesa, limite_habilidades):
        self._nome : str = nome
        self._pontos_vida : int = pontos_vida
        self._dado_ataque : Dado = dado_ataque
        self._pontos_ataque : int = pontos_ataque
        self._pontos_defesa : int = pontos_defesa
        self._limite_habilidades : int = limite_habilidades

    def __str__(self) -> str:
        return (
            f"Nome: {self._nome}\n"
            f"Pontos de Vida: {self._pontos_vida}\n"
            f"Dado de Ataque: {self._dado_ataque.__class__.__name__}\n"
            f"Pontos de Ataque: {self._pontos_ataque}\n"
            f"Pontos de Defesa: {self._pontos_defesa}\n"
            f"Limite de Habilidades: {self._limite_habilidades}"
            )
    
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"nome='{self._nome}', "
            f"pontos_vida={self._pontos_vida}, "
            f"dado_ataque={self._dado_ataque.__class__.__name__}(), "
            f"pontos_ataque={self._pontos_ataque}, "
            f"pontos_defesa={self._pontos_defesa}, "
            f"limite_habilidades={self._limite_habilidades}"
            f")"
            ) 
    
    @property
    def nome (self):
        return self._nome
    
    @property
    def pontos_vida (self):
        return self._pontos_vida
    
    @property
    def dado_ataque (self):
        return self._dado_ataque
    
    @property
    def pontos_ataque (self):
        return self._pontos_ataque

    @property
    def pontos_defesa (self):
        return self._pontos_defesa

    @property
    def limite_habilidades (self):
        return self._limite_habilidades

    @pontos_vida.setter
    #recebe um novo valor para pontos_de vida e substitui o antigo
    def pontos_vida (self, novo):
        if novo <= 0:
            raise ValueError("O seu personagem morreu!")
        else :
            self._pontos_vida = novo    
    
    @dado_ataque.setter
    #recebe um novo valor para dano_ataque e substitui o antigo
    def pontos_ataque (self, novo):
        if novo <= 0:
            raise ValueError("O dano de ataque deve ser um valor positivo!")
        else:
            self._pontos_ataque = novo
    
    @pontos_defesa.setter
    #recebe um novo valor para pontos_defesa e substitui o antigo
    def pontos_defesa (self, novo):
        if novo < 0:
            raise ValueError("O valor dos pontos de defesa deve ser igual ou superior a 0!")
        else:
            self._pontos_defesa = novo

class Guerreiro (Classe):
    def __init__(self):
        super().__init__(
            nome = "Guerreiro", 
            pontos_vida = 10 + 8 * 5, 
            dado_ataque = D12(), 
            pontos_ataque = 6,
            pontos_defesa = 8,
            limite_habilidades = 2
            )

class Mago (Classe):
    def __init__(self):
        super().__init__(
            nome = "Mago",
            pontos_vida = 8 + 3 * 2, 
            dado_ataque = D6(), 
            pontos_ataque = 10, 
            pontos_defesa = 3, 
            limite_habilidades = 5
            )
        
class Ladino (Classe):
    def __init__(self):
        super().__init__(
            nome = "Ladino",
            pontos_vida = 6 + 5 * 3, 
            dado_ataque = D8(), 
            pontos_ataque = 8, 
            pontos_defesa = 5, 
            limite_habilidades = 3
            )
        
