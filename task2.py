var1= input("num1 :")
var2= input("num2 :")
var3= input("num3 :")
def findLargest():
    if var1 > var2 and var1 > var3:
        return (var1)
    elif var2 > var1 and var2 > var3:
        return (var2)
    elif var3 > var1 and var3 > var2:
        return (var2)
    else:
        print("equal")

# var1= input("num1 :")
# var2= input("num2 :")
# var3= input("num3 :")
findLargest()