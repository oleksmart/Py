def get_todos(filepath="files/todos.txt"):
    """ Read text file description."""

    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local



def write_todos(todos_arg, filepath="files/todos.txt"):
     """Write todo items in the file."""
     
     with open(filepath, 'w') as file:
        file.writelines(todos_arg)   