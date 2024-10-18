print("1. Input a decimal number. If it is greater than 10, print the difference between it and 10; otherwise, print its product with 10")
num1: int = int(input("Enter number :"))
if num1 > 10:
    print(f"The input are greeter then 10 the difference are {num1- 10}\n")
else:
    print(f"The multiple of 10 * {num1} = {num1 * 10}\n")

print("2. Input three decimal numbers and print their sum only if the sum is greater than 100; otherwise, print The sum is less than 100")
num_1: int = int(input("Enter number1 :"))
num_2: int = int(input("Enter number2 :"))
num_3: int = int(input("Enter number3 :"))
num_sum = num_1 + num_2 + num_3
if num_sum > 100:
    print(f"The sum of 3 number are {num_sum}:\n")
else:
    print("The sum is less than 100\n")

print("3. Input two decimal numbers and print the larger fraction. If the fractions are equal, print Equal")
fraction1: float = float(input("Enter fraction1 number :"))
fraction2: float = float(input("Enter fraction2 number :"))
f1: float =  fraction1 - int(fraction1)
f2: float =  fraction2 - int(fraction2)
######
# for case 2.33 99.33 there is problem which => EQUAL <= not working
# Enter fraction1 number :2.33
# Enter fraction2 number :99.33
# The bigger :0.33
# f1 :0.33000000000000007
# f2 :0.3299999999999983
######
if f1 == f2:
    print("Equal\n")
elif f1 > f2:
    print(f"The bigger :{f1:.2f}")
else:
    print(f"The bigger :{f2:.2f}")
print(f"f1 :{f1}")
print(f"f2 :{f2}\n")

print("4. Input an age and verify that it is valid (greater than 0 and less than 120). If it is not valid, print Invalid age")
age: int = int(input("Enter your age :"))
if 0 <= age <= 120:
    print(f"Youe age {age}")
else:
    print("Invalid age")

print("5. Input a three-digit number and print its middle digit")
number_three: int = int(input("Input a three-digit number :"))
number_three = number_three // 10
middle_number:int = number_three // 10
print(f"{number_three - middle_number*10}\n")





