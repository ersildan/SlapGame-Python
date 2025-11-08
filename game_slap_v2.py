import random
import os 


class Unit:

    def __init__(self, name='Юнит', hp=10):
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
    def roll_dice(sides=20):
        """Бросок кубика 1-20"""

        return random.randint(1, sides)

    @staticmethod
    def human_choose_attack():
        """Выбор действия с валидацией"""

        valid_keys = ['A', 'D']
        
        while True:
            print("A - атака слева | D - атака справа")
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
        
        valid_keys = ['A', 'D', 'Q']
        q_flag = False
        
        while True:
            raw_input = input('Защита ==> [A] или [D] или [Q]: \n').upper()

            if not raw_input:
                return None
            
            choice = raw_input[0]
            
            if choice == 'Q':
                if q_flag:
                    print("ЭЙ! Q уже использован в этом ходу! \nВыбери A или D для защиты!")
                    continue
                    
                print("Бросок 🎲 на бабл Паладина!")
        
                while True:
                    user_input = input("Нажмите [space] для броска.\n" \
                                       "Сложность [15]: ")
                    
                    if user_input == " ":
                        break
                    else:
                        print("Нажмите именно SPACE!")
                
                n = GameLogic.roll_dice()
                
                print(f"На кубике: {n}")

                if n > 15:
                    print('Бабл активирован! Урона нет!')
                    return True
                else:
                    q_flag = True
                    print('Бабл не активирован! Выбери защиту вручную.\n')
                    continue
                    
            elif choice in ['A', 'D']:
                return choice
            else:
                print(f"Используй только => {', '.join(valid_keys)}!")

    @staticmethod
    def computer_choose():
        return random.choice(['A', 'D'])
    
    @staticmethod
    def check_hit(attack_side, defense_side):
        return attack_side != defense_side


class GameController:
    def __init__(self):
        self.computer = Unit("Хекс")
        self.player = Unit()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear') # чистка консоли
    
    def game_loop(self):
        """Фаза 1: Определение инициативы"""

        print("Бросок кубика на инициативу!")
        
        while True:
            user_input = input("Нажмите [ space ] для броска кубика + [ Enter ]\n")
            
            if user_input[0] == " ":
                break
            else:
                print("Чтобы бросить кубик нажмите на [ space ]")
        
        player_roll = GameLogic.roll_dice()
        computer_roll = GameLogic.roll_dice()
            
        print(f"Твой бросок: {player_roll} vs ИИ: {computer_roll}")
        
        if player_roll >= computer_roll:
            print("Юнит атакует первым!")
            self.player_attacks_first()
        else:
            print("Хекс атакует первым!")
            self.computer_attacks_first()
    
    def player_attacks_first(self):
        """Ветка событий: Юнит атакует первым"""

        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== РАУНД {round_number} ===")

            self.player_attack_phase()

            if self.computer.is_alive():
                self.computer_attack_phase() 

            round_number += 1
    
    def computer_attacks_first(self):
        """Ветка событий: Хекс атакует первым"""

        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== РАУНД {round_number} ===")

            self.computer_attack_phase()

            if self.player.is_alive():
                self.player_attack_phase()
            round_number += 1

    def player_attack_phase(self):
        """Атака Юнита - Хекс защищается"""

        self.clear_console()
        action1 = GameLogic.human_choose_attack()
        action2 = GameLogic.computer_choose()

        n = GameLogic.roll_dice()

        print("Хекс бросает 🎲 на бабл паладина")
        print(f"Проверка на активацию {{Сложность [15]}}, выпало: {n}")

        if n > 15:
            print("Хекс активирует бабл паладина и не получает урон!")
            return True
        else:
            if GameLogic.check_hit(action1, action2):
                print('Юнит наносит 3 очка урона, точно в цель!')
                self.computer.take_damage(3)
            else:
                print('Хекс защищает нужную сторону и получает всего 1 урон!')
                self.computer.take_damage(1)
            
            print(self.computer.get_status())
        
        if self.computer.is_alive():
            return True
        else:
            return 'Победил Юнит!'
    
    def computer_attack_phase(self):
        """Атака Хекса - Юнит защищается"""
        
        self.clear_console()
        computer_attack = GameLogic.computer_choose()
        player_defense = GameLogic.human_choose_defense()
        
        # Если игрок использовал Q и вернул True - нет урона
        if player_defense is True:
            print("Бабл сработал! Урона нет!")
            return
        
        # Сравниваем атаку компьютера и защиту игрока
        if GameLogic.check_hit(computer_attack, player_defense):
            print('Хекс наносит 3 урона!')
            self.player.take_damage(3)
        else:
            print('Юнит блокирует удар! 1 урона!')
            self.player.take_damage(1)
        
        print(self.player.get_status())

if __name__ == "__main__":
    game = GameController()
    game.game_loop()