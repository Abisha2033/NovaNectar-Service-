import random

# Define the player class
class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print("-", item)

# Define functions for different parts of the game

def character_creation():
    print("Welcome to Quest for the Lost Amulet!")
    name = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            player_class = "Warrior"
            break
        elif choice == '2':
            player_class = "Mage"
            break
        elif choice == '3':
            player_class = "Rogue"
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    player = Player(name, player_class)
    return player

def start_game(player):
    print(f"Welcome, {player.name} the {player.player_class}!")
    print("You are in the village of Oakvale. Rumors have spread of the Lost Amulet...")
    # Start your game logic here

# Main game loop
def main():
    player = character_creation()
    start_game(player)

if __name__ == "__main__":
    main()