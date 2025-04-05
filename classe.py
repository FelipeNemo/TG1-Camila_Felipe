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
        
