class Item:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def get_data(self):
        return {
            'name': self.name,
            'value': self.value
        }

    def set_data(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
