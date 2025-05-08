"""Classes para manipulação e gerenciamento de usuários e suas ações"""

# Imports.
from .gaming import *
# Dado, D4, D6, D8, D12, D10, D20
from .errors import *
#from . import constantes as const
import random
from abc import ABC, abstractmethod


#Classe : Classe abstrata que representa uma classe de personagem. Deve conter os seguintes atributos: (Feito) 
#nome : Nome da classe. (Feito)
#pontos_vida : quanta vida o personagem deverá ter. (Feito)
#dado_de_ataque : Dado de ataque da classe, um objeto do tipo Dado. (Feito)
#pontos_ataque : Pontos de ataque da classe. (Feito)
#pontos_defesa : Pontos de defesa da classe. (Feito)
#limite_habilidades : Limite de habilidades que o personagem pode ter. (Feito)

class Classe(ABC):
    def __init__(self, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades):
        self._nome = self.__class__.__name__  # define o nome com base na classe
        self._pontos_vida = pontos_vida
        self._dado_de_ataque = dado_de_ataque # objeto criado pela classe Dado
        self._pontos_ataque = pontos_ataque
        self._pontos_defesa = pontos_defesa
        self._limite_habilidades = limite_habilidades

    
    # nome será um atributo imutável, por isso não fiz o setter
    @property
    def nome(self):
        return self.__class__.__name__


    @property
    def pontos_vida(self):
        return self._pontos_vida
    
    @pontos_vida.setter 
    def pontos_vida(self, pontos_vida):
        self._pontos_vida = pontos_vida


    @property
    def dado_de_ataque(self):
        return self._dado_de_ataque
    
    @dado_de_ataque.setter 
    def dado_de_ataque(self, dado_de_ataque):
        if not isinstance(dado_de_ataque, Dado):
            raise ErroDadoAtaqueInvalido("dado_de_ataque deve ser uma instância das subclasses de Dado.")
        self._dado_de_ataque = dado_de_ataque


    @property
    def pontos_ataque(self):
        return self._pontos_ataque
    
    @pontos_ataque.setter 
    def pontos_ataque(self, pontos_ataque):
        self._pontos_ataque = pontos_ataque


    @property
    def pontos_defesa(self):
        return self._pontos_defesa
    
    @pontos_defesa.setter 
    def pontos_defesa(self, pontos_defesa):
        self._pontos_defesa = pontos_defesa


    @property
    def limite_habilidades(self):
        return self._limite_habilidades
    
    @limite_habilidades.setter 
    def limite_habilidades(self, limite_habilidades):
        self._limite_habilidades = limite_habilidades

    @abstractmethod # Não achei outra função abstrata ainda para essa classe... acho que vai ser algo relacionado aos danos nos atributos
    def __str__(self): # Em classes que herdam o str só é preciso ser implementado na mãe
        """Cada classe deve definir como usa suas habilidades."""
        pass

    def __repr__(self):
        # Representação técnica para debug
        return f"Classe(nome={self._nome}, pontos_vida={self._pontos_vida}, pontos_ataque={self._pontos_ataque}, pontos_defesa={self._pontos_defesa})"
    
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
    def __str__(self):
        return f"{self._nome} - Vida: {self._pontos_vida}, Ataque: {self._pontos_ataque}, Defesa: {self._pontos_defesa}"


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

    def __str__(self):
        return f"{self._nome} - Vida: {self._pontos_vida}, Ataque: {self._pontos_ataque}, Defesa: {self._pontos_defesa}"
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

    def __str__(self):
        return f"{self._nome} - Vida: {self._pontos_vida}, Ataque: {self._pontos_ataque}, Defesa: {self._pontos_defesa}"

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
            raise ErroClasseInvalida("classe deve ser uma instância de Classe")

    @property
    def inventario(self):
        return self._inventario
    
    @inventario.setter 
    def inventario(self, inventario):
        self._inventario = inventario

    def __str__(self):
        return (
        f"Nome: {self._nome} | "
        f"Classe: {self._classe._nome} | "
        f"Habilidades: {[habilidade.__class__.__name__ for habilidade in self._inventario]}"
    )

    def __repr__(self):
        return (
        f"Personagem(nome='{self._nome}', "
        f"classe='{self._classe._nome}', "
        f"inventario={[habilidade.__class__.__name__ for habilidade in self._inventario]})"
    )
        
# - Métodos:
    def esta_vivo(self):
        return self.classe.pontos_vida > 0
# criar_personagem(): Cria o objeto personagem
    @staticmethod 
    def criar_personagem(nome, nome_classe, habilidades_raw):
        habilidades_map = {"BolaDeFogo": BolaDeFogo,
                           "Cura": Cura,
                           "Tiro de Arco": TiroArco
                           }

        # 1. Cria a classe (isso já define limite_habilidades)
        if nome_classe == "Guerreiro":
            classe = Guerreiro()
        elif nome_classe == "Mago":
            classe = Mago()
        elif nome_classe == "Ladino":
            classe = Ladino()
        else:
            raise ErroClasseInvalida(f"Classe '{nome_classe}'deve ser uma instância de Classe.")

        # 2. Verifica o limite de habilidades
        if len(habilidades_raw) > classe.limite_habilidades:
            raise ErroLimiteInventario(f"A classe '{classe.nome}' permite no máximo {classe.limite_habilidades} habilidades, mas você tentou adicionar {len(habilidades_raw)}.")

        # 3. Monta o inventário
        inventario = []
        for habilidade_nome in habilidades_raw:
            if habilidade_nome in habilidades_map:
                inventario.append(habilidades_map[habilidade_nome]())
            else:
                raise ErroHabilidadeInvalida(f"Habilidade '{habilidade_nome}' não reconhecida.")

        return Personagem(nome, classe, inventario)


#usar_habilidade(alvo : Personagem) : Método que simula o uso de uma habilidade, retornando o dano causado.
# verifica se a habilidade está no inventário 
    def usar_habilidade(self, habilidade, alvo):
        if habilidade not in self._inventario:
            raise ErroHabilidadeNaoEncontrada("Habilidade não está no inventário.")
        return habilidade.usar(self, alvo)

    
#atacar(alvo : Personagem) : Método que simula um ataque do personagem,
#retornando o dano causado.
#Ao atacar, o personagem deve, antes de jogar o dado de ataque, verificar se não
#utilizará uma habilidade.
#Enquanto houver habilidades no inventário, o personagem deve ter uma chance
#de 50% de usar uma habilidade.
#O dano padrão de qualquer personagem é realizado com o dado de ataque da classe.
    def atacar(self, alvo):
        if self._inventario and random.random() < 0.5:
            # 50% de chance de usar uma habilidade
            return self.usar_habilidade(alvo)
        else:
            # Dano padrão: joga o dado de ataque e soma os pontos de ataque
            dano_bruto = self._classe.dado_de_ataque.rolar() + self._classe.pontos_ataque
            # Dano real é o dano bruto menos os pontos de defesa do alvo (mínimo 0)
            dano_real = max(0, dano_bruto - alvo._classe.pontos_defesa)
            # Aplica o dano ao alvo
            alvo._classe.pontos_vida -= dano_real
            return dano_real

    

