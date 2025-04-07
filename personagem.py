#classe personagem 06/04/2025 - Camila

from classe import Classe, Guerreiro, Mago, Ladino
from habilidade import Habilidade
class Personagem:
    def __init__(self, nome : str, classe : Classe):
        self._nome = nome
        self._classe = classe
        self._inventario: list[Habilidade] = []
        self._pontos_vida = classe._pontos_vida
        self._dado_de_ataque = classe._dado_ataque
        self._pontos_de_defesa = classe._pontos_defesa
        self._pontos_de_ataque = classe._pontos_ataque
        Personagem.qntd_instancias += 1

    def __str__(self):
        return (
            f"Nome: {self._nome}\n"
            f"Classe: {self._classe}\n"
            f"Inventário: {self._inventario}\n"
            f"Pontos de Vida: {self.pontos_vida}\n"
            f"Dado de Ataque: {self._dado_de_ataque}\n"
            f"Pontos de Defesa: {self._pontos_de_defesa}\n"
            f"Pontos de Ataque: {self._pontos_de_ataque}\n"    
            )
    
    def __repr__(self):
        return (
            f"Nome = {self._nome}\n"
            f"Classe = {self._classe}\n"
            f"Inventário = {self._inventario}\n"
            f"Pontos de Vida = {self.pontos_vida}\n"
            f"Dado de Ataque = {self._dado_de_ataque}\n"
            f"Pontos de Defesa = {self._pontos_de_defesa}\n"
            f"Pontos de Ataque = {self._pontos_de_ataque}\n"    
            )
                