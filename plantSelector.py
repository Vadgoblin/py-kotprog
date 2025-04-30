import pygame
from config import Config
import spriteLoader

plant_config = Config().plant
sun_config = Config().sun

def _load_plants():
    plants = []
    for plant_type in plant_config["types"]:
        plant = {}
        _plant_config = plant_config[plant_type]
        plant["type"] = plant_type
        plant["sprite_path"] = _plant_config["sprite"]
        plant["cost"] = _plant_config["cost"]
        plant["recharge_time"] = _plant_config["recharge_time"]
        plants.append(plant)
    return plants


class PlantSelector:
    def __init__(self, x = 240, y = 0):
        self._x = x
        self._y = y
        self._width = 500
        self._height = 119

        self._selected_plant_index = None
        self._sun_count = 50
        self._screen = None
        self._plants = _load_plants()
        self._load_sprites()
        self._load_sun_sprite()
        self._load_font()
        self._sun_position = (self._x + 5, self._y + 5)

    def _load_font(self):
        self._font = pygame.font.Font(Config().game["font"], 18)

    def _load_sun_sprite(self):
        sun_sprite_path = sun_config["sprite"]
        sun_sprite_size = (sun_config["width"], sun_config["height"])
        sun_sprite = spriteLoader.load(sun_sprite_path, sun_sprite_size)
        self._sun_sprite = sun_sprite

    def _load_sprites(self):
        for plant in self._plants:
            sprite_path = plant["sprite_path"]
            sprite = spriteLoader.load(sprite_path, (60,60))
            plant["sprite"] = sprite

    @property
    def selected_plant(self):
        if self._selected_plant_index is None:
            return None
        return self._plants[self._selected_plant_index]["type"]

    @property
    def sun_position(self):
        return self._sun_position

    def draw(self, screen):
        self._screen = screen
        self._draw_container()
        self._draw_sun()
        self._draw_sun_count()
        self._draw_plants()

    def _draw_container(self):
        pygame.draw.rect(self._screen, (109, 50, 18),(self._x, self._y, self._width, self._height), border_radius=15)
        pygame.draw.rect(self._screen, (148, 72, 32),(self._x, self._y, self._width, self._height), 5, 15)

    def _draw_sun(self):
        pygame.draw.line(self._screen,(148, 72, 32),(self._x + 85,0),(self._x + 85, self._height -1), 5)
        self._screen.blit(self._sun_sprite, self._sun_position)
        pygame.draw.rect(self._screen, (236,237,179), (self._x + 10, self._y + 85, 68, 20), border_radius=8)

    def _draw_sun_count(self):
        count = str(self._sun_count)
        text = self._font.render(count,True,"black")
        offset = text.get_width() / 2
        self._screen.blit(text, (self._x + 45 - offset, self._y + 86))

    def _draw_plants(self):
        for index in range(len(self._plants)):
            self._draw_plant(index)

    def _draw_plant(self, index):
        plant = self._plants[index]

        x = self._x + index * 80 + 96
        pygame.draw.rect(self._screen,(173,192,148),(x + 2,self._y + 15,65,71))
        pygame.draw.rect(self._screen,"white",(x + 2,self._y + 86,65,18))

        color = "white" if index==self._selected_plant_index else "black"
        pygame.draw.rect(self._screen, color, (x, self._y + 12, 69, 95),3,7)

        cost = str(plant["cost"])
        cost_text = self._font.render(cost,1,"black")
        cost_offset = cost_text.get_width() / 2
        self._screen.blit(cost_text,(x + 35 - cost_offset, self._y + 86))
        self._screen.blit(plant["sprite"],(x + 4, self._y + 20))

    def on_event(self, event: "pygame.event.Event"):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False

        click_pos = event.dict["pos"]
        click_x, click_y = click_pos
        if click_x < self._x or click_y < self._y:
            return False
        if click_y > self._y + self._height or click_x > self._x + self._width:
            return False

        clicked_plant_index = self._get_clicked_plant_index(click_pos)
        if clicked_plant_index is None:
            return True

        if self._selected_plant_index == clicked_plant_index:
            self._selected_plant_index = None
        else:
            self._selected_plant_index = clicked_plant_index

        return True

    def _get_clicked_plant_index(self, click_pos):
        input_x, input_y = click_pos
        for index in range(len(self._plants)):
            x = self._x + index * 80 + 96
            if x + 2 <= input_x <= x + 67 and self._y + 15 <= input_y <= self._y + 103:
                return index

        return None