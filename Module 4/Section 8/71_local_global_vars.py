#   Demonstrate local and global variables.


# Local varialbles
local_a = 10


def func():
    local_a = 20

    print(f"Local_a inside func {local_a}")


func()
print(f"Local_a outside func {local_a}")


print()

# Global variables.

global_a = 10


def func2():

    global_a = 20
    print(f"Global_a inside fun2 {global_a}")


print(f"Global_a outside before fun2 called {global_a}")
func2()
print(f"Global_a outside fun2 {global_a}")
