# defines the function  cheese_and_crackers then prints 4 lines
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# passes cheese_and_crackers two numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# passes cheese_and_crackers two variables that have been assigned
# numbers
print "OR, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# arguments passed to cheese_and_crackers are math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# arguments passed to cheese_and_crackers are math and variables combined
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
