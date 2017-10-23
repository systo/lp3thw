# Find all the places where a string is put inside a string

types_of_people = 10
# Spot 1
x = f"there are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# Spot 2 and 3
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# Spot 4
print(f"I said: {x}")

# Spot 5
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Spot 6
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)