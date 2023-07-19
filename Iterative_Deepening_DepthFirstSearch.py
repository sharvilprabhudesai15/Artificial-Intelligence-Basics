tree ={ 'A':['B','C'],
       'B':['D','E'],
       'C':['F','G'],
       'D':[], 'E':[],'F':[],'G':[]
       }
start=input("enter start node:")
goal=input("enter goal node:")
max_depth=int(input("enter max depth:"))

path=[]

level=0;
def iterative_dfs(start,goal,path,level,max_depth):
    print("Current level is ",level)
    path.append(start)
    if start==goal:
        print("Goal node is found")
        return path
    
    if level==max_depth:
        return False 
    print("Expanding current node :",start)
    
    neighbour=tree[start]
    for i in neighbour :
        if iterative_dfs(i, goal, path, level+1, i):
            return path
        print(path.pop())
        
    return False


for i in range(max_depth+1):
	path=[]
	result=iterative_dfs(start, goal, path, level, max_depth)
	if result:
		print("Goal node is present within the limit ");
		print(path)
		break
	else :
		print("Goal node is not present within the max limit ")    
      
