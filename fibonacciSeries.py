lim = int(input("I want n numbers in fibonacci series, where n is: "))
temp = 0
fibList = [0,1]
for i in range (2, lim):
    nxtEle = fibList[-1] + fibList[-2]
    fibList.append(nxtEle)
print(fibList)

Example:

Input:
I want n numbers in fibonacci series, where n is: 12
Output: 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
