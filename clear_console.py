import os
# Clearing the Screen
def clear_console():
    # posix is os name for Linux or mac
    if(os.name == 'posix'):
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')