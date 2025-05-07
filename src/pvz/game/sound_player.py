from pygame import mixer

from src.pvz.assets.asset_loader import load_sound
from src.pvz.config import Config


_sound_player = None


def play_bgm():
    _get_sound_player().play_music("bgm")


def play_win_music():
    _get_sound_player().play_music("win_music")


def play_chomp():
    _get_sound_player().play_sfx("chomp")


def play_plant():
    _get_sound_player().play_sfx("plant")


def play_sun_pickup():
    _get_sound_player().play_sfx("sun_pickup")


def play_splat():
    _get_sound_player().play_sfx("splat")


def play_cherry_bomb():
    _get_sound_player().play_sfx("cherry_bomb")


def stop_music():
    _get_sound_player().stop_music()


def _get_sound_player():
    global _sound_player
    if _sound_player is None:
        _sound_player = _SoundPlayer()
    return _sound_player


class _SoundPlayer:
    def __init__(self):
        self._audio = {}
        for name, filename in Config().audio.items():
            if name == "num_of_channels":
                continue
            self._audio[name] = load_sound(filename)
        self._num_of_channels = Config().audio["num_of_channels"]
        mixer.set_num_channels(self._num_of_channels)

    def play_music(self, music_name):
        if music_name in self._audio:
            channel = mixer.Channel(0)
            channel.play(self._audio[music_name], loops=-1)
        else:
            print(f"Error: Music '{music_name}' not found!")

    def play_sfx(self, sfx_name):
        if sfx_name in self._audio:
            for i in range(1, self._num_of_channels):
                channel = mixer.Channel(i)
                if not channel.get_busy():
                    channel.play(self._audio[sfx_name])
                    break
        else:
            print(f"Error: Sound effect '{sfx_name}' not found!")

    def stop_music(self):
        mixer.Channel(0).stop()