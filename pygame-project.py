# main.py
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PLAYER_SPEED = 5
PLAYER_JUMP = 15
GRAVITY = 1

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

# Load images
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (50, 50))
platform_img = pygame.image.load('platform.png')
platform_img = pygame.transform.scale(platform_img, (100, 20))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False

    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x
        
        # Check for collisions with platforms
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platform_hit_list:
            if self.change_x > 0:
                self.rect.right = platform.rect.left
            elif self.change_x < 0:
                self.rect.left = platform.rect.right

        self.rect.y += self.change_y

        # Check for collisions with platforms
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
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

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.change_y = -PLAYER_JUMP
            self.on_ground = False

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = platform_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Function to show text on screen
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Main function
def main():
    clock = pygame.time.Clock()
    
    global platforms
    platforms = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    player = Player()
    all_sprites.add(player)
    
    level = [
        Platform(0, SCREEN_HEIGHT - 40),
        Platform(200, SCREEN_HEIGHT - 150),
        Platform(400, SCREEN_HEIGHT - 300),
        Platform(600, SCREEN_HEIGHT - 450)
    ]
    
    for platform in level:
        platforms.add(platform)
        all_sprites.add(platform)
    
    game_over = False
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_x = -PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:
                    player.change_x = PLAYER_SPEED
                elif event.key == pygame.K_SPACE:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.change_x = 0
        
        if not game_over:
            all_sprites.update()
            if player.rect.top > SCREEN_HEIGHT:
                game_over = True
        
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        if game_over:
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(screen, "Press R to Restart", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 64)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main()
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

# Start screen
def start_screen():
    screen.fill(BLACK)
    draw_text(screen, "Press Any Key to Start", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYUP:
                waiting = False

# Run the game
if __name__ == "__main__":
    start_screen()
    main()