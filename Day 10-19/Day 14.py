class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
  
    def computeDifference(self):
        p = 0 
        j = 100
        for i in (self.__elements):
            q = i
            p = max(q, p)
            j = min(q, j)
        self.maximumDifference = (p - j)
        # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
