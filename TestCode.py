import random
#need to add a way to count up wins so I can add secret keys and things
class Game:
    def __init__(self, player):
        self.player = player
        self.house = House()

    def start(self):
        print("You have suddenly found yourself in an old strange neighborhood.")
        print("It all looks so uniform and strange, except one house just feels... different. You decide to go up to it to take a closer look.")
        choice = input("Do you want to enter the house? (yes/no): ").lower()
        if choice == 'yes':
            self.house.enter(self.player)
        else:
            print("You walk away and miss the opportunity... maybe next time.")

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def connect(self, direction, room):
        self.exits[direction] = room
    
    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def play(self, player):
        pass

class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 100  #the player starts with 100 dabloons
        self.inventory = []

    def add_coins(self, amount):
        self.coins += amount
        print(f'You now have {self.coins} dabloons.')

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            print(f'You now have {self.coins} dabloons.')
            return True
        else:
            print("You are out of dabloons!")
            return False

class SlotMachine(Room):
    def __init__(self):
        super().__init__('Slot Machine Room')
    
    def play(self, player):
        print('Welcome to the Slot Machine Room') #Add more detail
        if not player.spend_coins(10):
            return
        symbols = ['Cherry', 'Lemon', 'Bell']
        result = [random.choice(symbols) for i in range(3)]
        print(' | '.join(result))
        if len(set(result)) == 1:
            print("Jackpot! You win 50 Dabloons!")
            player.add_coins(50)
        else:
            print("Better luck next time.")

class DiceGame:
    def __init__(self):
        self.name = "Dice Game Room"

    def play(self,player):
        print("Welcome to the Dice Game Room.")
        if not player.spend_coins(5):
          return
        
        player_roll = random.randint(1, 6)
        house_roll = random.randint(1, 6)
        print(f'You rolled: {player_roll}')
        print(f'House rolled: {house_roll}')
        
        if player_roll > house_roll:
          print('You win 10 coins!')
          player.add_coins(10)
          
        else:
          print("You lose!")

class House:
    def __init__(self):
        self.rooms = {
          "north": SlotMachine(),
          "east": DiceGame()
    }
    def enter(self,player):
        print("You enter the house. It's dark and mysterious.")
        print("There are paths leading in different directions...")
        
        while True:
          print('\nAvailable directions:')
          
          for direction in self.rooms:
            print(f'- {direction.title()}')
          print('- Leave (to exit the mansion and end your night)')
          choice = input("Which direction do you want to go? ").lower()
          
          if choice in self.rooms:
            room = self.rooms[choice]
            print(f'You walk {choice} and enter the {room.name}!')
            room.play(player)
            
          elif choice == 'leave':
            print("You leave the house and step back into reality. The night is over.")
            break
        
          else:
            print('You can\'t go that way.')

