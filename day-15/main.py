"""
Day 15 - Human Survival Simulator
"""

import random
import time
import click


class Human:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 0
        self.energy = 100

    def status(self):
        print(
            f"""
              -=== Status of {self.name}
                -== Health: {self.health}
                -== Hunger: {self.hunger}
                -== Energy: {self.energy}
              """
        )

    def search_food(self):
        food_found = random.choice([True, False])
        if food_found:
            food = random.choice(["Berries", "Apple", "Chicken", "Rabbit"])
            print(f"{self.name} found some {food}.")
            self.eat(food)
        else:
            print(f"{self.name} found no food.")
            self.energy -= 10
            self.hunger += 10
            self.health -= 5

    def eat(self, food):
        food_energy = {"Berries": 5, "Apple": 7, "Chicken": 15, "Rabbit": 10}
        if food in food_energy:
            self.hunger -= food_energy[food]
            self.energy += food_energy[food]
            if self.hunger < 0:
                self.hunger = 0
            if self.energy > 100:
                self.energy = 100
            print(f"{self.name} eats {food} and gains {food_energy[food]} energy.")

    def drink(self):
        print(f"{self.name} drinks water.")
        self.health += 10
        self.energy += 5
        if self.health > 100:
            self.health = 100
        if self.energy > 100:
            self.energy = 100

    def rest(self, hours):
        print(f"{self.name} rests for {hours} hours.")
        self.energy += hours * 3
        self.hunger -= 5
        if self.energy > 100:
            self.energy = 100

    def check_survive(self):
        if self.health <= 0 or self.hunger >= 100 or self.energy <= 0:
            print(f"{self.name} is died.")
            exit()
        else:
            print(f"{self.name} is survive.")


print("Welcome to Human Survival Simulator!")
player_name = input("Enter your name: ")
player = Human(player_name)


def pause():
    player.check_survive()
    time.sleep(3)
    click.clear()
    main()


def main():

    print(
        f"""
        -=== STATUS
        Name: {player.name}
        Health: {player.health}
        Hunger: {player.hunger}
        Energy: {player.energy}    
        -================-\n
        -=== MENU
        1. Search Food
        2. Drink Water
        3. Rest
        4. Exit
        -================-
        """
    )
    choice = input("Enter your choice: ")
    if choice == "1":
        player.search_food()
        pause()
    elif choice == "2":
        player.drink()
        pause()
    elif choice == "3":
        player.rest(random.randint(1, 5))
        pause()
    elif choice == "4":
        exit()


if __name__ == "__main__":
    main()
