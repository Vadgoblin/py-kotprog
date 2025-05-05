from importlib.resources import files
from PIL import Image
import pygame
import tempfile
import shutil

import tempfile
import shutil
import pygame
from pathlib import Path
from pygame.mixer import Sound
from typing import cast, IO

def load_sprite(name, size = None, ghost = False):
    path = _resolve_asset_file(name)

    with path.open('rb') as f:
        image = pygame.image.load(f)

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


def load_font(name, size):
    font_resource = _resolve_asset_file(name)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".ttf") as tmp:
        tmp_path = Path(tmp.name)
        with font_resource.open('rb') as src:
            shutil.copyfileobj(src, tmp)

    return pygame.font.Font(str(tmp_path), size)

def load_sound(name):
    resource = _resolve_asset_file(name)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        with resource.open('rb') as src:
            shutil.copyfileobj(src, tmp_file)
        tmp_path = tmp_file.name

    return Sound(tmp_path)


def _resolve_asset_file(asset_name: str):
    return files('pvz').joinpath("assets",asset_name)