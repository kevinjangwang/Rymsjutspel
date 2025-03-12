import pygame

pygame.init()

SKARMENS_BREDD = 800
SKARMENS_HOJD = 800

skarm = pygame.display.set_mode((SKARMENS_BREDD, SKARMENS_HOJD))
pygame.display.set_caption("Space Shooter")


background_black = pygame.image.load("assets/backgrounds/bg.png")
background_stars = pygame.image.load("assets/backgrounds/Stars-A.png")
original_bild = pygame.image.load("assets/sprites/SpaceShip.png")


sprite_spelare = pygame.transform.scale(original_bild, (original_bild.get_width() // 2, original_bild.get_height() // 2))

spelare_x = SKARMENS_BREDD // 2 - sprite_spelare.get_width() // 2
spelare_y = SKARMENS_HOJD - 200
spelare_hastighet = 5


bakgrund_y = 0

spelet_kors = True
while spelet_kors:
    skarm.fill((0, 0, 30))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spelet_kors = False
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spelare_x > 0:
        spelare_x -= spelare_hastighet
    if keys[pygame.K_RIGHT] and spelare_x < SKARMENS_BREDD - sprite_spelare.get_width():
        spelare_x += spelare_hastighet
    if keys[pygame.K_UP] and spelare_y > 0:
        spelare_y -= spelare_hastighet
    if keys[pygame.K_DOWN] and spelare_y < SKARMENS_HOJD - sprite_spelare.get_height():
        spelare_y += spelare_hastighet
    
    
    skarm.blit(background_black, (0, 0))
    skarm.blit(background_stars, (0, bakgrund_y))
    skarm.blit(background_stars, (0, bakgrund_y - SKARMENS_HOJD))
    
    bakgrund_y += 2
    if bakgrund_y >= SKARMENS_HOJD:
        bakgrund_y = 0
    
    
    skarm.blit(sprite_spelare, (spelare_x, spelare_y))
    
    pygame.display.update()

pygame.quit()


