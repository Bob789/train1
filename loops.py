print("6. Check and add all the prime numbers from 1 to n in ascending order")
n: int = int(input("Enter n number :"))
for i in range(n, 1-1, -1):
    print(f"n = {i} ",end =" ")

print("\n")
print("7.Check and add all the even numbers between two consecutive primes")
n1: int = int(input("Enter n1 number :"))
n2: int = int(input("Enter n2 number :"))

if n1 > n2:
    if not n2 % 2 == 0:
        n2 += 1
    for i in range(n2, n1, 2):
        print(i, end=" ")
else:
    if not n1 % 2 == 0:
        n1 += 1
    for i in range(n1, n2, 2):
        print(i, end=" ")

print("\n")
print("8. Check and add all the numbers divisible by 3 and 5 simultaneously up to n")
n_num: int = int(input("Enter n number :"))

for i in range(3, n_num+1):
    if i % 3 == 0:
        print(i, end=" ")
    elif i % 5 == 0:
        print(i, end=" ")

print("\n")
print("9. Check and add all the multiples of 7 from 7 to n")
n7: int = int(input("Enter n number :"))
print("multiples 7")
for i in range(7, n7 + 1, 7):
    print(f" {i} ",end =" ")

