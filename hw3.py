import math

#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework3:
    def isRightAngledTriangle(self, x1,y1,x2,y2,x3,y3):
        # Start your code from here
        length1 = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
        length2 = math.sqrt(math.pow((x3 - x2), 2) + math.pow((y3 - y2), 2))
        length3 = math.sqrt(math.pow((x1 - x3), 2) + math.pow((y1 - y3), 2))
        return (round(math.pow(length1, 2) + math.pow(length3, 2), 4) == round(math.pow(length2, 2), 4)) or (round(math.pow(length2, 2) + math.pow(length3, 2), 4) == round(math.pow(length1, 2), 4)) or (round(math.pow(length1, 2) + math.pow(length2, 2), 4) == round(math.pow(length3, 2), 4))


# For testing your code uncomment below lines.
# l = Homework3()
# print(l.isRightAngledTriangle(0, 0 , 3, 0, 3, 4))
# Comment or delete the above test code before submitting.
