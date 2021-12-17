def shortestReach(n,edges, s):
    shortest_path = {}  # dictionary to store  the shortest paths to all the nodes  from the starting position
    to_visit= {} #nodes to visit


    t = int(input('Please enter number of test cases: '))  # collecting the number of test cases
    while t < 1 or t > 10:
        print('Out of range')
        break

    # collecting input for the number of nodes  and edges
    n, m = (input('Please enter the number of nodes,  leave  space then enter the number of edges: ')).split()
    while n < 2 or n > 3000:  # adding constraints
        print('Out of range')
    while n < 2 or n > 3000:  # adding constraints
        print('Out of range')

    # collecting the  x,y,r  values m  times by looping through range  of m
    for x in range(m):
        x, y, r = (input(
            'Please enter the beginning nodes,  leave  space then enter the ending nodes, leave  space then enter the length of the  edge: ')).split()
        while r < 1 or n > 10 ** 5 or x < 1 or y < 1 or x > float('inf') or y > float('inf'):  # adding constraints
            print('Out of range')

    s = (input('Please enter starting position: '))  # collecting the value of the  starting position

    while s < 1 or s > float('inf'):
        print('Out of range')

    shortest_path[s]  = 0 # setting the distance from the source to itself to 0
    for node in x:
        if node != s:
            shortest_path[node]  = float('inf')
        to_visit.append(node)# inserting node to the list of  nodes  to visit

    while to_visit: #while  there are  still nodes that haven't been visited
        nearest_node = None

        for node in to_visit:
            if shortest_path[nearest_node] > shortest_path[node]: # if  the shortest path of the nearest node is greater than that of the current node,  the current node  becomes the nearest node
                node =  nearest_node
            elif nearest_node == None:
                node = nearest_node

        possible_paths = to_visit[nearest_node].items() # the  possible paths are those that  the node is adjacent to which are in  the to_visit dictionary
        

        while r and y in possible_paths:
            if  shortest_path[y] > shortest_path[nearest_node] + r:#if shortest path to the next node is greater than that of the. nearest node
                shortest_path[y] = shortest_path[nearest_node] + r # shortest path to the next_node will then be that of. the. nearest node

        to_visit.pop(nearest_node) # removing nearest node from the nodes left to visit

        print(shortest_path)

shortestReach(0,0,0)
