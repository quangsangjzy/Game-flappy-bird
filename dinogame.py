import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Dino Game")

# Tao Bien
bg_dinox,bg_dinoy = 0,0
dino_x, dino_y = 0, 230
tree_x, tree_y = 550, 230

bg = pygame.image.load(r'dino\dino\assets\background.jpg')
# bg = pygame.transform.scale2x(bg)
dino = pygame.image.load(r'dino\dino\assets\dinosaur.png')
tree = pygame.image.load(r'dino\dino\assets\tree.png')

# tree_x1, tree_y1 = 600, 500
x_init = 5
y_init = 10
jump = False
score = 0
game_start = True
game_font = pygame.font.Font('04B_19.TTF', 30)

# kiem tra va cham
def check_vacham():
    if dino_hcn.colliderect(tree_hcn):
        return False
    else: 
        return True


# Hien thi diem
def sroce_view():
    if game_start:
        score_f = game_font.render(f'Score: {int(score)}', True, (0, 21, 255 ))
        screen.blit(score_f, (250,50))
    else:
        score_f = game_font.render(f'Score: {int(score)}', True, (0, 21, 255 ))
        screen.blit(score_f, (250,50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_start:
                if dino_y == 230:
                    jump = True
            if event.key == pygame.K_SPACE and game_start == False:
                game_start = True
                score = 0
    clock.tick(70)

    if game_start:
       # backdround
        screen.blit(bg, (bg_dinox,bg_dinoy))
        screen.blit(bg, (bg_dinox+600,bg_dinoy))
        bg_dinox -= x_init
        if bg_dinox == -600: bg_dinox = 0
            # tree
        screen.blit(tree, (tree_x, tree_y))
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        # screen.blit(tree1, (tree_x1, tree_y1))
        tree_x -= x_init
        if tree_x == -20: tree_x = 550

        # dino
        screen.blit(dino, (dino_x,dino_y))
        dino_hcn = screen.blit(dino, (dino_x,dino_y))
        if dino_y>=90 and jump:
            dino_y -= y_init
        else: 
            jump = False
        if dino_y < 230 and jump== False:
            dino_y += y_init
        score += 0.1
        sroce_view()
        game_start = check_vacham()
    else:
        bg_dinox,bg_dinoy = 0,0
        dino_x, dino_y = 0, 230
        tree_x, tree_y = 550, 230
        bg_hcn = bg.get_rect(center = (bg_dinox, bg_dinoy))
        dino_hcn = dino.get_rect(center = (dino_x, dino_y))
        tree_hcn = dino.get_rect(center = (tree_x, tree_y))
        score = 0
        sroce_view()
    pygame.display.update()