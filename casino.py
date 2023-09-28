from casino_logic import CasinoGame

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
