import random # завантажуємо розширення


random.seed()


class BlackJack:  # створюємо клас Блек Джек
    def __init__(self): 
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4
        self.score = 0
        self.bot_score = 0 # визначаємо ексемпляри класу

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очков.')
        else:
            print(f'Крупье попалась карта {current}. У крупье {score} очков') # функція виводу карти і підрахунку очків

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Ace':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score                         # рандомна наступна карта і вивід рахунку

    def choice(self):                                  
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Будете брать карту? y/n\n')  # вибір карти у гравця 
            if choice == 'y':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Извините, но вы проиграли')  # моделювання ігрових ситуацій
                    break
                elif score == 21 and bot_score == 21:
                    print('ничья')                      # ничія
                elif score == 21 or bot_score > 21:
                    print('Поздравляю, вы победили!')
                    break                               # перемога
            elif choice == 'n':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очков, у крупье {bot_score} очков') # програш
                else:
                    print(f'Вы победили, у вас {score} очков, у крупье {bot_score} очков')  # виграш

                break

    def start(self):               # оформлення ігрового середовища і старт гри
        random.shuffle(self.deck)
        print('Игра в BlackJack началась')
        print('В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков')
        print('----------------------------------')
        self.choice()

        print('До новых встреч!')


game = BlackJack()
game.start()