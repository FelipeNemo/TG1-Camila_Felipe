import csv
from .gaming import *
from .users import *
from .errors import *
from .constants import *

# Função para salvar os erros em CSV
def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def carregar_personagens(caminho_arquivo):
    personagens = []
    erros = []
    nome = None
    classe = None
    habilidades = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha.startswith("### "):
                    if nome and classe and habilidades:
                        print(f"[DEBUG] Criando personagem: {nome}, {classe}, {habilidades}")
                        personagem = criar_personagem(nome, classe, habilidades)
                        if personagem:
                            personagens.append(personagem)
                        else:
                            erros.append([nome, f"Classe inválida: {classe}"])

                    # Começa um novo personagem
                    nome = linha[4:].strip()
                    classe = None
                    habilidades = []
                    print(f"[DEBUG] Nome do personagem encontrado: {nome}")

                elif linha.startswith("- **Classe**:"):
                    classe = linha.replace("- **Classe**:", "").strip()
                    print(f"[DEBUG] Classe encontrada: {classe}")

                elif linha.startswith("- **Habilidades**:"):
                    # Linha apenas de marcação, ignora
                    continue

                elif linha.startswith("-"):  
                    habilidade = linha[2:].strip()
                    habilidades.append(habilidade)
                    print(f"[DEBUG] Habilidade adicionada: {habilidade}")

            # Último personagem após o loop
            if nome and classe and habilidades:
                print(f"[DEBUG] Criando último personagem: {nome}, {classe}, {habilidades}")
                personagem = criar_personagem(nome, classe, habilidades)
                if personagem:
                    personagens.append(personagem)
                else:
                    erros.append([nome, f"Classe inválida: {classe}"])

    except FileNotFoundError:
        erros.append(["Arquivo", "Não encontrado"])
    except Exception as e:
        erros.append(["Erro inesperado", str(e)])

    print("[DEBUG] Personagens carregados:", personagens)
    return personagens, erros
