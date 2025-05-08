import csv
from .combate import *
from .users import *
from .errors import *


def salvar_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

def carregar_personagens(caminho_arquivo):
    personagens = []
    erros = []


    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            blocos = conteudo.split("\n\n")  # cada bloco representa um personagem

            for bloco in blocos:
                linhas = bloco.strip().split("\n")
                nome = None
                classe = None
                habilidades = []

                for linha in linhas:
                    linha = linha.strip()

                    if linha.startswith("### "):
                        nome = linha[4:].strip()
                        #print(f"[DEBUG] Nome do personagem encontrado: {nome}")

                    elif linha.startswith("- **Classe**:"):
                        classe = linha.replace("- **Classe**:", "").strip()
                        #print(f"[DEBUG] Classe encontrada: {classe}")

                    elif linha.startswith("- **Habilidades**:"):
                        continue

                    elif linha.startswith("-"):
                        habilidade = linha[2:].strip()
                        habilidades.append(habilidade)
                        #print(f"[DEBUG] Habilidade adicionada: {habilidade}")

                if nome and classe and habilidades:
                    personagem = Personagem.criar_personagem(nome, classe, habilidades)
                    if personagem:
                        personagens.append(personagem)
                    else:
                        erros.append([nome, f"Classe inválida: {classe}"])
                    
#print(f"[DEBUG] Criando personagem: {nome}, {classe}, {habilidades}")
                # gaming.py class Habilidade usar()
                # users.py class usar_habilidade(), atacar()

    except FileNotFoundError:
        erros.append(["Arquivo", "Não encontrado"])

    except ErroClasseInvalida as e:
        erros.append(["Classe inválida", str(e)])

    except ErroLimiteInventario as e:
        erros.append(["Limite de inventário excedido", str(e)])

    except ErroInventarioVazio as e:
        erros.append(["Inventário vazio", str(e)])

    except ErroHabilidadeInvalida as e:
        erros.append(["Habilidade inválida", str(e)]) 
    
    except ErroDadoAtaqueInvalido as e:
        erros.append(["Dado de ataque inválido", str(e)])

    except ErroPersonagemInvalido as e:
        erros.append(["Erro personagem inválido", str(e)])
    
    except ErroNumeroPersonagem as e:
        erros.append(["Personagens insuficiêntes para o combate", str(e)])

    except ErroHabilidadeNaoEncontrada as e:
        erros.append(["Erro inesperado", str(e)])

    except Exception as e:
        erros.append(["Erro inesperado", str(e)]) 

    print("[DEBUG] Personagens carregados:", personagens)
    return personagens, erros