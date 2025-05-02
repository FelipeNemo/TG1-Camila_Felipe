"""Modulo que implementa todas as classes de erro!"""

#Class dado
class NumeroLadosInvalido(Exception):
    """O número de lados deve ser maior que 0"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "NumeroLadosInvalido (" + self.__msg +")"