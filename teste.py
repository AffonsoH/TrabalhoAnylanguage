import pygame

pygame.init()

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("TítuloTop")


tamanho_bola = 15
bola = pygame.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0, 750, tamanho_jogador, 15)

qtde_blocos_linha = 8
qtde_linhas_debloco = 5
qtde_total = qtde_blocos_linha * qtde_linhas_debloco

def criar_bloco(qtd_blocos_por_linha, qtde_linhas_deblocos):
    blocos = []
    bloco = pygame.Rect(50, 50, 80, 15)
    blocos.append(bloco)
    return blocos

cores = {
    "Branco": (255, 255, 255),
    "Preto": (0, 0, 0),
    "Amarelo": (255, 255, 0),
    "Azul": (0, 0, 255),
    "Verde": (0, 255, 0)
}

fim_jogo = False
pontuacao = 0
velocidade_bola = [1, 1]

def desenhar_inicio_do_jogo():
   tela.fill(cores["Preto"])
   pygame.draw.rect(tela, cores["Azul"], jogador)
   pygame.draw.rect(tela, cores["Branco"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["Verde"], bloco)

desenhar_inicio_do_jogo()
blocos = criar_bloco(qtde_blocos_linha, qtde_linhas_debloco)

criar_bloco(blocos)

while not fim_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit