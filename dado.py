# Classe dado 05/04/2025 - Camila

from abc import ABC, abstractmethod
from random import randint

class Dado (ABC):
    def __init__(self, lados : int):
        if lados > 0 :
            self._lados = lados
        else:
            raise ValueError("O dado deve conter um número positivo de lados")
    
    def jogar (self) -> int:
        return randint (1, self._lados)
    
    def __str__(self) -> str :
        return f"Lados: {self._lados}"
    
    def __repr__(self) -> str:
        return f"Lados = {self._lados}"
    
class D4 (Dado):
    def __init__(self):
        super().__init__(4)
    
class D6 (Dado):
    def __init__(self):
        super().__init__(6)
    
class D8 (Dado):
    def __init__(self):
        super().__init__(8)
    
class D10 (Dado):
    def __init__(self):
        super().__init__(10)
    
class D12 (Dado):
    def __init__(self):
        super().__init__(12)
    
class D20 (Dado):
    def __init__(self):
        super().__init__(20)