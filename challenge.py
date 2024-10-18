print("16. Input number and check if it divide by 3")
num = str(input("Input number :"))
list_num = list(num)
print(list_num)

sum_digits = sum(int(i) for i in list_num)
if sum_digits % 3 == 0:
    print("The number are divide by 3")
else:
    print("The number are NOT divide by 3")

print("\n")
print("17. Check if input string are reverse or NOT")
str_r = input("Enter string :")
len_end_string = len(str_r)
middle_list_size: int = (len_end_string // 2)
if middle_list_size % 2 == 0:
    middle_list_size -= 1
    index_list = 0
    while index_list <= middle_list_size:
        if str_r[index_list] == str_r[len_end_string - index_list - 1]:
            index_list += 1
        else:
            break

    if index_list - 1 == middle_list_size:
        print("The string are reverse :")
    else:
        print("The string are NOT reverse :")
