import colorama

colorama.init()
print(colorama.Fore.RED + 'This is red')

from colorama import *
init()
print(Fore.BLUE + 'This is blue')

from colorama import init, Fore
print(Fore.GREEN + 'This is green')

#we installed the colorama module using the requirements.txt file
#but just writing "import requirements" will not work
#because requirements.txt is not a Python module
#we should run this command in the terminal: pip install -r requirements.txt
#then we will be able to import colorama module
#but we will not use the form "from requirements import colorama"
#because, as mentioned, requirements.txt is not a Python module