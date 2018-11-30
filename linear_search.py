def search(mylist,n):
    for item in mylist:
        if item == n:
            return True

    return False


mylist = [5,8,4,6,9,2]
n = 4

if search(mylist, n):
    print('Found')
else:
    print('Not Found')

