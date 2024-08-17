from base_character import BaseCharacter
from typing import List


class Mage(BaseCharacter):
    def __init__(self, name: str, level: int, health: int, mana: int, strength: int, agility: int, intelligence: int, magic_type: str, arcane_mastery: int):
        super().__init__(name, level, health, mana, strength, agility, intelligence)
        self.magic_type = magic_type
        self.arcane_mastery = arcane_mastery

    
    def attack(self, opponent: BaseCharacter):
        return self.intelligence * 0.5