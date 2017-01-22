# variable for the number of cars
cars = 100
#variable for amount of space per cars
space_in_a_car = 4.0
# available number of drivers
drivers = 30
# number of passengers needed rides
passengers = 90
# number of cars that are not being driven
cars_not_driven = cars - drivers
# number of cars driven - which is equivalent to number of drivers
cars_driven = drivers
# total capacity that the car pool can handle
carpool_capacity = cars_driven * space_in_a_car
# number passengers that each car will take within the car pool
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
