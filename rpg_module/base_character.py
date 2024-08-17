from typing import List
from items import Item

class BaseCharacter:
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, intelligence: int):
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def get_stats(self):
        return {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'mana': self.mana,
            'strength': self.strength,
            'agility': self.agility,
            'intelligence': self.intelligence,
        }

    def set_stats(self, stats: dict):
        for key, value in stats.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def attack():
        return True


    def reduce_health(self, amount: int):
        self.health -= amount