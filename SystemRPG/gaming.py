"""Classes para manipulação de ações dos personagens dentro do jogo"""


import random
from .errors import *
from .users import *
from abc import ABC, abstractmethod
import csv

# ------------------------------------

def salvar_csv(nome_arquivo, relatorio):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ['atacante', 'alvo','dado_lancado', 'dano', 'status_atacante', 'status_alvo', 'sucesso']
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        writer.writeheader()  # Escreve a linha de cabeçalho
        for linha in relatorio:
            writer.writerow(linha)  # Escreve cada linha do relatório

# ------------------------------------

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
    
#Habilidade : Classe que representa uma habilidade do personagem.
#nome : Nome da habilidade.
#descricao : Descrição da habilidade.
#pontos_ataque : Pontos de ataque da habilidade.
#usar() : Método que simula o uso da habilidade.
class Habilidade:
    def __init__(self, descricao, pontos_ataque):
        self.nome = self.__class__.__name__ 
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    def usar(self, personagem_atual, alvo):
        print(f"Habilidade {self.__class__.__name__ } foi usada")

    def __str__(self):
        return f"{self.nome}: (Poder de ataque: {self.pontos_ataque})"



#BolaDeFogo : Subclasse de  Habilidade  que representa uma bola de fogo.
#descricao : "Uma bola de fogo que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 10 dano.
class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__(
            descricao="Bola de fogo lançada, causa 10 pontos de dano!",
            pontos_ataque=10
        )

    def usar(self, personagem_atual, alvo): # Checar na lista a se tem habilidade e usar Fazer o tratamento aqui
        alvo._classe._pontos_vida -= self.pontos_ataque
        return self.pontos_ataque  # 1 = ataque

#Cura : Subclasse de  Habilidade  que representa uma cura.
#descricao : "Uma cura que recupera 10 pontos de vida."
#usar() : Método que simula o uso da habilidade, recuperando 10 pontos de vida.
class Cura(Habilidade):
    def __init__(self):
        super().__init__(
            descricao="Magia de cura lançada, usuário recebe 10 pontos de vida!",
            pontos_ataque=10 
        )                     

    def usar(self, personagem_atual, alvo):
        personagem_atual._classe._pontos_vida += self.pontos_ataque
        return self.pontos_ataque # 0 = cura


#Tiro de Arco : Subclasse de  Habilidade  que representa um tiro de arco.
#descricao : "Um tiro de arco que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 6 dano.
class TiroArco(Habilidade):
    def __init__(self):
        super().__init__(
            descricao="Tiro de arco lançado, causa 6 pontos de dano!",
            pontos_ataque=6
        )

    def usar(self, personagem_atual, alvo):
        alvo._classe._pontos_vida -= self.pontos_ataque
        return self.pontos_ataque
    
#Arena : Classe que representa a arena de combate.
#personagens : Lista de personagens que estão na arena. (Feito)
#adicionar_personagem() : Método que adiciona um personagem à arena. (Feito)
#remover_personagem() : Método que remove um personagem da arena. (Feito)
#combate() : Método que simula o combate entre os personagens da arena, (Feito)
#retornando o vencedor.
#As regras do combate serão as seguintes:
#O combate será realizado em turnos, onde cada personagem pode atacar
#um oponente aleatório (em combates com dois jogadores, será sempre o
#mesmo).
#O atacante rodará um D20 (um dado de 20 lados) e somará o resultado ao
#seu ataque.
#Se o valor final de ataque for maior que o valor de defesa do oponente, o
#ataque será bem sucedido.

# para cura Personagem.usar_habilidade
#para ataque Personagem.atacar
    
class Arena:
    def __init__(self, personagens):
        self.personagens = personagens
        self.relatorio = []
        self.dado_20 = D20()

    def adicionar_personagem(self, personagem):
        self.personagens.append(personagem)

    def remover_personagem(self, personagem):
        if personagem in self.personagens:
            self.personagens.remove(personagem)
  
    def combate(self):
        self.relatorio = [] # Reset no relatório a cada combate

        # Enquanto houver mais de um personagem vivo, o combate continua
        while len([p for p in self.personagens if p.esta_vivo()]) > 1:
            for atacante in self.personagens:
                if not atacante.esta_vivo():
                    # Pula o personagem se ele estiver morto
                    continue
                # Escolhe aleatoriamente um alvo vivo diferente do atacante
                alvos_vivos = [p for p in self.personagens if p != atacante and p.esta_vivo()]
                #  Se não houver mais alvos, o combate termina
                if not alvos_vivos:
                    break
                alvo = random.choice(alvos_vivos)
                # Usa o dado de 20 lados para o ataque
                ataque_dado = self.dado_20.jogar()
                # Soma o modificador de ataque da classe do atacante
                total_ataque = ataque_dado + atacante._classe.pontos_ataque

                if total_ataque > alvo._classe.pontos_defesa: # # Se o ataque for bem-sucedido
                    dano = atacante.atacar(alvo)  #calcula o dano
                    # Registrando o ataque no relatório
                    self.relatorio.append({
                        'atacante': atacante.nome,
                        'alvo': alvo.nome,
                        'dado_lancado': ataque_dado,
                        'dano': dano,
                        'status_atacante': atacante.exibir_status(),
                        'status_alvo': alvo.exibir_status(),
                        'sucesso': True
                    })
                    print(f"{atacante.nome} atacou {alvo.nome} e causou {dano} de dano!")
                else:
                     # Registrando a falha no relatório
                    self.relatorio.append({
                        'atacante': atacante.nome,
                        'alvo': alvo.nome,
                        'dado_lancado': ataque_dado,
                        'dano': 0,
                        'status_atacante': atacante.exibir_status(),
                        'status_alvo': alvo.exibir_status(),
                        'sucesso': False
                    })
                    print(f"{atacante.nome} tentou atacar {alvo.nome}, mas falhou!")

        vencedor = next(p for p in self.personagens if p.esta_vivo())
        return vencedor
    
    def get_relatorio_combates(self):
                # Aqui você pode usar o método exibir_status para exibir o status de todos os personagens
        for combate in self.relatorio:
            atacante = next(p for p in self.personagens if p.nome == combate['atacante'])
            alvo = next(p for p in self.personagens if p.nome == combate['alvo'])

            # Exibe o status dos personagens após cada combate
            print(f"Status após o combate: {atacante.exibir_status()} VS {alvo.exibir_status()}")
        return self.relatorio
    





