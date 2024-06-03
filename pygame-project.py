import random
import pygame as pg

# --CONSTANTS--
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
PLAYER_SPEED = 5
PLAYER_JUMP = 15
GRAVITY = 1

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('player.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x

        # Check for collisions with platforms
        platform_hit_list = pg.sprite.spritecollide(self, platforms, False)
        for platform in platform_hit_list:
            if self.change_x > 0:
                self.rect.right = platform.rect.left
            elif self.change_x < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.change_y

        # Check for collisions with platforms
        platform_hit_list = pg.sprite.spritecollide(self, platforms, False)
        for platform in platform_hit_list:
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
                self.on_ground = True
            elif self.change_y < 0:
                self.rect.top = platform.rect.bottom
            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += GRAVITY

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height
            self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.change_y = -PLAYER_JUMP
            self.on_ground = False

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('platform.png')
        self.image = pg.transform.scale(self.image, (100, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def draw_text(surface, text, size, x, y):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_screen(screen):
    screen.fill(BLACK)
    draw_text(screen, "Press Any Key to Start", 64, WIDTH // 2, HEIGHT // 2)
    pg.display.flip()
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYUP:
                waiting = False

def main():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("Platformer Game")
    clock = pg.time.Clock()

    global platforms
    platforms = pg.sprite.Group()
    all_sprites = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    level = [
        Platform(0, HEIGHT - 40),
        Platform(200, HEIGHT - 150),
        Platform(400, HEIGHT - 300),
        Platform(600, HEIGHT - 450)
    ]

    for platform in level:
        platforms.add(platform)
        all_sprites.add(platform)

    game_over = False
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.change_x = -PLAYER_SPEED
                elif event.key == pg.K_RIGHT:
                    player.change_x = PLAYER_SPEED
                elif event.key == pg.K_SPACE:
                    player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    player.change_x = 0

        if not game_over:
            all_sprites.update()
            if player.rect.top > HEIGHT:
                game_over = True

        screen.fill(BLACK)
        all_sprites.draw(screen)

        if game_over:
            draw_text(screen, "GAME OVER", 64, WIDTH // 2, HEIGHT // 2)
            draw_text(screen, "Press R to Restart", 32, WIDTH // 2, HEIGHT // 2 + 64)
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                main()

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    screen = pg.display.set_mode(SCREEN_SIZE)
    start_screen(screen)
    main()
