import random
from decouple import config

class CasinoGame:
    def __init__(self):
        self.money=int(config('MY_MONEY'))
        self.slots=list(range(1, 31))

    def play_round(self, amount):
        selected_slot=int(input('Слот для ставки (1-30: '))
        if selected_slot not in self.slots:
            print('Неверно')
            return

        win_slot=random.choice(self.slots)
        print(f'Выигрышный слот: {win_slot}')

        if selected_slot == win_slot:
            winnings = amount * 2
            print(f"Поздравляем! Вы выиграли ${winnings}!")
            self.money += winnings
        else:
            print(f"Увы, вы проиграли ${amount}.")
            self.money -= amount

    def game_over(self):
        print(f"Игра завершена. Ваш итоговый капитал: ${self.money}")

if __name__ == "__main__":
    game = CasinoGame()
    while True:
        print(f"Ваш текущий капитал: ${game.money}")
        bet_amount = int(input("Сделайте ставку: "))
        if bet_amount > game.money:
            print("У вас недостаточно средств.")
            break
        game.play_round(bet_amount)
        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            game.game_over()
            break
