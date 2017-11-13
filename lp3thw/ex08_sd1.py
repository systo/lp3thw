# creates a string with four variables
formatter = "{} {} {} {}"

# calls the format function on the formatter string; inserts four variables into the string
print(formatter.format(1, 2, 3, 4))
# calls the format function on the formatter string; inserts four variables into the string
print(formatter.format("one", "two", "three", "four"))
# calls the format function on the formatter string; inserts four variables into the string
print(formatter.format(True, False, False, True))
# recursion, calls formatter on itself
print(formatter.format(formatter, formatter, formatter, formatter))
# prints echo using the phonetic alphablet
print(formatter.format(
	"Echo",
	"Charlie",
	"Hotel",
	"Oscar"
))