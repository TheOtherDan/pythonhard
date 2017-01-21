# Number of cars
cars = 100
# amount of spac each car has
space_in_a_car = 4
# the number of drivers
drivers = 30
# the number of passengers
passengers = 90
# calculate how many cars not being driven
cars_not_driven = cars - drivers
# calculate how many cars are being driven
cars_driven = drivers
# calculate how many people can join the carpool
carpool_capacity = cars_driven * space_in_a_car
# calculate the number of passengers need to fit in each car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
