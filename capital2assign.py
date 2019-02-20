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

with Pool(5) as p:
        print("Result(process p1):",p.map(square,listnum ))
        sum(p.map(square,listnum ))


if __name__=="__main__":
    listnum = [1,2,3,4]
    

    with Pool(5) as p:
        print("Result(main program):",p.map(square,listnum ))
        sum(p.map(square,listnum ))
