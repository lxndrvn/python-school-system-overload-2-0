# Write here your console application
from menu import *

if __name__=='__main__':
    menu=Menu()
    while menu.session==True:
        menu.login()
