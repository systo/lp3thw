# Declaring a variable
types_of_people = 10

# Declaring a variable with an inset, formatted string
x = f"there are {types_of_people} types of people."

# declaring another couple of variables
binary = "binary"
do_not = "don't"

# declaring another string, only with two inset variables
y = f"Those who know {binary} and those who {do_not}."

# printing two strings
print(x)
print(y)

# printing a string with an inset string variable
print(f"I said: {x}")

#printing another string with an inset variable. The ' work as they are not
# used as the boundary? characters, and also don't need to be escaped
print(f"I also said: '{y}'")

# declaring anther variable this time a boolean
hilarious = False

# declaring a string with an inset string variable that can be formatted later
joke_evaluation = "Isn't that joke so funny?! {}"

# adding a variable to the joke_evaluation string with the format method?
print(joke_evaluation.format(hilarious))

# declaring two halves of a string
w = "This is the left side of..."
e = "a string with a right side."

# printing both halves together using the + symbol.  apparently this doesn't
# auto-add a space
print(w + e)

# but the , adds a space between both halves
print(w, e)