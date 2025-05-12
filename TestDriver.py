from TestCode import Player
from TestCode import Game

def main():
      name = input('What\'s your name? ')
      player = Player(name)
      print()
      print(f'Welcome, {player.name}, the night is young, lets get started.')
      player = Player(name)
      game = Game(player)
      game.start()
if __name__ == '__main__':
  main()

#Currently the game starts and runs, and there are 2 options and the leave option. Both Games work
  
#Need to improve:
  #more options for the games and rooms
  #Save name and dabloons to file??
  #add secret rooms by counting up wins and if you get so many wins you get keys to secret rooms.