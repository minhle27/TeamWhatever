import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Scary Game')
clock = pygame.time.Clock()

start_font = pygame.font.Font('punktype/Punktype.ttf', 50)
start_surface = start_font.render('PRESS SPACE TO RETURN TO CAMP', False, 'Red')
start_rect = start_surface.get_rect(midbottom = (960,900))

camp_surf = pygame.image.load('Graphics/Campsite.png').convert()
destroyed_surf = pygame.image.load('Graphics/Campsite(2).png').convert()



player_surf = pygame.image.load('Graphics/characterV2.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (960,1000))

stage = 0
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player_speed = 5
    
    if game_active:
        if stage == 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player_rect.top > 0:
                player_rect.y -= player_speed
            if keys[pygame.K_s] and player_rect.bottom < 1080:
                player_rect.y += player_speed
            if keys[pygame.K_a] and player_rect.left > 0:
                player_rect.x -= player_speed
            if keys[pygame.K_d] and player_rect.right < 1920:
                player_rect.x += player_speed

            #print(player_rect.center)
            #900x 200y
            
            if player_rect.collidepoint(900,200):
                stage = 2


            screen.blit(destroyed_surf,(0,0))
            screen.blit(player_surf,player_rect)
    
    else:
        if stage == 0:
            
            screen.blit(camp_surf,(0,0))
            screen.blit(start_surface, start_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_active = True
                stage = 1




    #leave at end, updates and draws everything
    pygame.display.update()
    clock.tick(60)

