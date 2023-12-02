import random, time
from colorama import *

#some try to play this =)
init(autoreset=True)


def game():
    def hp_gamers():
        print(Fore.LIGHTGREEN_EX + f"        {name_player.title()} :  {player_h} хп    vs    ИИ :  {computer_h} хп")
        print(Fore.LIGHTGREEN_EX + '-' * 65)
        pass

    def welcome():

        txt = f'  Добро пожаловать, в игру "Пощечина", {name_player.title()}.\n' \
              f'  Главная цель спустить жизни соперника ниже 0.\n' \
              f'  Кнопки выбора: [ l ] - левая щека, [ R ] - правая щека.\n' \
              f'  Ввод других символов приравнивается к игнорированию атаки или защиты \n' \
              f'  Попадание снимает 3 очка здоровья, блок предотвращает 2 очка урона\n'
        return "{0}{1}".format(Fore.LIGHTBLUE_EX, txt)

    def protection():
        return random.choice(['L', 'R'])

    def attack_phrases():
        text = (
                'готовит мощную',
                'подготавливает скользящую',
                'воссоздаёт батину',
                'заготавливает мягкую',
                'приготовил сильную',
                'разминает руки, чтобы влепить',
                'дует на лодони, чтобы влепить хорошую',
                'использует приём Вялый оплевух, чтобы дать',
                'входит в режим берсерк, чтобы дать',
                'улыбается и делает замах, чтобы дать',
                'хватает ребенка и готовит детскую',
                'заходит со спины и использует грязную',
                'подготавливает симпатишную',
                'целует ладонь, чтобы влепить'
                )
        return random.choice(text)

    def defence_phrases(s='text'):
        text = ('Зрители делают ставки, что выберешь - правую или левую?',
                'После боя чем займешься? Может снова сыграем?',
                'Случайный зритель пожал вам руку на удачу!',
                'Какая щека у тебя крепче  всего - правая или левая?',
                'Ты хочешь защитить с правой стороны или с левой?',
                'Он думает куда тебя ударить, что будешь защищать?',
                'Я не знаю, какую тебе защитить! Левую или правую щеку? ',
                'Какая из твоих щек мягче - правая или левая?',
                'Скорее выбирайте какую щеку  будешь защищать!',
                'К какой щеке вам приложить сковородку для защиты?',
                'Держи подушку и приложи к защитной щеке:',
                'Закрой глаза, выбери защиту и получай удовльствие',
                'Ещё совсем немного потерпеть, что будешь защищать?',
                'Будет бить как девчонка, куда ставить блок?'
                )
        text_ = (
                'в последний миг укрывается правильно',
                'ставит блок! Уверенно смотрит сопернику в глаза',
                'отстаивает свои позиции блоком',
                'укрепляет оборону подушкой',
                'ставит защиту вялой ладошкой',
                'смог противостоять нападению, поставив блок',
                'сохраняет своё щи, используя интуицию',
                'угадывает сторону атаки',
                'применяет удачную защиту',
                'ставит блок котиком',
                'угадывает сторону удара и ставит блок',
                'предотвращает угрозу сковородкой'
                )
        return random.choice(text) if s == 'text' else random.choice(text_)

    total = 1
    player_h, computer_h = 5, 5

    d_fight = {
                1: 'первую',
                2: 'вторую',
                3: 'третью',
                4: 'ЧЕТВЕРТУЮ',
                5: 'НИЧЕСИ! ПЯТУЮ!',
                6: 'ШЕСТУЮ!!!'
               }

    name_player = 'Юнит'

    print(welcome())

    time.sleep(3.5)
    print('-' * 24, f'Начался {total} раунд', '-' * 24)

    while True:
        print(Fore.LIGHTBLUE_EX + f'  {name_player} {attack_phrases()} {d_fight[total]} пощёчину.')

        at = input(f'  Выбрать сторону для атаки ==>  [ L ] или [ R ]   ').upper()

        if at == protection():
            computer_h -= 1
            print('-' * 65)
            print(Fore.LIGHTYELLOW_EX + '\033[3m'f"   Компьютер {defence_phrases('text_')}! Теряет всего 1 очко")
            print('-' * 65)
            hp_gamers()
        else:
            computer_h -= 3
            print('-' * 65)
            print(Fore.LIGHTYELLOW_EX + "\033[3m"f'   {name_player}, точно в цель! ИИ теряет 3 очка')
            print('-' * 65)
            hp_gamers()

        print(Fore.LIGHTBLUE_EX + f'  ИИ {attack_phrases()} пощёчину.')
        print(f'  {Fore.LIGHTBLUE_EX + defence_phrases()}')
        block = input('  Выбрать сторону для защиты ==>  [ L ] или [ R ]   ').upper()

        if protection() == block:
            player_h -= 1
            print('-' * 65)
            print(Fore.LIGHTYELLOW_EX + '\033[3m'f"   {name_player} {defence_phrases('text_')} и теряет всего 1 очко!")
            print('-' * 65)
        else:
            player_h -= 3
            print('-' * 65)
            print(Fore.LIGHTYELLOW_EX + "\033[3m"f'   ИИ заряжает точно в цель! {name_player} теряет 3 очка')
            print('-' * 65)
        time.sleep(1)

        print('-' * 25, f'Итог {total} раунда', '-' * 25)
        print(Fore.LIGHTGREEN_EX + f"        {name_player} :  {player_h} хп    vs    ИИ :  {computer_h} хп")
        print('-' * 65)
        time.sleep(1)

        if player_h == computer_h and player_h < 0 and computer_h < 0:
            print(Fore.LIGHTGREEN_EX + '   Бой окончен!')
            print(Fore.LIGHTGREEN_EX + '   Ничья, господа. Победила дружба. ')
            break
        if player_h < 0:
            print(Fore.LIGHTWHITE_EX + '   Бой окончен!')
            print(Fore.LIGHTWHITE_EX + f'   ПОБЕДИЛ: ИИ')
            break
        if computer_h < 0:
            print(Fore.LIGHTWHITE_EX + '   Бой окончен! Поздравляем!')
            print(Fore.LIGHTWHITE_EX + f'   ПОБЕДИЛ: {name_player}')
            print(Fore.LIGHTCYAN_EX + f'   Бодрые аплодисменты от автора игры!')
            break

        time.sleep(1)
        print('-' * 24, f'Начался раунд {total + 1}', '-' * 24)
        total += 1

    return '-' * 65


while True:
    print('   Начать игру [ + ]')
    print('   Чтобы выйти из игры [ - ]')
    sos = input('  ')
    if sos == '-':
        exit()
    else:
        print(game())
