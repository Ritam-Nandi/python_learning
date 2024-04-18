import random


start=(int)(input("Enter start of the range "))
end=(int)(input("Enter end of the range "))

a = random.randrange(start,end)

count=1

guess = (int)(input("Enter a number:  "))

while guess!=a:
    guess = (int)(input("Try Again:  "))
    count = count+1
1
print("You guessed the correct number in %d tries" % (count))

