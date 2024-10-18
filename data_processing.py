print("11. Add all the negative numbers")
SENTINEL: int = 0
sum_negative: int = 0
while True:
    number: int = int(input('Enter numbers, to exit enter 0 :'))
    if number == SENTINEL:
        break
    if number < 0:
        sum_negative += number

print(f" SUM negative = {sum_negative}\n")

print("12. Enter 10 numbers to list, print in reverse order")
SENTINEL: int = 10
list_numbers: list [int] = []
for i in range(1, SENTINEL + 1):
    list_numbers.append(input(f" Enter number {i} :"))

print(list_numbers[::-1],"\n")

print("13. Input list of numbers untile type SENTINEL = 0, print how meny prime numbers ")
SENTINEL: int = 0
input_list: list [int] = []
while True:
    num: int = int(input('Enter numbers, to exit enter 0 :'))
    if num == SENTINEL:
        break
    else:
        input_list.append(num)

print(f"Your input list : {input_list}")

#  [append(x)            for x in                          check if rishoni]
prime_numbers = [x       for x in input_list     if all([x % i for i in range(2, x)])]

# remove negative and 1 cose they are not prime number
prime_numbers = [x for x in prime_numbers if x > 1]
print(f" The prime numbers are: {prime_numbers}")
print(f" There are {len(prime_numbers)} numbers\n")

print("14. Input 5 number then print the average, ")
input_list: int = []
average_list: int = []
for i in range(1, 6):
    input_list.append(int(input(f'Enter number {i} :')))

print(f"Your input list : {input_list}")
average = sum(input_list) / 5
print(f"average :{average}")

average_list = [i for i in input_list if average < i]
print(f"Number which greater then  average {average}: {average_list}")


print("\n")
print("15. Input two numbers :")
bigger: int = int(input("Enter number 1 :"))
smaller: int = int(input("Enter number 2 :"))
temp: int = None
if  bigger < smaller:
    temp = smaller
    smaller = bigger
    bigger = temp

print(bigger, " / ", smaller," =", end=" ")
counter: int = 0
while bigger >= smaller:
    bigger -= smaller
    counter +=1

print(counter)








