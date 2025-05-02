import csv
from .classes import *

# Função para salvar os erros em em um log
def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def carregar_personagens(caminho_arquivo):
    personagens = [] # Lista para armazenar os personagens criados com sucesso
    erros = [] # Lista para armazenar erros de leitura/formato


    try:
        # Abre o arquivo de entrada em modo de leitura com encoding UTF-8
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines() # ler linha por linha

        for linha in linhas: # percorre linhas dando strip
            linha = linha.strip() # remove extra whitespaces and specified characters from the start 

            if not linha: # se não tem linha
                continue  # pula linhas em branco

            partes = linha.split(";") # deve ser dividido por :

            if len(partes) < 3:
                erros.append([linha, "Formato inválido"])
                continue

            #if "###" in linhas:
                
           # if "- **Classe**:" é uma classe
           # if "- **Habilidades**:" mostra as habilidades do inventário

            nome = partes[0].strip()
            classe = partes[1].strip()
            # adicionar habilidade
            inventario = [item.strip() for item in partes[2].split(",") if item.strip()]

            personagem = criar_personagem(nome, classe, inventario)

            if personagem:
                personagens.append(personagem)# Se a criação for bem-sucedida, adiciona à lista
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
    
def combate_entre_dois(): # combate entre dois/ uelo
    pass

def combate_free_for_all(): # combate entre vários/arena
    pass

def get_relatorio_combates(): # Relatório dos combates feitos
    pass