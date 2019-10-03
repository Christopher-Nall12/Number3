# variables

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity02 = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven
print("there are ", cars, "cars available")
print("there are only ", drivers, "drivers available")
print("we can transport", carpool_capacity02, "people today")
print("we have", passengers, "to carpool today")
print("we need to put about", average_passengers_per_car, "in each car" )


# more variables

myName = "Chris"
myAge = 567
myHight = 80 # inches
myEyes = "brown"
myTeeth = "white"
myHair = "blonde"

print("let's talk about %s. " %myName)
print("he's %d inches tall." %myHight)
print("he's got %s eyes and %s hair." % (myEyes, myHair))
print("his teeth are usually %s depending \n on the coffee" % myTeeth)
print("if i had %d and %d, i get %d" % (myAge, myHight, myAge + myHight))
