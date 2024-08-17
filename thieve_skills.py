from skill import Skill
import random

class ThieveSkill(Skill):
    def __init__(self, name: str, mana_cost: int, damage: int, cooldown: int, crit_chance: float):
        super().__init__(name, mana_cost, damage, cooldown)
        self.crit_chance = crit_chance

    def chance(self) -> bool:
        """ Calcula si se aplica el crítico para el daño. """
        return random.random() < self.crit_chance

    def use(self, player):
        """ Usa el skill, aplica el cooldown, consume el mana del jugador y verifica si aplica crítico. """
        if self.can_use(player):
            player.mana -= self.mana_cost
            self.current_cooldown = self.cooldown
            if self.chance():
                print(f"¡Crítico! El daño ha aumentado.")
         
        else:
            print("No se puede usar el skill. Mana insuficiente o cooldown activo.")
