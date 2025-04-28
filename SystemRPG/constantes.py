



#Subclasses:
#Arena : Classe que representa a arena de combate.
#personagens : Lista de personagens que estão na arena.
#adicionar_personagem() : Método que adiciona um personagem à arena.
#remover_personagem() : Método que remove um personagem da arena.
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
#Guerreiro : Subclasse de Classe que representa um guerreiro.
#pontos_vida : 10 + ( pontos_defesa * 5)
#dado_de_ataque : D12.
#pontos_ataque : 6
#pontos_defesa : 8
#limite_habilidades : 2
#Mago : Subclasse de Classe que representa um mago.
#pontos_vida : 8 + ( pontos_defesa * 2)
#dado_de_ataque : D6.
#pontos_ataque : 10
#pontos_defesa : 3
#limite_habilidades : 5
#Ladino : Subclasse de Classe que representa um ladino.
#pontos_vida : 6 + ( pontos_defesa * 3)
#dado_de_ataque : D8.
#pontos_ataque : 8
#pontos_defesa : 5
#limite_habilidades : 3
#BolaDeFogo : Subclasse de Habilidade que representa uma bola de fogo.
#descricao : "Uma bola de fogo que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 10 dano.
#Restrições:
#Ponto por Criatividade:
#Cura : Subclasse de Habilidade que representa uma cura.
#descricao : "Uma cura que recupera 10 pontos de vida."
#usar() : Método que simula o uso da habilidade, recuperando 10 pontos de vida.
#Tiro de Arco : Subclasse de Habilidade que representa um tiro de arco.
#descricao : "Um tiro de arco que causa dano em área."
#usar() : Método que simula o uso da habilidade, causando 6 dano.
#Subclasses para cada tipo principal de Dado:
#D4 : Subclasse de Dado que representa um dado de 4 lados.
#D6 : Subclasse de Dado que representa um dado de 6 lados.
#D8 : Subclasse de Dado que representa um dado de 8 lados.
#D10 : Subclasse de Dado que representa um dado de 10 lados.
#D12 : Subclasse de Dado que representa um dado de 12 lados.
#D20 : Subclasse de Dado que representa um dado de 20 lados.
#Toda classe deve implementar métodos __str__ e __repr__ para facilitar a visualização
#dos objetos.
#Implemente um método __eq__ para comparar dois personagens, considerando o nome e a classe.
#Implemente todos os métodos necessários para garantir que a classe Dado possa ser
#comparada com outros dados ( D20 > D12 , D4 <= D10 , ...).
#O sistema deve ser capaz de lidar com erros, como por exemplo, quando um personagem
#carregado do arquivo possui mais habilidades que o permitido pela classe.
#Os erros devem ser registrados em um arquivo de log, que deve conter uma explicação sobre o erro.
#O sistema deve gerar um relatório de combate, que deve conter o nome dos personagens,
#o dano causado por cada ataque e o vencedor do combate.
#Todas as classes e métodos devem ser documentados com docstrings.
#Para usar o sistema, você deverá implementá-lo como um pacote. Ou seja, deverá criar um
#diretório chamado RPG que conterá os arquivos de classes. O script main.py deverá estar
#fora desse diretório e chamar as classes do pacote RPG