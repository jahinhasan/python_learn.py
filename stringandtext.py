x = "there are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary,do_not)

print (x)
print (y)

print ("I said : %r"%x)
print("i also said : %s"%y)

hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print(joke_evaluation% hilarious)

w="this is the left sideof .."
e ="a string wth a right side."

print (w+e)