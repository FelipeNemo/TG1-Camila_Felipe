
# _------------------------------------------------------------------------
"""Arquivo responsável por carregar personagens e tratamento de erros"""

import csv
from .users import *
from .errors import *
from .gaming import *

# ------------------------------------

def salvar_log(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

# ------------------------------------

def carregar_personagens(caminho_arquivo):
    personagens = []
    erros = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            blocos = conteudo.split("\n\n")  # cada bloco representa um personagem e é separado por \n 

            for bloco in blocos:
                linhas = bloco.strip().split("\n")
                nome = None
                classe = None
                habilidades = []

                for linha in linhas:
                    linha = linha.strip()

                    if linha.startswith("### "):
                        nome = linha[4:].strip()

                    elif linha.startswith("- **Classe**:"):
                        classe = linha.replace("- **Classe**:", "").strip()

                    elif linha.startswith("- **Habilidades**:"):
                        continue

                    elif linha.startswith("-"):
                        habilidade = linha[2:].strip()
                        habilidades.append(habilidade)

                if nome and classe and habilidades:
                    try:
                        personagem = Personagem.criar_personagem(nome, classe, habilidades)
                        personagens.append(personagem)

                    except ErroHabilidadeInvalida as e:
                        # Trata habilidades inválidas
                        habilidades_validas = [
                            h for h in habilidades 
                            if h in ["BolaDeFogo", "Cura", "Tiro de Arco"]
                        ]
                        erros.append([nome, f"{str(e)} — habilidades filtradas: {habilidades_validas}"])
                        # Tenta criar novamente com habilidades filtradas
                        try:
                            personagem = Personagem.criar_personagem(nome, classe, habilidades_validas)
                            personagens.append(personagem)
                        except Exception as e2:
                            erros.append([nome, f"Erro após tentar corrigir habilidades: {str(e2)}"])

                    except ErroLimiteInventario as e:
                        erros.append([nome, f"{str(e)} — habilidades antes: {habilidades}"])
                        habilidades_limitadas = habilidades[:Personagem._classe.limite_habilidades]

                        try:
                            personagem = Personagem.criar_personagem(nome, classe, habilidades_limitadas)
                            personagens.append(personagem)
                            erros.append([nome, f"ErroLimiteInventario tratado — habilidades limitadas: {habilidades_limitadas}"])
                        except Exception as e3:
                            erros.append([nome, f"Erro após tentar limitar habilidades: {str(e3)}"])


                    except ErroClasseInvalida as e:
                        erros.append([nome, str(e)])

                    except Exception as e:
                        erros.append([nome, f"Erro inesperado ao criar personagem: {str(e)}"])

                    except FileNotFoundError:
                        erros.append(["Arquivo", "Não encontrado"])

    except ErroLeituraArquivo as e:
        erros.append(["Erro inesperado na leitura do arquivo", str(e)])

    print("[DEBUG] Personagens carregados:", personagens)
    return personagens, erros
