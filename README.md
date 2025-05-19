# Pacote `systemRPG`

### Estrutura do Projeto

- **`Reports/`**  
  Contém os dados de relatório e o arquivo `erros.log`.

- **`systemRPG/`**  
  Núcleo da lógica de batalha e componentes principais:
  
  - `constants.py`: Armazena constantes globais.  
  - `combate.py`: Define as funções `free_for_all()` e `combate_entre_dois()`, que utilizam a classe `Arena`.  
  - `erros.py`: Define exceções customizadas do sistema.  
  - `gaming.py`: Contém as classes `Dado`, `Habilidade` (e subclasses), e `Arena`, com métodos para gerar os dados do relatório.  
  - `loading.py`: Função `carregar_personagem()` que lida com exceções, lê o arquivo de entrada e utiliza `criar_personagem()`.  
  - `users.py`: Define a classe `Classe` (e subclasses), `Personagem`, e os métodos `criar_personagem()`, `usar_habilidade()` e `atacar()`.

- **`gameplay/`**  
  Responsável pelos elementos visuais e animações:
  
  - `graph.py`: Gera o gráfico HP x Rodada.  
  - `animation.py`: Cria animações com base nas sprints do combate a partir do relatório.

- **`main.py`**  
  Menu principal e interface.

### Importação:

```python
import systemRPG as r
import gameplay as g

r.free_for_all()
r.combate_entre_dois()
