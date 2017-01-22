# load the argv module
from sys import argv

# define two arguments to be given
script, filename = argv

#create a variable that will open the specified file
txt = open(filename)

# print the question to the user to provide the name of file to be opened.
print "Here's your file %r:" % filename
#call the open file variable defined by txt.
print txt.read()

# print the file again after user provides it
print "Type the filename again:"
file_again = raw_input("> ")

# define variable for open file again
txt_again = open(file_again)

#print the output of the file again.
print txt_again.read()

#close file
txt.close()
txt_again.close()
