from base_character import BaseCharacter
from typing import List


class Warrior(BaseCharacter):
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, intelligence: int, rage: int):
        super().__init__(name, level, health, mana, strength, agility, intelligence)
        self.rage = rage
        self.armor = 0


    def attack(self, opponent: BaseCharacter):
        return self.strength * 0.5 