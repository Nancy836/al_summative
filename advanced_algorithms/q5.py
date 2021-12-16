def shortestReach(n, edges, s):

    #collecting input for the number of nodes  and edges
    n,m = (input('Please enter the number of nodes,  leave  space then enter the number of edges: ')).split()n

    #collecting the  x,y,r  values m  times by looping through range  of m
    for x in range(m):
        x,y,r = (input('Please enter the beginning nodes,  leave  space then enter the ending nodes, leave  space then enter the length of the  edge: ')).split()

    s = (input('Please enter starting position: ')) #collecting the value of the  starting position

    shortest_path = {}#dictionary to store  the shortest paths to all the nodes  from the starting position





shortestReach(0,0,0)
