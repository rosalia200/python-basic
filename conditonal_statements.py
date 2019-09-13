# in python if is th only conditonal statement
bal=10
wd=20
name="name"
if wd<= bal and name=="said":
    print("withdraw success")
else:
    print("insufficient funds")

# if elif else
score = "poor"

if score == "Good" :
    print(" Green label")
elif score == "Excellent":
    print(" blue label")
elif score == "Poor"or score == "poor": #or " poor " or "poor":
    print(" Red label")
else:
    print("Unrecognized")


# ask a user o enter the following marks
# math
# eng
# kis
# ssc
# sci
# calculate the total and average
# using average give grade to the student
math=input("math : ")
eng=input("eng : ")
kis=input("kis : ")
ssc=input("ssc : ")
sci=input("sci : ")
total=int(int(math) + int(eng) + int(kis) + int(ssc) + int(sci))
print(total)
avg= total/5
print(avg)
if avg >100 or avg < 0:
    print("UNREALISTIC")
elif avg >= 80:
    print("A")
elif avg >= 70:
    print("B")
elif avg >= 60:
    print("C")
elif avg  >= 50:
    print("D")
elif avg >100 or avg < 0:
    print("UNREALISTIC")
else:
    print("E")

