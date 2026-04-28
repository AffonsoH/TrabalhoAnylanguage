import pygame
import sys

pygame.init()

cores = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "preto": (0, 0, 0)
}

x = 0
y = 0
velocidade = 5
keys = pygame.key.get_pressed()
retangulo = pygame.Rect(x, y, 50, 50)


tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("SDSA")

pygame.draw.rect(tela, cores["vermelho"], retangulo)

relogio = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  x -= velocidade
    if teclas[pygame.K_RIGHT]: x += velocidade
    if teclas[pygame.K_UP]:    y -= velocidade
    if teclas[pygame.K_DOWN]:  y += velocidade
    tela.fill(cores["preto"])
    pygame.draw.rect(tela, cores["vermelho"], pygame.Rect(x, y, 50, 50))
    pygame.display.flip()
    relogio.tick(60)
            
pygame.quit()
sys.exit()