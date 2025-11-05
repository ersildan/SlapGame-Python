class Unit:
    def __init__(self, name='Юнит', hp=5):
        self.name = name
        self.hp = hp
    
    def take_damage(self, damage):
        self.hp -= damage
        return self.hp
    
    def is_alive(self):
        return self.hp > 0
    
    def get_status(self):
        return f"{self.name}: {self.hp} здоровья"
    
