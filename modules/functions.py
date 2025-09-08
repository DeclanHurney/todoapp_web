# Both modules here are declared with default arguments (filepath)
# therefore we don't need to specify these arguments where we are calling these modules
# The default arguments must follow non-default arguments

FILEPATH = './todos.txt'
def read_todos_file(filepath=FILEPATH):
    # Return the contents of the text file, returning the contents as a list
    with open(filepath, "r") as file_to_read:
        todos_local = file_to_read.readlines()
    return todos_local

#the following help command will display the docstring you added to the function
# help(read_todos_file)
# Help on function read_todos_file in module __main__:




def write_todos_file(todos_arg, filepath=FILEPATH):
    # Add new contents of a list to the text file
    with open(filepath, "w") as file_to_write:
        file_to_write.writelines(todos_arg)

# if __name__ == "__main__":
#     print(__name__)
#     print("Hello from Functions")