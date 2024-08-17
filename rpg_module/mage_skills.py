from skill import Skill

class MageSkill(Skill):
    def __init__(self, name: str, mana_cost: int, damage: int, cooldown: int, elemental_type: str):
        super().__init__(name, mana_cost, damage, cooldown)
        self.elemental_type = elemental_type

    def increase_damage_by_intelligence(self, mage):
        """ Aumenta el daño en base a la inteligencia del mago. """
        self.damage += mage.intelligence * 0.1  # Ajustar el factor de incremento según necesidades

    def can_use(self, player) -> bool:
        """ Verifica si el mago puede usar el skill considerando el mana, cooldown y tipo de magia. """
        return super().can_use(player) and self.elemental_type == player.magic_type
