from player import TestCode

def main():
  name = input('What\'\s your name? ')
  player = Player(name)
  print(f'Welcome, {player.name}, the night is young, lets get started.')
if __name__ == '__main__':
  main()