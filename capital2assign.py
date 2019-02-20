from multiprocessing import Process,Pool

listnum = [1,2,3,4]

def square(num):
    return num * num

def sum(numlist):
    numsum = 0
    for num in numlist:
        numsum = numsum + num
    else:
        print(numsum)