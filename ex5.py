name = 'Zed A. Shaw'
age = 35 # not a lie in 2009
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

weight_kg = weight*0.45
height_cm = height*2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "My weight in kilograms is %dkg." % weight_kg
print "My height in centimetres is %dcm." % height_cm
