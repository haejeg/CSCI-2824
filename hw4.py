#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework4:
    def smallCount(self, nums):
        smalls = []
        for i in nums:
            count = 0
            for j in nums:
                if (j < i):
                    count+=1
            smalls.append(count)
            
        return smalls
        # Start your code from here

# For testing your code uncomment below lines.
# l = Homework4()
# print(l.smallCount([8,1,2,2,3]))
# Comment or delete the above test code before submitting.
