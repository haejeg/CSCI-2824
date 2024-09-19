#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
from itertools import permutations 

class Homework8:
    def canRearrange(self, str1, str2):
        perm1 = [''.join(p) for p in permutations(str1)]
        perm2 = [''.join(p) for p in permutations(str2)]

        p1 = True
        p2 = True

        for i in list(perm1):
            for j in list(perm2):
                c1 = 0
                c2 = 0
                print(range(len(str1)))
                for x in range(len(i)):
                    print("Comparing ", i[x], " and",j[x], p1, c1)
                    if (i[x] > j[x]):
                        p1 = False
                        c1 = 0
                    else:
                        p1 = True
                        c1 += 1

                for x in range(len(i)):
                    print("Comparing ", i[x], " and ",j[x], i[x] < j[x], c2)
                    if (i[x] < j[x]):
                        p2 = False
                        c2 = 0
                    else:
                        p2 = True
                        c2 += 1
                    
                if c1 == len(str1) or c2 == len(str2):
                    return True
                   
                
                # if (str2[0] >= str1[0])

        
        return False
        # Start your code from here


# For testing your code uncomment below lines.
# l = Homework8()
# print(l.canRearrange("pqr","xyp"))
# Comment or delete the above test code before submitting.
