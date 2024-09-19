#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework6:
    def isPower(self, n):
        # Start your code from here
        if n == 1:
            return True
        elif n <= 0:
            return False
        else:
            while n % 15 == 0:
                n = n / 15
            return n == 1