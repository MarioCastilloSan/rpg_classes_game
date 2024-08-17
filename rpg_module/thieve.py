from base_character import BaseCharacter
from typing import List


class Thieve(BaseCharacter):
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, intelligence: int, stealth: int):
        super().__init__(name, level, health, mana, strength, agility, intelligence)
        self.stealth = stealth


    def attack(self, opponent: BaseCharacter):
        return self.agility * 0.5 