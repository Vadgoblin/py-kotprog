class Level:
    def __init__(self, enemies):
        self._enemies = enemies
        pass

    def __getitem__(self, item):
        return self._enemies[item]

    def __len__(self):
        return len(self._enemies)