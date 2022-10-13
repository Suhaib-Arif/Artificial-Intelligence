#The tree is stored as a dictionary
#Dictionary consists of Keys:Values pair
#The Parent node is stored as key and the child nodes are stored in an list(array) as values
#The sibling nodes are present in the same list
tree = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
#                        5
#                      /   \
#                     3     7
#                    /  \    \ 
#                   2    4 ---8
#                                      

#BFS uses Queue data structure, a list is created called queue
queue=[]
#Another list is created to store the nodes already visited
visited=[]
def bfs(queue,visited,node):
    """
    doc strings are cool
    """
    #append() is a built_in function to add the an element to the list
    #the value of the current node is inserted into the visited and queue list
    visited.append(node)
    queue.append(node)
    #Traversing until the queue is empty
    while queue:
        #In queue the data is removed from the front
        #The value at the 0th index location(front) of queue is removed and stored inside a variable
        m=queue.pop(0)
        print(m)
        #Printing the below statements might give more clarity
        # print("queue",queue)
        # print("visited",visited)

        #Traversing the child nodes of the parent nodes dequeued from the queue OR Traversing the list/arrays of the keys 
        for neighbour in tree[m]:
            #If the nodes are not already visited, enqueue them into the queue
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        
print("The Following is breath first search")
bfs(queue,visited,'5')
