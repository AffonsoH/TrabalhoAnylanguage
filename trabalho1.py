import pygame
import pymunk
pygame.init()

cores = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "preto": (0, 0, 0)
}


tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("SDSA")
