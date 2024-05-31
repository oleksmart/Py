def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local


while True:
    user_actions = input("Type add,show, edit, complete or exit: ")
    user_actions = user_actions.strip()
    
    if user_actions.startswith('add'):
            todo = user_actions[4:]
      
            todos = get_todos()
            
            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                 file.writelines(todos)         

    elif user_actions.startswith('show'):
        todos = get_todos()
        for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}-{item}"
                print(row)
                            
    elif user_actions.startswith('edit'):
        try:
            number = int(user_actions[5:])
            print(number)
            indexArr = int(number) - 1
            todos = get_todos()
            
            newItem = input("Enter new item: ")
            todos[indexArr] = newItem + "\n"
            print(todos)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not allowed")
            continue

        #^^^^^^^^^^^^^this will execute
        #user_actions = input("Type add,show, edit, complete or exit: ")
        #user_actions = user_actions.strip()
         
    elif user_actions.startswith('complete'):
            try:
                comp = int(input("Whitch item is complete? "))

                todos = get_todos()
                index = comp - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)
                with open('todos.txt', 'w') as file:
                    file.writelines(todos) 
                for index,item in enumerate(todos):
                    print(index + 1, item)
                print("Item is removed")
            except IndexError:
                 print("Choose the right number!")
    elif user_actions.startswith('exit') or user_actions.startswith('x'):
            break
    else:
          print("Command is not valid - you are looser!")

print("Bye!")