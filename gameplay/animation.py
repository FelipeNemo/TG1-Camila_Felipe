# animacao.py
import pygame
import time

def mostrar_batalha(relatorio, sprites):
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Animação da Batalha RPG")

    # Carregando imagens dos personagens
    imagens = {nome: pygame.image.load(path).convert_alpha() for nome, path in sprites.items()}

    clock = pygame.time.Clock()
    rodando = True
    index = 0

    while rodando:
        tela.fill((0, 0, 0))

        if index < len(relatorio):
            evento = relatorio[index]
            # Mostrar os personagens, barra de vida, ação, etc
            atacante_img = imagens[evento["atacante"]]
            defensor_img = imagens[evento["defensor"]]
            tela.blit(atacante_img, (100, 300))
            tela.blit(defensor_img, (600, 300))

            fonte = pygame.font.SysFont(None, 32)
            texto = fonte.render(f"{evento['atacante']} causou {evento['dano']} em {evento['defensor']}", True, (255, 255, 255))
            tela.blit(texto, (200, 50))

            index += 1
            time.sleep(1.5)
        else:
            # Espera antes de sair
            fonte = pygame.font.SysFont(None, 48)
            fim = fonte.render("Batalha Encerrada!", True, (255, 255, 0))
            tela.blit(fim, (250, 250))
            pygame.display.update()
            time.sleep(3)
            rodando = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
