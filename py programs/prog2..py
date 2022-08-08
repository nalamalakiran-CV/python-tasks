"""python program to print the number which is missing in a
list ranging numbers 1 to 100"""

def missingNo(N):
    a = []
    for x in range(N[0],N[-1]+1):
        if x not in N:
            a.append(x)
    print(a)

N = [10,20,30]
missingNo(N)