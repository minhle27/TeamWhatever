import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Scary Game')
clock = pygame.time.Clock()

start_font = pygame.font.Font('punktype/Punktype.ttf', 50)
start_surface = start_font.render('PRESS SPACE TO RETURN TO CAMP', False, 'Red')
start_rect = start_surface.get_rect(midbottom = (960,900))

win_font = pygame.font.Font('punktype/Punktype.ttf', 50)
win_surface = win_font.render('YOU SURVIVED', False, 'Red')
win_rect = win_surface.get_rect(midbottom = (960,900))

lose_font = pygame.font.Font('punktype/Punktype.ttf', 50)
lose_surface = lose_font.render('YOU DIED', False, 'Red')
lose_rect = lose_surface.get_rect(midbottom = (960,900))



camp_surf = pygame.image.load('Graphics/Campsite.png').convert()
destroyed_surf = pygame.image.load('Graphics/Campsite(2).png').convert()
garden_surf = pygame.image.load('Graphics/Garden.png').convert()
garden_surf = pygame.transform.scale(garden_surf, (1920,1080))
stone_surf = pygame.image.load('Graphics/stone.png')
stone_surf = pygame.transform.scale(stone_surf, (1920,1080))

player_surf = pygame.image.load('Graphics/characterV2.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (960,1000))

lantern_surf = pygame.image.load('Graphics/lanternfly.png').convert_alpha()
lantern_rect = lantern_surf.get_rect(midtop = (960,200))

gotkey = False


stage = 0
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player_speed = 6
    
    if game_active:
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player_rect.top > 0:
            player_rect.y -= player_speed
        if keys[pygame.K_s] and player_rect.bottom < 1080:
            player_rect.y += player_speed
        if keys[pygame.K_a] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_d] and player_rect.right < 1920:
            player_rect.x += player_speed

        
        
        if stage == 1:
            
            #print(player_rect.center)
            #900x 200y

            screen.blit(destroyed_surf,(0,0))
            screen.blit(player_surf,player_rect)
            
            if player_rect.collidepoint(900,200):
                stage = 3 #change later to 2
                player_rect.bottomleft = (1200, 1080)

                key_surf = pygame.image.load('Graphics/key.png').convert_alpha()
                key_surf = pygame.transform.scale(key_surf, (50,50))
                key_rect = key_surf.get_rect(midtop = (960,200))

                gate_surf = pygame.image.load('Graphics/gate.png').convert_alpha()
                gate_surf = pygame.transform.scale(gate_surf, (300,200))
                gate_rect = gate_surf.get_rect(midleft = (0,500))

                lock_surf = pygame.image.load('Graphics/lock.png').convert_alpha()
                lock_surf = pygame.transform.scale(lock_surf, (50,50))
                lock_rect = lock_surf.get_rect(center = gate_rect.center)



        if stage == 2:

            screen.blit(garden_surf,(0,0))
            screen.blit(player_surf,player_rect)
            screen.blit(lantern_surf)

        if stage == 3:
            lantern_speed = 2
        

            if lantern_rect.centerx < player_rect.centerx:
                lantern_rect.x += lantern_speed
            elif lantern_rect.centerx > player_rect.centerx:
                lantern_rect.x -= lantern_speed
            if lantern_rect.centery < player_rect.centery:
                lantern_rect.y += lantern_speed
            elif lantern_rect.centery > player_rect.centery:
                lantern_rect.y -= lantern_speed

            if player_rect.colliderect(lantern_rect):
                game_active = False
                stage = -1

            screen.blit(garden_surf,(0,0))

            screen.blit(gate_surf, gate_rect)

            if gotkey == False: 
                screen.blit(lock_surf,lock_rect)
                screen.blit(key_surf,key_rect)

            if player_rect.colliderect(key_rect):
                gotkey = True

            if gotkey and player_rect.colliderect(gate_rect):
                stage = -2
                game_active = False

            screen.blit(lantern_surf,lantern_rect)
            screen.blit(player_surf,player_rect)
            
            
    
    else:
        if stage == 0:
            screen.blit(camp_surf,(0,0))
            screen.blit(start_surface, start_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_active = True
                stage = 1
        elif stage == -1:
            screen.blit(destroyed_surf, (0,0))
            screen.blit(lose_surface,lose_rect)
        elif stage == -2:
            screen.blit(camp_surf, (0,0))
            screen.blit(win_surface, win_rect)


    #leave at end, updates and draws everything
    pygame.display.update()
    clock.tick(60)

