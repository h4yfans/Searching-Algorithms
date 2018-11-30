def search(mylist, n):
    found = False
    first = 0
    last = len(mylist)-1

    while first <= last and not found:
        mid = (last+first)//2
        if mylist[mid] == n:
            print(f'Found! Index of {mid}')
            found=True
        else:
            if mylist[mid] > n:
                last  = mid - 1
            else:
                first = mid + 1

    return found
        
mylist = [3, 4, 6, 9, 23, 45, 54, 78, 86, 90, 100]
n = 86

search(mylist, n)
