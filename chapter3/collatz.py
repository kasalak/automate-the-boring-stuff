
def collatz(number):
    if number % 2 == 0: # even number
        return number // 2
    elif number % 2 == 1: # odd number
        return 3 * number + 1

print("Please input a number: ")
number = int(input())
print(collatz(number))
number = collatz(number)
while collatz(number) > 1 :
    number = collatz(number)
    print(number)
if collatz(number) == 1:
    print(collatz(number))
