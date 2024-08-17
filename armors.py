from items import Item

class Armor(Item):
    def __init__(self, name: str, value: int, defense_power: int):
        super().__init__(name, value)
        self.defense_power = defense_power

    def get_data(self):
        data = super().get_data()  # Obtiene datos de la clase base
        data.update({
            'defense_power': self.defense_power
        })
        return data

    def set_data(self, data: dict):
        super().set_data(data)  # Actualiza datos de la clase base
        if 'defense_power' in data:
            self.defense_power = data['defense_power']
