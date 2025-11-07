import random


class Unit:

    def __init__(self, name='Юнит', hp=10):
        self.name = name
        self.hp = hp
        self.abilities = {
            'heal_used': False, 
            'bubble_used': False
        }

    
    def take_damage(self, damage):
        self.hp -= damage
        return self.hp


    def is_alive(self):
        return self.hp > 0
    

    def get_status(self):
        return f"{self.name}: {self.hp} здоровья"


class GameLogic:

    @staticmethod
    def roll_dice(sides=20):
        """Бросок кубика 1-20"""

        return random.randint(1, sides)
    

    @staticmethod
    def human_choose_attack():
        """Выбор действия с валидацией"""

        valid_keys = ['A', 'D', 'E', 'Q', ' ']
        
        while True:
            print("A - атака слева | D - атака справа")
            print("E - аптечка | Q - бабл паладина")
            choice = input('Выберите действие: ').upper()
            
            if not choice:
                return None
            
            choice = choice[0]
            
            if choice in valid_keys:
                return choice
                   
            else:
                print(f"Используй только => {', '.join(valid_keys)}!")

    @staticmethod
    def human_choose_defense():
        """Выбор защиты с валидацией"""
        
        valid_keys = ['A', 'D']
        
        while True:
            raw_input = input('Защита ==> [A] или [D] ').upper()

            if not raw_input:
                return None
            
            choice = raw_input[0]
            
            if choice in valid_keys:
                return choice
            else:
                print(f"Используй только => {', '.join(valid_keys)}!")
        

    @staticmethod
    def computer_choose():
        return random.choice(['A', 'D'])
    
    
    @staticmethod
    def check_hit(attack_side, defense_side):
        return attack_side != defense_side
    
    
computer = Unit("Хекс")
player = Unit()

