import random


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


class GameLogic:

    @staticmethod
    def human_choose_attack():
        return input('Атака ==> [A] или [D] ').upper()
    
    @staticmethod
    def human_choose_defense():
        return input('Защита ==> [A] или [D] ').upper()
    
    @staticmethod
    def computer_choose():
        return random.choice(['A', 'D'])
    
    @staticmethod
    def check_hit(attack_side, defense_side):
        return attack_side != defense_side
    
    
computer = Unit("S5")
player = Unit()
