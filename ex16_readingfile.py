from sys import argv

script, filename = argv

print "We're going to open the file %r." % filename
print "If you would like to read the file hit RETURN."
raw_input("ok? ")

print "Opening the file..."
helpme = open(filename, 'r')
print helpme.read()
