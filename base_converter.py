## This a base converter file
##
from unittest import case

name = input ('Please type your name and press Enter. ')
# print ('Hi, ', name, 'this program will convert integer numbers between three base classes. ')


while (True):
    print ('\n Your input options are: Quit(X), Binary(b), Decimal(d), Hexadecimal(h)')
    convert = input ("Type the first letter of your choice and press Enter.")
    if len (convert) < 1 or len (convert) > 2:
        print ("Kindly input correct command.")
    elif convert[0] in ['x', 'X']:
        print ('Thanks for playing! Existing the program now!')
        break

    if convert[0] in ['b', 'B']:
        num_in = int (input ("Type the integer you want to convert to the base 2."), 10)
        print ('The integer ', num_in, ' in binary : {0:b}'.format (num_in))
    elif convert[0] in ['h', 'H']:
        num_in = int (input ("Type the integer you want to convert to the base 16."), 16)
        print ('The integer ', num_in, ' in hexadecimal : {0:x}'.format (num_in))
    elif convert[0] in ['d', 'D']:
        num_in = int (input ("Type the integer you want to convert to the base 10."), 10)
        print ('The integer ', num_in, ' in decimal : {0:d}'.format (num_in))
    else:
        print ("Something is wrong with our code")
