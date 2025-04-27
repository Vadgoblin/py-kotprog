import pygame
from PIL import Image

def load(path, size = None):
    image = pygame.image.load(path)
    if size is None:
        return image

    pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
    pil_scaled_image = pil_image.resize(size, Image.Resampling.BICUBIC)
    scaled_image = pygame.image.fromstring(pil_scaled_image.tobytes(), pil_scaled_image.size, pil_scaled_image.mode)
    return scaled_image