def super_digit(n,k):

    superdigit = 0

    p = str(n) * int(k) # getting the p value by repeating n k times

    print(p)

    for digit in str(p):
        superdigit += int(digit) #adding the digits in p to get the first superdigit

    #print(superdigit)

    if superdigit > 10: #if the superdigit is greater than 10, meaning it has more than 1 digit, repeat the process until
        #the superdigit has only one digit

        super_digit(str(superdigit),1)#calling the superdigit function again


    else:
        print(superdigit)#if the superdigit has only  one digit, then that is the superdigit

#taking input for the n and k values separated by a space
n,k = (input('Please enter the integer (n),  leave  space then enter the number of timesto concatenate it (k): ')).split()
super_digit(n,k)