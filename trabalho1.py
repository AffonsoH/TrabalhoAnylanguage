import pygame
import sys

pygame.init()

pygame.font.init()
fonte = pygame.font.SysFont("Arial", 24, bold=True)


cores = {
    "vermelho": (255, 0, 0),
    "azul": (0, 0, 255),
    "preto": (0, 0, 0),
    "amarelo": (255, 255, 0),
    "cinza": (100, 100, 100)
}

x = 400
y = 50
velocidade = 5
keys = pygame.key.get_pressed()
retangulo = pygame.Rect(x, y, 50, 50)

x2 = 400
y2 = 750
velocidade2 = 5

hpPlayer1 = 100
hpPlayer2 = 100

balas = []
balas2 = []
velocidade_bala = 10
stun_player1 = 0

direcao1 = [0, 1]
direcao2 = [0, -1]

socos = []
velocidade_socos = 30

player1 = pygame.Rect(x, y, 50, 50)
player2 = pygame.Rect(x2, y2, 50, 50)

cooldown_tiro = 1500
ultimo_tiro = 0

tamanho_tela = (800, 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("SDSA")

pygame.draw.rect(tela, cores["vermelho"], retangulo)

img_p1 = pygame.image.load(r'C:\Users\aluno\Downloads\player1.jpg')
img_p2 = pygame.image.load(r'C:\Users\aluno\Downloads\player2.jpg')

img_p1 = pygame.transform.scale(img_p1, (50, 50))
img_p2 = pygame.transform.scale(img_p2, (50, 50))

img_gameover = pygame.image.load(r'C:\Users\aluno\Downloads\gameover2.jpg')
img_gameover = pygame.transform.scale(img_gameover, tamanho_tela)

img_gameover2 = pygame.image.load(r'C:\Users\aluno\Downloads\gameover1.jpg')
img_gameover2 = pygame.transform.scale(img_gameover2, tamanho_tela)

relogio = pygame.time.Clock()

rodando = True
while rodando:
    tempo_atual = pygame.time.get_ticks()
    
    if hpPlayer1 <= 0 or hpPlayer2 <= 0:
        tela.fill(cores["preto"])
        if hpPlayer1 <= 0:
            tela.blit(img_gameover, (0, 0))
        elif hpPlayer2 <= 0:
            tela.blit(img_gameover2, (0, 0))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        continue
        
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                if tempo_atual - ultimo_tiro > cooldown_tiro:
                    nova_bala = pygame.Rect(player2.centerx - 5, player2.top, 10, 20)
                    balas.append(nova_bala)
                    ultimo_tiro = tempo_atual
                    
                    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e:
                nova_bala2 = pygame.Rect(player2.centerx - 5, player2.top, 10, 20)
                balas2.append({
    "rect": nova_bala2, 
    "tempo": tempo_atual, 
    "vel_x": direcao2[0] * velocidade_bala, 
    "vel_y": direcao2[1] * velocidade_bala
})
                
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RSHIFT:
                novo_soco = pygame.Rect(player1.centerx - 5, player1.top, 10, 20)
                socos.append({
                    "rect": novo_soco, 
                    "tempo": tempo_atual, 
                    "vel_x": direcao1[0] * velocidade_socos, 
                    "vel_y": direcao1[1] * velocidade_socos
})                  
            
    pos_antiga1 = player1.topleft
    pos_antiga2 = player2.topleft
    
    teclas = pygame.key.get_pressed()
    

    if tempo_atual > stun_player1:
       if teclas[pygame.K_LEFT]:  
            x -= velocidade
            direcao1 = [-1, 0]
       if teclas[pygame.K_RIGHT]: 
            x += velocidade
            direcao1 = [1, 0]
       if teclas[pygame.K_UP]:    
            y -= velocidade
            direcao1 = [0, -1]
       if teclas[pygame.K_DOWN]:  
            y += velocidade
            direcao1 = [0, 1]
    
    if teclas[pygame.K_a]: 
        x2 -= velocidade
        direcao2 = [-1, 0]
    if teclas[pygame.K_d]: 
        x2 += velocidade
        direcao2 = [1, 0]
    if teclas[pygame.K_w]: 
        y2 -= velocidade
        direcao2 = [0, -1]
    if teclas[pygame.K_s]: 
        y2 += velocidade
        direcao2 = [0, 1]
    player1.topleft = (x, y)
    player2.topleft = (x2, y2)
    
    if player1.colliderect(player2):
        x, y = pos_antiga1
        x2, y2 = pos_antiga2
        player1.topleft = (x, y)
        player2.topleft = (x2, y2)
        
    for bala in balas[:]:
        bala.y -= velocidade_bala 
        
        if bala.colliderect(player1):
            stun_player1 = tempo_atual + 1000 
            balas.remove(bala)
        elif bala.y < 0: 
            balas.remove(bala)
            
    for bala2 in balas2[:]:
        bala2["rect"].x += bala2["vel_x"]
        bala2["rect"].y +=bala2["vel_y"]
        
        if bala2["rect"].colliderect(player1):
            balas2.remove(bala2)
            hpPlayer1 -= 7
            
        elif bala2["rect"].y < 0:
            balas2.remove(bala2)
    
    for soco in socos[:]:
        soco["rect"].x += soco["vel_x"]
        soco["rect"].y += soco["vel_y"]
        if tempo_atual - soco["tempo"] > 50:
            socos.remove(soco)
        elif soco["rect"].colliderect(player2):
            socos.remove(soco)
            hpPlayer2 -= 14
    
    tela.fill(cores["preto"])
    tela.blit(img_p1, player1)
    tela.blit(img_p2, player2)
    
    texto_hp1 = fonte.render(f"HP P1: {hpPlayer1}", True, (255, 255, 255))
    texto_hp2 = fonte.render(f"HP P2: {hpPlayer2}", True, (255, 255, 255))
    
    tela.blit(texto_hp1, (10, 10))  
    tela.blit(texto_hp2, (10, 40))
    
    for bala in balas:
        pygame.draw.rect(tela, cores["amarelo"], bala)
        
    for bala2 in balas2:
        pygame.draw.rect(tela, cores["cinza"], bala2["rect"])
        
    for soco in socos:
        pygame.draw.rect(tela, cores["vermelho"], soco["rect"])
    
    pygame.display.flip()
    relogio.tick(60)


            
pygame.quit()
sys.exit()