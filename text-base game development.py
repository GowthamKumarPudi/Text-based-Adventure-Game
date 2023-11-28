import time

class Story:
    def __init__(self):
        self.storyline = [
            "You find yourself in a bustling city square. People are rushing by, and there's a mysterious alley to your left.",
            "As you enter the alley, you encounter a shady figure offering you a peculiar-looking map.",
            "The map reveals two options: 'Lost Caves' or 'Enchanted Garden.' Choose wisely.",
            "You follow the map and arrive at the entrance of the chosen location."
        ]

class UserInterface:
    @staticmethod
    def get_choice():
        return input("Enter your choice (1/2): ")

    @staticmethod
    def display(text):
        print(text)
        time.sleep(1)

class Game:
    def __init__(self):
        self.story = Story()
        self.ui = UserInterface()
        self.inventory = []

    def start_game(self):
        current_index = 0

        while current_index < len(self.story.storyline):
            self.ui.display(self.story.storyline[current_index])

            if current_index == 2:
                choice = self.ui.get_choice()
                if choice == "1":
                    self.ui.display("You venture into the Lost Caves.")
                    self.lost_caves()
                elif choice == "2":
                    self.ui.display("You enter the Enchanted Garden.")
                    self.enchanted_garden()
                else:
                    self.ui.display("Invalid choice. Please enter 1 or 2.")
            else:
                current_index += 1

    def lost_caves(self):
        self.ui.display("Inside the dark caves, you discover a hidden treasure chest.")
        time.sleep(1)
        self.inventory.append("Treasure")
        self.ui.display(f"Congratulations! You found a treasure. Your inventory: {self.inventory}")
        self.end_game()

    def enchanted_garden(self):
        self.ui.display("In the magical garden, you encounter a talking tree.")
        time.sleep(1)
        self.ui.display("The tree offers you a choice: 'Wisdom' or 'Strength.'")
        choice = self.ui.get_choice()

        if choice == "1":
            self.ui.display("You gain wisdom and knowledge.")
            self.inventory.append("Wisdom")
        elif choice == "2":
            self.ui.display("You feel a surge of strength coursing through you.")
            self.inventory.append("Strength")
        else:
            self.ui.display("Invalid choice. You leave the garden empty-handed.")

        self.ui.display(f"Your inventory: {self.inventory}")
        self.end_game()

    def end_game(self):
        self.ui.display("The adventure concludes. Thanks for playing!")

if __name__ == "__main__":
    game = Game()
    game.start_game()
