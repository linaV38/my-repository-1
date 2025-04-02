global_var = "I'm a global variable"

def my_function():
    global global_var
    global_var = "I defined inside inside the scope of my_function"

print(global_var)
my_function()
print(global_var)

