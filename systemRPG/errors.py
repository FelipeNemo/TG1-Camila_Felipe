"""Classes de erros do sistema"""


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

class ErroLimiteInventario(Exception): # Saruman
    """Define o limite do inventário para cada Classe válida"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroLimiteInventario (" + self.__msg +")" 

class ErroHabilidadeInvalida(Exception): # Frodo
    """Habilidade não é válida - ou seja não possue classe com o nome da habilidade"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroHabilidadeInvalida (" + self.__msg +")"  

class ErroInventarioVazio(Exception):
    """Caso o inventário esteja vazio"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroInventarioVazio (" + self.__msg +")"  

class ErroDadoAtaqueInvalido(Exception):
    """Dado de ataque deve ser instancia da classe dado"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroDadoAtaqueInvalido (" + self.__msg +")"
    
class ErroPersonagemInvalido(Exception):
    """Existe elementos na lista que não são instancia da classe Personagem"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroPersonagemInvalido (" + self.__msg +")" 

class ErroNumeroPersonagem(Exception):
    """Deve haver pelo menos dois personagens na batalha"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroNumeroPersonagem (" + self.__msg +")"
    
class ErroHabilidadeNaoEncontrada(Exception):
    """Habilidade não está no inventário"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroHabilidadeNaoEncontrada (" + self.__msg +")" 
    
class ErroLeituraArquivo(Exception):
    """Erro ao ler o arquivo"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroLeituraArquivo (" + self.__msg +")"