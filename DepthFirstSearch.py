tree = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]
        }
start = input("Enter the start node : ")

def dfs_goalsearch(tree):
    goal = input("Enter Goal Node : ")
    visited=[]
    stack = [[start]]        #list of list for best possible path
    if start==goal:
        print("Start is the Goal node")
        return start
    while stack:
        path = stack.pop()          #path is the variable that is taking a path from list of list
        node = path[-1]             #poping last element in stack
        if node not in visited:
            visited.append(node)
            neigbour=tree[node]
            for i in neigbour:
                new_path=list(path)         #creating a list using list() constructor
                new_path.append(i)
                stack.append(new_path)
                if i==goal:
                    return new_path
  
def dfs_traversal(tree):
    visited = []
    stack = [start]                 # stack has [A]
    while stack :                   # while stack is nnot empty
        node=stack.pop()           #poping the first element in stack
        if node not in visited :
            visited.append(node)    #adding the node which has been visited
            neighbour=tree[node]    #taking the childern/neigbours of node variable and putting in variable neigbour 
            for i in neighbour :
                stack.append(i)     #putting the neigbours in the stack 
    return visited

print("Path is ",dfs_goalsearch(tree))
print("Traversal is ",dfs_traversal(tree))



