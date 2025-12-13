#now we will see how we can import from utils.py

#if we import module as a namespace
import utils
utils.display('There is no warning')

#if we want to import all functions from utils.py
from utils import *
display('There is no warning')

#if we want to import only a specific function from utils.py
from utils import display
display('This is a warning message')

#if you realized it, we have two different usages of display function
#one is utils.display and another is just display
#the difference is because of the way we imported the function
#neverthless,in big projects, using the first way is more common