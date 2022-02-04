from jumper import game, play

game = input('would you like to play the game?(y/n)')
if game == "y":

    jumper = play()
    jumper.start_game()
else:
    print("That's too bad")
