from pygame import mixer
from config import Config
from pygame.mixer import Sound

_soundPlayer = None

def play_bgm():
    _play_music("bgm")

def play_win_music():
    _play_music("win_music")

def play_chomp():
    _play_sfx("chomp")

def play_plant():
    _play_sfx("plant")

def play_sun_pickup():
    _play_sfx("sun_pickup")

def play_splat():
    _play_sfx("splat")

def play_cherry_bomb():
    _play_sfx("cherry_bomb")

def _play_music(music_name):
    global _soundPlayer
    if _soundPlayer is None:
        _soundPlayer = _SoundPlayer()
    _soundPlayer.play_music(music_name)

def _play_sfx(sfx_name):
    global _soundPlayer
    if _soundPlayer is None:
        _soundPlayer = _SoundPlayer()
    _soundPlayer.play_sfx(sfx_name)


class _SoundPlayer:
    def __init__(self):
        audio = {}
        for name, path in Config().audio.items():
            audio[name] = Sound(path)
        self._audio = audio

        mixer.set_num_channels(1000)

    def play_music(self,music_name):
        mixer.Channel(0).play(self._audio[music_name])

    def play_sfx(self,sfx_name):
        for i in range(1, 100):
            channel = mixer.Channel(i)
            if channel.get_busy():
                continue
            channel.play(self._audio[sfx_name])
            break