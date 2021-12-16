def shortestReach(n, edges, s):

    t = (input('Please enter number of test cases: '))  # collecting the number of test cases
    while t <1 or t>10 :
        print('Out of range')
        break


    #collecting input for the number of nodes  and edges
    n,m = (input('Please enter the number of nodes,  leave  space then enter the number of edges: ')).split()
    while n <2or n>3000 :# adding constraints
        print('Out of range')
    while n <2or n>3000 :# adding constraints
        print('Out of range')

    #collecting the  x,y,r  values m  times by looping through range  of m
    for x in range(m):
        x,y,r = (input('Please enter the beginning nodes,  leave  space then enter the ending nodes, leave  space then enter the length of the  edge: ')).split()
        while r < 1 or n > 10**5 or x < 1 or y<1 or x> float('inf') or y > float('inf'):# adding constraints
            print('Out of range')


    s = (input('Please enter starting position: ')) #collecting the value of the  starting position

    while s <1or s> float('inf') :
        print('Out of range')

    shortest_path = {}#dictionary to store  the shortest paths to all the nodes  from the starting position







shortestReach(0,0,0)
