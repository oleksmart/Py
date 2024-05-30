
#from functions import get_todos, write_todos
from modules import functions

while True:
    user_actions = input("Type add,show, edit, complete or exit: ")
    user_actions = user_actions.strip()
    
    if user_actions.startswith('add'):
            todo = user_actions[4:]
            todos = functions.get_todos()
            todos.append(todo + '\n')
            functions.write_todos(todos)   

    elif user_actions.startswith('show'):
        todos = functions.get_todos()
        for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}-{item}"
                print(row)
                            
    elif user_actions.startswith('edit'):
        try:
            number = int(user_actions[5:])
            print(number)
            indexArr = int(number) - 1
            todos = functions.get_todos()
            
            newItem = input("Enter new item: ")
            todos[indexArr] = newItem + "\n"
            print(todos)
            functions.write_todos(todos)  

        except ValueError:
            print("Your command is not allowed")
            continue

        #^^^^^^^^^^^^^this will execute
        #user_actions = input("Type add,show, edit, complete or exit: ")
        #user_actions = user_actions.strip()
         
    elif user_actions.startswith('complete'):
            try:
                comp = int(input("Whitch item is complete? "))
                todos = functions.get_todos()
                index = comp - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                functions.write_todos(todos)  

                print("Item is removed")
            except IndexError:
                 print("Choose the right number!")
    elif user_actions.startswith('exit') or user_actions.startswith('x'):
            break
    else:
          print("Command is not valid - you are looser!")

print("Bye!")