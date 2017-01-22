name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
# this is the value to multiply inches by to get centimeters
convert_to_centimeter = 2.54
convert_to_kg = 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "He's %d tall in centimeters." % ( height * convert_to_centimeter)
print "He weighs %r in kilograms." % (weight * convert_to_kg)


#this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
