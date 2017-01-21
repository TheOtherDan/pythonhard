# imports argv from sys module
from sys import argv

# gets variables from command prompt
script, filename = argv

# sets variable txt to be the file specified above
txt = open(filename)

# prints a message then prints file content using .read()
print "Here's your file %s:" % filename
print txt.read()

# prompts for user input
print "Type the filename again:"
file_again = raw_input(">")

# sets txt_again to hold the file
txt_again = open(file_again)

# prints file content using .read()
print txt_again.read()

txt.close()
txt_again.close()
