from typing import List
class Homework9:
    def find_Inspector(self, n: int, trust: List[List[int]]) -> int:
        print(trust)
        print(n)
        if n <= 0 or not trust:
            return -1
        trustedperson = trust[0][1]
        untrustworthy = []
        for i in trust:
            for j in trust:
                if i[1] == j[0]:
                    untrustworthy.append(j[0])
                    break
            
            if i[1] not in untrustworthy:
                count = 0
                for m in trust:
                    if m[1] == i[1]:
                        count+=1
                if (count + 1 == n):
                    return i[1]
        print(untrustworthy)
        return -1
            
# For testing your code uncomment below lines.
# c = Homework9()
# n = 4
# trust = [[1,2],[2,3],[4,3],[2,1]]
# print(c.find_Inspector(n, trust))

# c = Homework9()
# n = 3
# trust = [[1, 3], [2, 3]]
# print(c.find_Inspector(n, trust))
 
# Comment or delete the above test code before submitting.

