import pygame
import sys

pygame.init()

cores = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "preto": (0, 0, 0)
}

x = 400
y = 50
velocidade = 5
keys = pygame.key.get_pressed()
retangulo = pygame.Rect(x, y, 50, 50)

x2 = 400
y2 = 750
velocidade2 = 5
balas = []
velocidade_bala = 10
stun_player1 = 0

player1 = pygame.Rect(x, y, 50, 50)
player2 = pygame.Rect(x2, y2, 50, 50)

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("SDSA")

pygame.draw.rect(tela, cores["vermelho"], retangulo)

relogio = pygame.time.Clock()

rodando = True
while rodando:
    tempo_atual = pygame.time.get_ticks()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Cria um Rect para a bala saindo do Player 2 (Azul) para cima
                nova_bala = pygame.Rect(player2.centerx - 5, player2.top, 10, 20)
                balas.append(nova_bala)
            
    pos_antiga1 = player1.topleft
    pos_antiga2 = player2.topleft
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:  x -= velocidade
    if teclas[pygame.K_RIGHT]: x += velocidade
    if teclas[pygame.K_UP]:    y -= velocidade
    if teclas[pygame.K_DOWN]:  y += velocidade
    tela.fill(cores["preto"])
    
    if teclas[pygame.K_a]: x2 -= velocidade
    if teclas[pygame.K_d]: x2 += velocidade
    if teclas[pygame.K_w]: y2 -= velocidade
    if teclas[pygame.K_s]: y2 += velocidade
    
    player1.topleft = (x, y)
    player2.topleft = (x2, y2)
    
    if player1.colliderect(player2):
        x, y = pos_antiga1
        x2, y2 = pos_antiga2
        player1.topleft = (x, y)
        player2.topleft = (x2, y2)
    
    pygame.draw.rect(tela, cores["azul"], (x2, y2, 50, 50))
    pygame.draw.rect(tela, cores["vermelho"], pygame.Rect(x, y, 50, 50))
    pygame.display.flip()
    relogio.tick(60)
            
pygame.quit()
sys.exit()