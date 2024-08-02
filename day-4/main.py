"""
Day 4 - Todo List
"""

import json
import click
import time

task_list = []


def save():
    with open("data.json", "w") as file:
        json.dump(task_list, file)


def load():
    global task_list
    try:
        with open("data.json", "r") as file:
            task_list = json.load(file)
        print("Task list has been loaded from 'data.json'")
    except FileNotFoundError:
        print("File 'data.json' not found'")


def new(task):
    task_list.append({"task": task, "completed": False})


def show():
    if not task_list:
        print("No task in list.")
    else:
        for index, task in enumerate(task_list, start=1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{index}. {task['task']} - {status}")


def show_filter(completed=None):
    filtered_task = task_list
    if completed is not None:
        filtered_task = [task for task in task_list if task["completed"] == completed]
    if not filtered_task:
        print("No task that match the filter.")
    else:
        for index, task in enumerate(filtered_task, start=1):
            status = "Completed" if task["completed"] else "Not completed"
            print(f"{index}. {task['task']} - {status}")


def complete(number):
    if 0 < number <= len(task_list):
        task_list[number - 1]["completed"] = True
        print(f"Task '{task_list[number - 1]['task']}' Has marked as completed")
    else:
        print("Task number not found.")


def delete(number):
    if 0 < number <= len(task_list):
        task = task_list.pop(number - 1)
        print(f"Task '{task['task']}' Has deleted.")
    else:
        print("Task number not found.")


def update(number, new_task):
    if 0 < number <= len(task_list):
        task_list[number - 1]["task"] = new_task
        print(f"Task number {number} has updated to '{new_task}'")
    else:
        print("Task number not found.")


def home(sleeptime):
    time.sleep(sleeptime)
    click.clear()
    main()


def main():
    print(
        f"""
          1. New Task
          2. Task List
          3. Task List (filtered)
          4. Mark as Completed
          5. Delete Task
          6. Exit
          
          98. Save Task
          99. Load Task
          
          Save your task every time!
          """
    )
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        new(task)
        print(f"Task '{task}' added.")
        home(2)
    elif choice == "2":
        show()
        print("Back to home in 5 seconds...")
        home(5)
    elif choice == "3":
        filter = input("Do you want to see completed task? (yes/no): ")
        if filter == "yes":
            show_filter(completed=True)
            print("Back to home in 5 seconds...")
            home(5)
        elif filter == "no":
            show_filter(completed=False)
            print("Back to home in 5 seconds...")
            home(5)
    elif choice == "4":
        number = int(input("Enter task ID to mark as completed: "))
        complete(number)
        home(2)
    elif choice == "5":
        number = int(input("Enter task ID to delete: "))
        delete(number)
        home(2)
    elif choice == "6":
        exit()
    elif choice == "98":
        print("Saving todo list...")
        save()
        print("Task list has been saved to 'data.json'")
        home(2)
    elif choice == "99":
        print("Loading task list from 'data.json'...")
        load()
        home(2)


if __name__ == "__main__":
    main()
