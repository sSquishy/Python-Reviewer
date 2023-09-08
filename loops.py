#Loops example

#for loop
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print("Fruit:", x)


#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1


#while loop with if-else
num = 0
while num < 5:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

    num += 1

#for loop with if-else
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")
