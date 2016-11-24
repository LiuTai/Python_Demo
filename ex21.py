# practic 21 Funcitons can return something
def add(a, b):
    print "ADDing %d + %d " %(a, b)
    return a + b
def substract(a , b):
    print "subtracting %d - %d" % (a, b)
    return a - b
def multiply(a, b):
    print"multiplying %d * %d" % (a, b)
    return a * b
def divide(a, b):
    print "dividing %d / %d" %(a,b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiple(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# A puzazle for the extra credit, type is in anyway.
print "here is a puzzle."

what = add(age, subtract(height, muitiply(weight,divide(iq,2)))) 

print "That becomes:", what, "can you do it by  hand?"

