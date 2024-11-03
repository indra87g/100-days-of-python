"""
Day 24 - Shop with Membership
"""

import random
from click import termui

shop_items = {
    "Book": 300,
    "Pencil": 100,
    "Pen": 125,
    "Ruler": 50,
    "Printer Tint": 75,
    "Eraser": 45,
}
reward = {
    "Amazon Voucher $5": 15,
    "Spotify Premium 1 Month": 30,
    "Youtube Premium 1 Month": 35,
    "Google Play Voucher $5": 10,
}


class Shop:
    def __init__(self, name, balance=1000, points=10, inventory=None):
        self.name = name
        self.balance = balance
        self.points = points
        self.inventory = inventory if inventory is not None else []

    def buy(self, item):
        if item in shop_items:
            self.inventory.append(item)
            self.balance -= shop_items[item]
            self.points += random.randint(1, 5)
            print(f"You buy {item} with {shop_items[item]} balance.")
            print(
                f"You receive some membership point. You can withdraw it for rewards!"
            )

    def sell(self, item):
        if item in shop_items:
            self.inventory.remove(item)
            self.balance += shop_items[item] - random.randint(1, 7)
            print(f"You sell {item} for {shop_items[item]} balance")

    def claim_reward(self, item):
        if item in reward:
            self.inventory.append(item)
            self.points -= reward[item]
            print(f"You claim {item} with {reward[item]} membership")


def main(shop_member):
    print(
        f"""
        ==-----------------==
        Welcome, {shop_member.name}!
          
        Balance: {shop_member.balance}
        Membership Points: {shop_member.points}
        Inventory: {shop_member.inventory}
        ==-----------------==
        MENU
        1. Buy
        2. Sell
        3. Claim Rewards
        4. Exit
        """
    )
    choice = str(input("Enter your choice: "))
    if choice == "1":
        termui.clear()
        print(f"Available items in our shop:\n{shop_items}\n")
        item = str(input("Which item do you want to buy? "))
        shop_member.buy(item)
        next_action(shop_member)
    elif choice == "2":
        termui.clear()
        print(f"Available items in your inventory:\n{shop_member.inventory}\n")
        item = str(input("Which item do you want to sell? "))
        shop_member.sell(item)
        next_action(shop_member)
    elif choice == "3":
        termui.clear()
        print(
            f"Available rewards for our member:\n{reward}\nYour membership points: {shop_member.points}\n"
        )
        item = str(input("Which reward do you want to claim? "))
        shop_member.claim_reward(item)
        next_action(shop_member)
    elif choice == "4":
        print(f"Goodbye, {shop_member.name}")
        exit()
    if not choice:
        raise ValueError("Invalid choice!")


def next_action(shop_member):
    termui.pause()
    termui.clear()
    main(shop_member)


if __name__ == "__main__":
    try:
        name = str(input("Enter your name: "))
        if not name:
            raise ValueError("Name cannot be empty!")
        else:
            shop_member = Shop(name)
            main(shop_member)
    except KeyboardInterrupt:
        print("\nProgram closed.")
