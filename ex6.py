# variable creation with a string calling a value
x = "There are %d types of people." % 10
# variable to insert the word binary.
binary = "binary"
# a variable to insert don't
do_not = "don't"
# bad joke about binary using defined variables.
y = "Those who know %s and those who %s." % (binary, do_not)

# print the first variable x
print x
# print the variable y
print y

# print the variable phrase
print "I said: %r." % x
print "I also said: '%s'." % y

# create variable hilarious
hilarious = False
# create variable joke_evaluation sentence calling hilarious variable.
joke_evalutation = "Isn't that joke so funny?! %r"

# print the variable joke eval and response.
print joke_evalutation % hilarious

# Two varialbes that will be joined.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
