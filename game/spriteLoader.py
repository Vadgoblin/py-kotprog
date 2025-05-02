import pygame
from PIL import Image

def load(path, size = None, ghost = False):
    image = pygame.image.load(path)

    if size is None:
        pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
    else:
        pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
        pil_image = pil_image.resize(size, Image.Resampling.BICUBIC)

    if ghost:
        r, g, b, a = pil_image.split()
        a = a.point(lambda p: p // 2)
        pil_image.putalpha(a)

    scaled_image = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)
    return scaled_image