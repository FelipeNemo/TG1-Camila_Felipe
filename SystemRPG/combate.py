"""Funções para manipular as rodadas dos combates"""


from .gaming import *
from .users import *


def combate_entre_dois(personagens):
    print("Escolha dois personagens para o combate:")
    for i, p in enumerate(personagens):
        print(f"{i} - {p.nome} ({p.classe})")

    idx1 = int(input("\nEscolha o primeiro personagem:\n"))
    idx2 = int(input("\nEscolha o segundo personagem:\n"))
    
    p1 = personagens[idx1]
    
    p2 = personagens[idx2]
    print(f"\n * {p1.nome}")
    p1.exibir_status()
    print(f"\n* {p2.nome}")
    p2.exibir_status()

    rodada_combate(p1, p2)

    return p1, p2

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
        print(f"\n{p1.nome}, escolha sua habilidade:")
        p1.exibir_status()
        habilidade = escolher_habilidade(p1)
        p1.usar_habilidade(habilidade, p2)
        
        if not p2.esta_vivo():
            print(f"{p2.nome} foi derrotado!")
            break
        
        print(f"\n{p2.nome}, escolha sua habilidade:")
        p2.exibir_status()
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

def get_relatorio_combates(p1, p2):
    relatorio = []
    relatorio.append(f"--- RELATÓRIO DE COMBATE ---")
    relatorio.append(f"Personagens: {p1.nome} ({p1.classe}) vs {p2.nome} ({p2.classe})\n")

    rodada = 1
    while p1.esta_vivo() and p2.esta_vivo():
        relatorio.append(f"--- Rodada {rodada} ---")

        # Turno do p1
        relatorio.append(f"\n{p1.nome} (Vida: {p1.vida}) escolhe sua habilidade:")
        for i, h in enumerate(p1.inventario):
            relatorio.append(f"{i} - {h}")
        idx1 = int(input(f"\n{p1.nome}, escolha o índice da habilidade: "))
        habilidade1 = p1.inventario[idx1]
        relatorio.append(f"{p1.nome} usou {habilidade1.nome} em {p2.nome}")
        p1.usar_habilidade(habilidade1, p2)
        relatorio.append(f"Status de {p2.nome}: Vida = {p2.vida}")

        if not p2.esta_vivo():
            relatorio.append(f"{p2.nome} foi derrotado!")
            break

        # Turno do p2
        relatorio.append(f"\n{p2.nome} (Vida: {p2.vida}) escolhe sua habilidade:")
        for i, h in enumerate(p2.inventario):
            relatorio.append(f"{i} - {h}")
        idx2 = int(input(f"\n{p2.nome}, escolha o índice da habilidade: "))
        habilidade2 = p2.inventario[idx2]
        relatorio.append(f"{p2.nome} usou {habilidade2.nome} em {p1.nome}")
        p2.usar_habilidade(habilidade2, p1)
        relatorio.append(f"Status de {p1.nome}: Vida = {p1.vida}")

        if not p1.esta_vivo():
            relatorio.append(f"{p1.nome} foi derrotado!")
            break

        rodada += 1

    relatorio.append("\n--- FIM DO COMBATE ---\n")
    vencedor = p1.nome if p1.esta_vivo() else p2.nome
    relatorio.append(f"VENCEDOR: {vencedor}")
    
    return "\n".join(relatorio)
