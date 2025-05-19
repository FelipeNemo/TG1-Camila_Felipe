# Pacote systemRPG

Reports → Dados do relatório e erros.log.

SystemRPG → lógica de batalha e arquivos.

constants.py: Guarda as constantes.

combate.py: Guarda as funções free_for_all() e um_contra_um() que utilizam a classe Arena.

erros.py: Guarda classes de erros elevados do sistema.

gaming.py: Guarda a classe Dado, Habilidade e suas subclasses e Arena com os métodos necessários para gerar os dados que vão gerar o relatório.

loading.py: Função carregar_personagem() que estabelece as exceções lê o arquivo de entrada, e usa a função criar_personagem().

users.py: Guarda a classe Classe e suas subclasses, classe Personagem e métodos criar_personagem(), usar_habilidade() e atacar().
 
gameplay → animação, visual.

graph.py faz o gráfico HP x Rodada
animation.py faz animação usando as sprints de combate com base no relatório.

main.py → menu/interação

import systemRPG as e
import gameplay as g

e aplica as funções free_for_all() e um_contra_um()



 