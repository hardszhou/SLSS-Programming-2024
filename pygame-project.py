# platformer-game.py
# Simple platformer game

import pygame as pg

# --CONSTANTS--
# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
PLAYER_SPEED = 5
PLAYER_JUMP = 15
GRAVITY = 1
DOUBLE_JUMP_TIME = 500  # Time window for double jump in milliseconds
SPIKE_HEIGHT = 10

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)  # Initial position away from spikes and goal
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.last_jump_time = 0

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x

        # Prevent the player from moving outside the screen boundaries
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

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
                self.jump_count = 0  # Reset jump count when landing
            elif self.change_y < 0:
                self.rect.top = platform.rect.bottom
            self.change_y = 0

        # Check for collisions with spikes
        spike_hit_list = pg.sprite.spritecollide(self, spikes, False)
        if spike_hit_list:
            self.kill()  # Game over if player hits a spike

        # Check for collisions with goal
        goal_hit_list = pg.sprite.spritecollide(self, goals, False)
        if goal_hit_list:
            for goal in goal_hit_list:
                goal.kill()  # Remove the goal from the game

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += GRAVITY

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height
            self.on_ground = True
            self.jump_count = 0  # Reset jump count when landing

    def jump(self):
        current_time = pg.time.get_ticks()
        if self.on_ground or (self.jump_count < 2 and current_time - self.last_jump_time < DOUBLE_JUMP_TIME):
            self.change_y = -PLAYER_JUMP
            self.on_ground = False
            self.jump_count += 1
            self.last_jump_time = current_time

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width=200, height=20):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spike(pg.sprite.Sprite):
    def __init__(self, x, y, width=50):
        super().__init__()
        self.image = pg.Surface((width, SPIKE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - SPIKE_HEIGHT  # Adjust the y position to be on top of the platform

class Goal(pg.sprite.Sprite):
    def __init__(self, x, y, width=30, height=30):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - height  # Adjust the y position to be on top of the platform

def draw_text(surface, text, size, x, y):
    font = pg.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def start_screen(screen):
    screen.fill(BLACK)
    draw_text(screen, "Press Any Key to Start", 64, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Arrow Keys to Move, Space to Jump (Double tap for double jump)", 32, WIDTH // 2, HEIGHT // 2 + 64)
    pg.display.flip()
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYUP:
                waiting = False

def end_screen(screen, message):
    screen.fill(BLACK)
    draw_text(screen, message, 64, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Press R to Restart", 32, WIDTH // 2, HEIGHT // 2 + 64)
    pg.display.flip()
    waiting = True
    while waiting:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYUP:
                if event.key == pg.K_r:
                    main()

def main():
    pg.init()
    pg.font.init()  # Initialize the font module
    screen = pg.display.set_mode(SCREEN_SIZE)
    pg.display.set_caption("Platformer Game")
    clock = pg.time.Clock()

    global platforms, spikes, goals
    platforms = pg.sprite.Group()
    spikes = pg.sprite.Group()
    goals = pg.sprite.Group()
    all_sprites = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    # Adjusted platform positions to make them easier to reach
    level = [
        Platform(0, HEIGHT - 40, WIDTH, 40),  # Ground platform
        Platform(100, HEIGHT - 140),  # First platform
        Platform(300, HEIGHT - 240),  # Second platform
        Platform(500, HEIGHT - 340),  # Third platform
        Platform(200, HEIGHT - 440),  # Fourth platform
        Platform(400, HEIGHT - 540),  # Fifth platform
    ]

    for platform in level:
        platforms.add
        platforms.add(platform)
        all_sprites.add(platform)

    # Add spikes on platforms, ensuring they are on top of the platform
    spikes.add(Spike(350, HEIGHT - 240))  # Adjusted position
    spikes.add(Spike(550, HEIGHT - 340))  # Adjusted position
    spikes.add(Spike(250, HEIGHT - 440))  # Adjusted position
    spikes.add(Spike(450, HEIGHT - 540))  # Adjusted position
    for spike in spikes:
        all_sprites.add(spike)

    # Add spikes on the ground
    spikes.add(Spike(100, HEIGHT - 40))
    spikes.add(Spike(700, HEIGHT - 40))
    for spike in spikes:
        all_sprites.add(spike)

    # Add goal on a platform, ensuring it doesn't overlap with any spikes
    goal = Goal(650, HEIGHT - 540)  # Adjusted position
    goals.add(goal)
    all_sprites.add(goal)

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
            if not player.alive():
                game_over = True
                end_screen(screen, "GAME OVER")
                return
            if not goals:
                game_over = True
                end_screen(screen, "YOU WIN")
                return

        screen.fill(BLACK)
        all_sprites.draw(screen)

        pg.display.flip()
        clock.tick(FPS)

    pg.quit()

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    start_screen(screen)
    main()
