tasklist=[23,"Jane",["lesson_23",560,{"currency":"KES"}],987,(76,"John")]
#1.Determing type of variable in  taskList using an inbuilt function
print(type(tasklist))

#2. Print KES
print(tasklist[2][2]["currency"])
# 3.Print 560
print(tasklist[2][1])
#4. Use a function to determine the length of taksList
print(len(tasklist))

#5. Change 987 to 789  using indexing only
#z=tasklist[3]="789"#without using indexing
#nom=tasklist[0][::-2]
z=tasklist[3]
z=str(z)
z=z[::-1]
print(z)

print(str(tasklist[3])[::-1])
#6. Change the name “John” to “Jane” .


