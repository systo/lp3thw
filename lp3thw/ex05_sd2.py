my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Some variables that convert inches and pounds to centimeters and kilograms
to_centimeter = my_height * 2.54
# Learned the built-in round function
to_kilogram = round(my_weight * 0.453592, 2) 

# Testing the new variables
print(f"He's {to_kilogram} kilograms heavy.")
# Combining with the int function
print(f"He's {int(round(to_centimeter, 0))} centimeters tall, rounded up of course.") 


