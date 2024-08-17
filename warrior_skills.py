from skill import Skill
import random

class WarriorSkill(Skill):
    def __init__(self, name: str, mana_cost: int, damage: int, cooldown: int, stun_chance: float):
        super().__init__(name, mana_cost, damage, cooldown)
        self.stun_chance = stun_chance

    def stun(self) -> bool:
        """ Calcula si la habilidad aplica un efecto de aturdimiento al enemigo. """
        return random.random() < self.stun_chance

    def use(self, player):
        """ Usa el skill, aplica el cooldown, consume el mana del jugador y verifica si aplica aturdimiento. """
        if self.can_use(player):
            player.mana -= self.mana_cost
            self.current_cooldown = self.cooldown
            if self.stun():
                print(f"¡Aturdido! El enemigo está inhabilitado por un turno.")
                # Puedes implementar la lógica para inhabilitar al enemigo aquí
        else:
            print("No se puede usar el skill. Mana insuficiente o cooldown activo.")
