# Past examples are programmatically insecure
# You require arguments to be passed in but what if the wrong arguments are provided?
# Look at the timestable solution which changes numbers to text - what happens if you provide the number 30?
#
# One way of controlling these things uses conditions
# These enable specific operations to be carried out "if" something is the case or "else" something else is the case

a = 5

# first condition trial
if a >= 5:
	print("Value is greater than 5")
else:
	print("Value is less than 5")

# second condition trial
if a >= 5:
	print("Value is greater than 5")
elif a < 5:
	print("Value is less than 5")
else:
	print("Value is 5")

# if and (2 conditions)
a=3
b=5
if (a==3) and (b==5):
    print("a and b are as expected - great :)")
else:
	print("a and b not as expected - not great :(")