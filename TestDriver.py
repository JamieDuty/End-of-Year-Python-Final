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
  
#Where I am at currently it needs to start the game, where you come up on the neighborhood