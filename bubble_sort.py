def bubbleSort(mylist):
    for num in range(len(mylist)-1,0,-1):
        for i in range(num):
            if mylist[i] > mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp



mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(mylist)
print(mylist)
