while True:
    user_actions = input("Type add,show, edit, complete or exit: ")
    user_actions = user_actions.strip()
    
    match  user_actions:
        case 'add':
            todo = input("Enter todo: ") + "\n"
      
            with open('files/todos.txt', 'r') as file:
                 todos = file.readlines()
            todos.append(todo)
            with open('files/todos.txt', 'w') as file:
                 file.writelines(todos)         

        case 'show':
            with open('files/todos.txt', 'r') as file:
                 todos = file.readlines()

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1}-{item}"
                print(row)
                            
        case 'edit':
            print('Todos: ', todos)
            number = input("Number of the todo to edit: ")
            indexArr = int(number) - 1
            with open('files/todos.txt', 'r') as file:
                 todos = file.readlines()
            

            newItem = input("Enter new item: ")
            todos[indexArr] = newItem + "\n"
            print(todos)
            with open('files/todos.txt', 'w') as file:
                 file.writelines(todos)  


        case 'complete':
            
            comp = int(input("Whitch item is complete? "))
            with open('files/todos.txt', 'r') as file:
                 todos = file.readlines()
            index = comp - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('files/todos.txt', 'w') as file:
                 file.writelines(todos) 
            for index,item in enumerate(todos):
                print(index + 1, item)
            print("Item is removed")
        case 'exit':
            break
#        case _:
#            print("WRONG YOU WILL DIE")
print("Bye!")