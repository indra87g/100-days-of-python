"""
Day 3 - SQLite CRUD
"""

import sqlite3 as sq
import time
import click
from database import create_connection, create_table


def create(name, description):
    conn = create_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO items (name, description) VALUES (?, ?)", (name, description)
    )
    conn.commit()
    conn.close()


def read():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    rows = c.fetchall()
    conn.close()
    return rows


def update(item_id, name, description):
    conn = create_connection()
    c = conn.cursor()
    c.execute(
        "UPDATE items SET name = ?, description = ? WHERE id = ?",
        (name, description, item_id),
    )
    conn.commit()
    conn.close()


def delete(item_id):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id = ?", (item_id))
    conn.commit()
    conn.close()


def main():
    create_table()
    print(
        f"""
            1. Create Item
            2. Read Item
            3. Update Item
            4. Delete Item
            5. Exit
            """
    )
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        create(name, description)
        print("Item created!")
        time.sleep(2)
        click.clear()
        main()
    elif choice == "2":
        items = read()
        for item in items:
            print(f"ID: {item[0]} Name: {item[1]} Description: {item[2]}")
    elif choice == "3":
        item_id = int(input("Enter item ID to update: "))
        name = input("Enter new item name: ")
        description = input("Enter new item description: ")
        update(item_id, name, description)
        print("Item updated!")
        time.sleep(2)
        click.clear()
        main()
    elif choice == "4":
        item_id = int(input("Enter item ID to delete: "))
        delete(item_id)
        print("Item deleted!")
        time.sleep(2)
        click.clear()
        main()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
