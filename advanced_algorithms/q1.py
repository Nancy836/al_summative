import time


def add(n):

    sum=0 #sum starts off as zero

    for i in range(1, n+1): #looping  through n and  adding the each number in the range to the sum until all the numbers in the range have been added
        sum+= i


    return sum

print(add(8))



#testing

#testing the response time when the value of n is 10

def add1(n):
    # starting time
    start = time.time()

    sum=0 #sum starts off as zero

    for i in range(1, n+1): #looping  through n and  adding the each number in the range to the sum until all the numbers in the range have been added
        sum+= i


    return sum

    time.sleep(1)


    # end time
    end = time.time()
    print(f'Time taken for n=10: {end-start}')# time taken measured for testing purposes

print(add1(10))

#testing the response time when the value of n is 10000

def add2(n):
    # starting time
    start = time.time()

    sum=0 #sum starts off as zero

    for i in range(1, n+1): #looping  through n and  adding the each number in the range to the sum until all the numbers in the range have been added
        sum+= i


    return sum

    time.sleep(1)


    # end time
    end = time.time()
    print(f'Time taken for n=10000: {end-start}')# time taken measured for testing purposes

print(add2(10000))

#testing the response time when the value of n is 10000

def add3(n):
    # starting time
    start = time.time()

    sum=0 #sum starts off as zero

    for i in range(1, n+1): #looping  through n and  adding the each number in the range to the sum until all the numbers in the range have been added
        sum+= i


    return sum

    time.sleep(1)


    # end time
    end = time.time()
    print(f'Time taken for n=1000000: {end-start}')# time taken measured for testing purposes

print(add3(1000000))

#testing the response time when the value of n is 10000

def add4(n):
    # starting time
    start = time.time()

    sum=0 #sum starts off as zero

    for i in range(1, n+1): #looping  through n and  adding the each number in the range to the sum until all the numbers in the range have been added
        sum+= i


    return sum

    time.sleep(1)


    # end time
    end = time.time()
    print(f'Time taken for n=1000000000: {end-start}')# time taken measured for testing purposes

print(add4(1000000000))