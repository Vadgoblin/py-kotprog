import pygame
from PIL import Image

class Zombie:
    def __init__(self):
        self.hp = 10
        self.position = (0,0)

        # sprite = pygame.image.load("assets/zombie.png").convert_alpha()
        # sprite = pygame.transform.scale(sprite, (78, 140))
        # self.sprite = sprite

        image = pygame.image.load("assets/zombie.png")

        pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
        pil_scaled_image = pil_image.resize((78, 140), Image.Resampling.BICUBIC)
        scaled_image = pygame.image.fromstring(pil_scaled_image.tobytes(), pil_scaled_image.size, pil_scaled_image.mode)
        self.sprite = scaled_image

    def draw(self, screen):
        screen.blit(self.sprite, (0, 0))