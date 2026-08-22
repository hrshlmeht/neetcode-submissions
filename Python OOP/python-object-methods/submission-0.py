class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        print(f"{self.name} has been fed.")
        self.hunger  = self.hunger - 1 
        print(f"{self.name}'s hunger level: {self.hunger}")
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
Pet.feed(my_pet)
Pet.feed(my_pet)
Pet.feed(my_pet)
