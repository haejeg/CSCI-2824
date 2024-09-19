#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
class Homework10:
    def hasPath(self, edges, start, end):
        if len(edges) == 0:
            return True
        for i in edges:
            if i[0] == start and i[1] == end:
                return True
        
        for i in edges:
            if i[0] == start:
                if self.hasPath(edges, i[1], end):
                    return True
        
        return False

# For testing your code uncomment below lines.
# l = Homework10()
# print(l.hasPath([(4, 3), (1, 4), (4, 8), (1, 7), (6, 4), (4, 2), (7, 4), (4, 0), (0, 9), (5, 4)], 5, 9))
# Comment or delete the above test code before submitting.
