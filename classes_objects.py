#terminology
    # a class is a group of related functions and variables
    #object orientated programming
    # a function inside a class is methods
    # object-instance of a class
    #        -member of a class
    #constructor-special methodb that runs every time you(instantiate)create an instance a class

class Student:
    math = 0
    eng = 0
    kis = 0
    ssr = 0
    sci = 0
    total = 0
    average = 0
    grade = ""

    def __init__(self,math,eng,kis,ssr,sci):
        self.math = math
        self.eng = eng
        self.kis = kis
        self.ssr = ssr
        self.sci = sci
        self.findTotal()
        self.findAverage()
        self.findGrade()

    def findTotal(self):
        self.total=self.math + self.eng + self.kis + self.sci + self.ssr

    def findAverage(self):
        self.average = self.total / 5

    def findGrade(self):
        ave = self.average
        if ave >= 80 and ave<=100:
            self.grade = "A"
        elif ave >=70 :
            self.grade = " B"
        elif ave >=60 :
            self.grade = " C"
        elif ave >=50 :
            self.grade = " D"
        else:
            self.grade = "E"
