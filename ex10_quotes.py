# this is the drills for escape characters
eyes = "Brown"
hair = "Gray"
escape_test = "Let's test the escape characters"
script_kiddy = """
"Let's test the quotes with:
"Testing double \" quotes ",
'and then single\''
"""

print escape_test
print script_kiddy

print "It's \"double quotes\"",
print "..then \'single quotes\'."

print "Test \"double with %r." % escape_test

# end user view vs. debub for double quotes
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's got %r eyes and %r hair." % (eyes, hair)


# end user view vs. debub for single quotes
print 'He\'s got %s eyes and %s hair.' % (eyes, hair)
print 'He\'s got %r eyes and %r hair.' % (eyes, hair)
