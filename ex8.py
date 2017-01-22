# sets a variable to call 4 values in debug mode.
formatter = "%r %r %r %r"

# print the numbers 1 - 4 in debug
print formatter % (1, 2, 3, 4)
# print 1- 4 using spelled values
print formatter % ("one", "two", "three", "four")
# use debug format for True-False
print formatter % (True, False, False, True)
# print the formatter varaible 4 times.
print formatter % (formatter, formatter, formatter, formatter)
#print each line below calling the formatter varialbe to debug each line.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
