def findDupe(self, num):
    num.sort()
    for i in range(1, len(num)):
        if num[i] == num[i-1]:
            return num[i]