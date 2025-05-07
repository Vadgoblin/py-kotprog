"""
Asset loader.

This module loads the assets for the game.
"""

import shutil
import tempfile
from functools import lru_cache
from importlib.resources import files
from pathlib import Path

import pygame
from PIL import Image
from pygame.mixer import Sound


@lru_cache(maxsize=None)
def load_sprite(name:str, size:tuple[int, int]|None=None, ghost=False):
    """
    Loads the specified sprite.

    :param name: The name of the sprite including extension.
    :param size: The size of the loaded sprite, None means no resize.
    :param ghost: Set true to have 50% opacity.
    :return: The loaded sprite.
    """
    path = _resolve_asset_file(name)

    with path.open('rb') as f:
        image = pygame.image.load(f)

    if size is None:
        pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
    else:
        pil_image = Image.frombytes("RGBA", image.get_size(), pygame.image.tostring(image, "RGBA"))
        pil_image = pil_image.resize(size, Image.Resampling.BICUBIC)

    if ghost:
        _, _, _, a = pil_image.split()
        a = a.point(lambda p: p // 2)
        pil_image.putalpha(a)

    scaled_image = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)
    return scaled_image


@lru_cache(maxsize=None)
def load_font(name, size):
    """
    Loads the specified font.
    :param name: the name of the font file
    :param size: the wanted font size
    :return: the loaded font object
    """
    font_resource = _resolve_asset_file(name)

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = Path(tmp.name)
        with font_resource.open('rb') as src:
            shutil.copyfileobj(src, tmp)

    return pygame.font.Font(str(tmp_path), size)


@lru_cache(maxsize=None)
def load_sound(name):
    """
    Loads the specified sound.
    :param name: the name of the sound including extension
    :return: the loaded sound object
    """
    resource = _resolve_asset_file(name)
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        with resource.open('rb') as src:
            shutil.copyfileobj(src, tmp_file)
        tmp_path = tmp_file.name

    return Sound(tmp_path)


def _resolve_asset_file(asset_name: str):
    return files('pvz').joinpath("assets", asset_name)
