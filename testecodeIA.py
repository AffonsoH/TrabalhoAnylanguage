import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
x, y = 400, 300  # Posição inicial
velocidade = 5
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Captura as teclas pressionadas para movimento contínuo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  x -= velocidade
    if teclas[pygame.K_RIGHT]: x += velocidade
    if teclas[pygame.K_UP]:    y -= velocidade
    if teclas[pygame.K_DOWN]:  y += velocidade

    tela.fill((0, 0, 0)) # Limpa a tela
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50)) # Desenha o retangulo
    pygame.display.update()
    pygame.time.Clock().tick(60) # Limita a 60 FPS
