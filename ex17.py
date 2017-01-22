from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# If you wnat to know the size of the from_file
# print "The input file is %d bytes long" % len(indata)

# If you want the OS to check if the file already exists or not.
# TRUE for yes it exists, FALSE for no,
# print "Does the output file exist? %r" % exists(to_file)

# If you would like to ask to hit RETURN before proceeding
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
