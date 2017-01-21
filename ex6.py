# sets up variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# prints variables
print x
print y
# prints variables and shows the difference between %s and %r
print "I said: %r." % x
print "I also said: '%s'." % y
# sets up variables
hilarous = False
joke_evaluation = "Isn't that joke so funny?! %r"
# prints above variables
print joke_evaluation % hilarous
# sets up variables
w = "This is the left side of..."
e = "a string with a right side."
# prints variables concatinated
print w + e
