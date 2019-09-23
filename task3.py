# input_string = input("marks:  ")
# list  = input_string.split()




# def make2(l):
#     return l[0:int(len(l)/2)]
#
#     # part2=list[int(len(l)/2):]
#     # print(type(part2))
#
#
# l=1,2,3,4,5,6,7,8
# make2(l)
# print("Calculating sum of element of input list")
# sum = 0
# for num in list:
#     sum += int (num)
# print("Sum = ",sum)


    # Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
    # makes a new list of only the first and last elements of the given list. For practice, write this code inside a function
def first_last(w):
    first=w[0]
    last=w[-1]
    return str(first) + "\n" + str(last)

input_string = input("marks:  ")
list  = input_string.split()
a=first_last(list)
print(a)
