from .gaming import *
from .users import *
def combate_entre_dois(personagens):
    print("Escolha dois personagens para o combate:")
    for i, p in enumerate(personagens):
        print(f"{i} - {p.nome} ({p.classe})")

    idx1 = int(input("Escolha o primeiro personagem: "))
    idx2 = int(input("Escolha o segundo personagem: "))

    p1 = personagens[idx1]
    p2 = personagens[idx2]

    rodada_combate(p1, p2)  # função interativa em gaming.py

def combate_free_for_all(personagens):
    print("Iniciando combate entre todos os personagens!")
    # Exemplo simples:
    while len(personagens) > 1:
        p1 = personagens[0]
        p2 = personagens[1]
        rodada_combate(p1, p2)
        # Lógica de eliminar quem perde, etc...

def rodada_combate(p1, p2):
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\n{p1.nome} vs {p2.nome}")
        print(f"{p1.nome}, escolha sua habilidade:")
        habilidade = escolher_habilidade(p1)
        p1.usar_habilidade(habilidade, p2)
        if not p2.esta_vivo():
            print(f"{p2.nome} foi derrotado!")
            break
        print(f"{p2.nome}, escolha sua habilidade:")
        habilidade = escolher_habilidade(p2)
        p2.usar_habilidade(habilidade, p1)

        if not p1.esta_vivo():
            print(f"{p1.nome} foi derrotado!")
            break

def escolher_habilidade(personagem):
    for i, h in enumerate(personagem.inventario):
        print(f"{i} - {h}")
    idx = int(input("Escolha o índice da habilidade: "))
    return personagem.inventario[idx]
