#!/usr/bin/env python3

# import the datetime module for working with dates
import datetime

# define a class for a to-do item
class TodoItem:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f'{self.title} ({self.due_date}) - {self.description}'

# define a function for adding a new to-do item
def add_todo():
    print('Add a new to-do item')
    title = input('Title: ')
    description = input('Description: ')
    due_date_str = input('Due date (YYYY-MM-DD): ')
    due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
    todo_item = TodoItem(title, description, due_date)
    with open('todo_list.txt', 'a') as f:
        f.write(f'{todo_item.title}\t{todo_item.description}\t{todo_item.due_date}\n')
    print('To-do item added successfully!')

# define a function for listing all to-do items
def list_todos():
    print('List of to-do items')
    with open('todo_list.txt', 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            title = parts[0]
            description = parts[1]
            due_date = datetime.datetime.strptime(parts[2], '%Y-%m-%d').date()
            todo_item = TodoItem(title, description, due_date)
            print(todo_item)

# main program loop
while True:
    print('To-do list app')
    print('1. Add a new to-do item')
    print('2. List all to-do items')
    print('3. Quit')
    choice = input('Enter your choice (1-3): ')
    if choice == '1':
        add_todo()
    elif choice == '2':
        list_todos()
    elif choice == '3':
        print('Goodbye!')
        break
    else:
        print('Invalid choice, please try again')

