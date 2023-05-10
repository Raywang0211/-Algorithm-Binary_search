def BS(s,target):
    low = 0
    upper = len(s)-1

    while low<=upper:
        mid = (upper+low)//2
        if s[mid]>target:
            upper = mid-1
        elif s[mid]<target:
            low = mid+1
        else:
            return mid
    return -1


test_case = [1,3,11,56,57,60,67,77,88]
target = 11
ans = BS(test_case,target)
if ans ==-1:
    print("No index")
else:
    print(ans)
    print(test_case[ans])