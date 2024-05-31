import random
import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)


class Snowflake(pg.sprite.Sprite):
    def __init__(self):
        """
        Initialize a snowflake with random size, position, and velocity.
        """
        super().__init__()

        # Random size between 5 and 15 pixels
        self.size = random.randint(5, 15)

        # Create a blank surface with an alpha channel
        self.image = pg.Surface((self.size, self.size), pg.SRCALPHA)

        # Draw a circle inside of it
        pg.draw.circle(self.image, WHITE, (self.size // 2, self.size // 2), self.size // 2)

        self.rect = self.image.get_rect()

        # Random starting position at the top of the screen
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-HEIGHT, 0)

        # Random velocity
        self.velocity = random.uniform(1, 3)

    def update(self):
        """Make the snow fall from top to bottom"""
        self.rect.y += self.velocity

        # Reset position if it falls below the screen
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = random.randint(-HEIGHT, 0)
            self.velocity = random.uniform(1, 3)


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Add 100 snowflakes to the all_sprites Group
    for _ in range(100):
        all_sprites.add(Snowflake())

    pg.display.set_caption("Snowfall Landscape")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        # Update the state of all sprites
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        # Draw all the sprites
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()