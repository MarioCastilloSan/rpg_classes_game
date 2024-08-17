class Skill:
    def __init__(self, name: str, mana_cost: int, damage: int, cooldown: int):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.cooldown = cooldown
        self.current_cooldown = 0

    def can_use(self, player) -> bool:
        """ Verifica si el jugador puede usar el skill considerando el mana y el cooldown. """
        return player.mana >= self.mana_cost and self.current_cooldown == 0

    def use(self, player):
        """ Usa el skill, aplica el cooldown y consume el mana del jugador. """
        if self.can_use(player):
            player.mana -= self.mana_cost
            self.current_cooldown = self.cooldown
            return True  
        return False  
