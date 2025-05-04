"""Modulo que implementa todas as classes de erro!"""

#Class dado
class NumeroLadosInvalido(Exception):
    """O número de lados deve ser maior que 0"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "NumeroLadosInvalido (" + self.__msg +")"
    
class ErroClasseInvalida(Exception):
    """classe deve ser uma instância de Classe"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroClasseInvalida (" + self.__msg +")"  

class ErroLimiteInventario(Exception):
    """Define o limite do inventário para cada Classe válida"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroClasseInvalida (" + self.__msg +")" 

class ErroHabilidadeInvalida(Exception):
    """Habilidade não é válida - ou seja não possue classe com o nome da habilidade"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroClasseInvalida (" + self.__msg +")"  

class ErroInventarioVazio(Exception):
    """Caso o inventário esteja vazio"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroClasseInvalida (" + self.__msg +")"  

class ErroDadoAtaqueInvalido(Exception):
    """Dado de ataque deve ser instancia da classe dado"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroClasseInvalida (" + self.__msg +")"