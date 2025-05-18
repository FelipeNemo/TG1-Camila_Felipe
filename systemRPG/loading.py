
"""Arquivo responsável por carregar personagens e tratamento de erros"""

import csv
from .users import *
from .errors import *
from .gaming import *
from . import constants as const

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
            blocos = conteudo.split("\n\n")

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

                    except ErroLimiteInventario as e:
                        # Salva o erro na lista erros
                        erros.append(["Limite de inventário excedido", str(e)])
                        # [CORREÇÃO] Cortando para o limite de cada subclasse 
                        classe_obj = const.CLASSES_DISPONIVEIS[classe]()  # Recria instância da subclasse
                        limite = classe_obj.limite_habilidades_padrao() # Aplica o método do limite
                        habilidades_limitadas = habilidades[:limite] # Corta segundo o limite
                        
                        # Recria o personagem com o erro corrigido
                        personagem = Personagem.criar_personagem(nome, classe, habilidades_limitadas)
                        personagens.append(personagem)

                    except ErroHabilidadeInvalida as e:
                        # Salva o erro na lista erros
                        erros.append(["Habilidade inválida", str(e)])
                        # Pega o nome da habilidade no erro  
                        habilidade_invalida = str(e).split("'")[1]
                        # Percorre retirando a list habilidades a retirando do do erro
                        habilidades_corrigidas = [h for h in habilidades if h != habilidade_invalida] 
                        
                        # Recria o personagem com o erro corrigido
                        personagem = Personagem.criar_personagem(nome, classe, habilidades_corrigidas)
                        personagens.append(personagem)

                    # ----------------------------------------------------------
                    except ErroClasseInvalida as e:
                        erros.append(["Classe inválida", str(e)])
                    except ErroInventarioVazio as e:
                        erros.append(["Inventário vazio", str(e)])                    
                    except ErroDadoAtaqueInvalido as e:
                        erros.append(["Dado de ataque inválido", str(e)])
                    except ErroPersonagemInvalido as e:
                        erros.append(["Erro personagem inválido", str(e)])
                    except ErroHabilidadeNaoEncontrada as e:
                        erros.append(["Habilidade não encontrada", str(e)])
                    except ErroNumeroPersonagem as e:
                        erros.append(["Personagens insuficiêntes para o combate", str(e)])
                    except Exception as e: # Erro global da leitura
                        erros.append([nome, str(e)])
                #else:
                    #erros.append([nome or "Desconhecido", "Dados incompletos"])

    except FileNotFoundError:
        erros.append(["Arquivo", "Não encontrado"])

    print("[DEBUG] Personagens carregados:", personagens)
    return personagens, erros
