from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Alright!")
clock = pygame.time.Clock()
Font = pygame.font.Font("UltimatePygameIntro/font/Pixeltype.ttf", 50)

sky_surf = pygame.image.load("UltimatePygameIntro/graphics/Sky.png").convert()
ground_surf = pygame.image.load("UltimatePygameIntro/graphics/ground.png").convert()

text_surf = Font.render("Score: ", False, 'Black')
text_rect = text_surf.get_rect(center=(300, 20))

snail_surface = pygame.image.load("UltimatePygameIntro/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(800, 300))

player_surf = pygame.image.load("UltimatePygameIntro/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                gravity = -20

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, (350, 20))

    snail_rect.x -= 10
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    gravity += 1
    player_rect.y += gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        exit()

    pygame.display.update()
    clock.tick(60)
