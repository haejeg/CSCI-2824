#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework5:
    def localMaximum(self, nums):
        # What? I've literally  never  created a program for logn so i have  no  idea what  it  even looks  like
        # Start your code from here
        highest = nums[0]
        # for i in range(len(nums) - 2):
        #     if nums[i] < highest and nums[i+2] < highest:
        #        highest = nums[i + 1]
        #        return highest
        # if nums[len(nums) - 1] > nums[len(nums) - 2]:
        #     return nums[len(nums) - 1]
        # return
        for i in range(len(nums)):
            if (i + 1) >= len(nums) and (nums[i - 1]) < nums[i] :
                return nums[i]
            elif (i - 1) < 0 and (nums[i + 1]) < nums[i]:
                return nums[i]
            else:
                if (nums[i - 1]) < nums[i] and (nums[i + 1]) < nums[i]:
                    return nums[i]
        return


        

# For testing your code uncomment below lines.
# l = Homework5()
# print(l.localMaximum([8, 10, 12, 13]))
# Comment or delete the above test code before submitting.
