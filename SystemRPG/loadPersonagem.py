import csv
from .classes import *

# Função para salvar os erros em CSV
def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def carregar_personagens(caminho_arquivo):
    personagens = []
    erros = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            linha = linha.strip()

            if not linha:
                continue  # pula linhas em branco

            partes = linha.split(";")

            if len(partes) < 3:
                erros.append([linha, "Formato inválido"])
                continue

            nome = partes[0].strip()
            classe = partes[1].strip()
            inventario = [item.strip() for item in partes[2].split(",") if item.strip()]

            personagem = criar_personagem(nome, classe, inventario)

            if personagem:
                personagens.append(personagem)
            else:
                erros.append([nome, f"Classe inválida: {classe}"])

    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")

    return personagens, erros

def criar_personagem(nome, classe, inventario):
    if classe.lower() == "guerreiro":
        return Guerreiro(nome, classe, inventario)
    elif classe.lower() == "mago":
        return Mago(nome, classe, inventario)
    elif classe.lower() == "arqueiro":
        return Ladino(nome, classe, inventario)
    else:
        return None
