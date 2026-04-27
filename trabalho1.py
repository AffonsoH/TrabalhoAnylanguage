import pygame
import sys

pygame.init()

pygame.display.flip()

cores = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "preto": (0, 0, 0)
}


tamanho_tela = (500, 500)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("SDSA")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
pygame.quit()
sys.exit()