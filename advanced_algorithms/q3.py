import numpy as np

def encrypt():

    global text # ensuring that this variable is accessible  by the decrypt  function

    text = 'Plain text' #input text
    t_length = len(text) # length of text


    # Declaring number of columns which are equal to the length of the text
    C = t_length

    global array1,array2,a_length,a_length2 #ensuring that these variables are accessible by the decrypt function


    array1= ['']*C # creating first  array  which acts  as row  1
    array2=['']*C # creating second  array  which acts  as row  2

    a_length = len(array1)
    a_length2 = len(array2)
    #encrypted1= ''
    #encrypted2 = ''

    # inserting the text in the array while  skipping one space and starting from index 0
    for i,j in zip(range(0,t_length,2),range(0,a_length,2)):
        array1[j]= text[i]
        #encrypted1+=array1[j]
    # inserting the text in the array while  skipping one space and starting from index 1
    for i,j in zip(range(1,t_length,2),range(1,a_length2,2)):
        array2[j]= text[i]
        #encrypted2 += array2[j]

    matrix= np.stack([array1, array2], axis=0) #combining the arrays to make a matrix

    #encrypted= encrypted1 + encrypted2


    print('Input: ' + text)
    print('Encrypted message: ')
    print(str(matrix))
    #print('The encrypted message as text: ' + encrypted)



def decrypt():

    encrypt()#calling the encrypt function

    msg2=[]
    msg_len= len(text)
    decrypted= ''

    for x,y,z,a in zip(range(0,a_length,2),range(1,a_length2,2), range(0,msg_len,2),range(1,msg_len,2)):

        msg2.insert(z, array1[x]) #inserting only the letters from array1 into an array skipping one space, and starting from index 0
        msg2.insert(a, array2[y])#inserting only the letters from array2 into the  same  array skipping one space, and starting from index 1


    for letter in msg2:
        decrypted += letter# adding the letters from  the array with decrypted message to the decrypted string

    print( 'The decrypted message  is: '+ decrypted)


decrypt()









