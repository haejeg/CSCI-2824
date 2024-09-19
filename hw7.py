from math import factorial
from collections import Counter

#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class Homework7:
    def count_permutations(self, input):
        c_count = Counter(input)

        total_permu = factorial(len(input))

        for count in c_count.values():
            total_permu//= factorial(count)
        
        return total_permu
#pass
# # For testing your code uncomment below lines.
# l = Homework7()
# print(l.count_permutations( "testing"))
# # Comment or delete the above test code before submitting.