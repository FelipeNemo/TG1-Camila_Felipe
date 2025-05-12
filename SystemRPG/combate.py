"""Funções para manipular as rodadas dos combates"""

#from .errors import *
from .gaming import *
from .users import *


def combate_entre_dois(personagens):
    print("Escolha dois personagens para o combate:")
    for i, p in enumerate(personagens):
        print(f"{i} - {p.nome} ({p.classe})")

    idx1 = int(input("\nEscolha o primeiro personagem: "))
    idx2 = int(input("\nEscolha o segundo personagem: "))
        
    p1 = personagens[idx1]
    p2 = personagens[idx2]

    print(f"\n * {p1.nome}")
    p1.exibir_status()

    print(f"\n * {p2.nome}")
    p2.exibir_status()

    # Cria arena apenas com os dois
    arena = Arena([p1, p2])
    vencedor = arena.combate()

    print(f"\n🏆 Vencedor: {vencedor.nome} {vencedor.exibir_status()}!")
    return arena.relatorio


def combate_free_for_all(personagens):
    arena = Arena([])  # Começa com arena vazia
    print("Escolha os personagens que participarão do combate:")
    for i, p in enumerate(personagens):
        print(f"{i} - {p.nome} ({p.classe})")
        p.exibir_status()

    indices_escolhidos = input("\nDigite os números dos personagens separados por vírgula (ex: 0,2,3):\n")
    indices_escolhidos = [int(i.strip()) for i in indices_escolhidos.split(',')]

    for idx in indices_escolhidos:
        arena.adicionar_personagem(personagens[idx])

    print("\nEscolha qual personagem você deseja controlar:")
    for i, p in enumerate(arena.personagens):
        print(f"{i} - {p.nome} ({p.classe})")
        p.exibir_status()

    jogador_idx = int(input("\nDigite o número do seu personagem:\n"))
    jogador = arena.personagens[jogador_idx]

    print(f"\nVocê escolheu: {jogador.nome} ({jogador.classe})")
    jogador.exibir_status()

    # Inicia o combate automático (sem perguntar se usa habilidade)
    vencedor = arena.combate()

    print(f"\nO vencedor foi: {vencedor.nome} ({vencedor.classe})")
    return arena.relatorio


def rodada_combate(p1, p2):
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\n{p1.nome} vs {p2.nome}")
        dano = p1.atacar(p2)
        print(f"{p1.nome} atacou {p2.nome} e causou {dano} de dano!")
        
        if not p2.esta_vivo():
            print(f"{p2.nome} foi derrotado!")
            break

        dano = p2.atacar(p1)
        print(f"{p2.nome} atacou {p1.nome} e causou {dano} de dano!")

        if not p1.esta_vivo():
            print(f"{p1.nome} foi derrotado!")
            break


def escolher_habilidade(personagem):
    for i, h in enumerate(personagem.inventario):
        print(f"{i} - {h}")
    idx = int(input("Escolha o índice da habilidade: "))
    return personagem.inventario[idx]
