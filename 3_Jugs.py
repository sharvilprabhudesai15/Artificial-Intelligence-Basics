x=int(input("Enter the capacity of jug A:::"))
y=int(input("Enter the capacity of jug B:::"))
z=int(input("Enter the capacity of jug C:::"))

goalA=int(input("Enter the goal state of jug A:::"))
goalB=int(input("Enter the goal state of jug B:::"))

initial_state=(8,0,0)
visited={}     #all visited
path=[]       #To store entire path 


def waterJugState(state):
    a=state[0]
    b=state[1]
    c=state[2]
    if(a==goalA and b==goalB):
        path.append(state)
        return True
    if((a,b,c) in visited):
        return False
    visited[(a,b,c)]=1

    if(a>0):
        if(a+b<=y):
            if(waterJugState((0,a+b,c))):
                path.append(state)
                return True
        else:
            if(waterJugState((a-(y-b),y,c))):
                path.append(state)
                return True
        if(a+c<=z):
            if(waterJugState((0,b,a+c))):
                path.append(state)
                return True
            else:
                if(waterJugState((a-(z-c),b,z))):
                   path.append(state)
                   return True
    if(b>0):
          if(b+a<=x):
              if(waterJugState((a+b,0,c))):
                  path.append(state)
                  return True
          else:
                  if(waterJugState((x,b-(x-a),c))):
                      path.append(state)
                      return True
          if(b+c<=z):
              if(waterJugState((a,0,b+c))):
                  path.append(state)
                  return True
          else:
                  if(waterJugState((a,b-(z-c),z))):
                     path.append(state)
                     return True    
    if(c>0):
           if(c+a<=x):
               if(waterJugState((a+c,b,0))):
                   path.append(state)
                   return True
           else:
                   if((waterJugState(x,b,c-(x-a)))):
                       path.append(state)
                       return True
           if(c+b<=y):
               if(waterJugState((a,b+c,0))):
                   path.append(state)
                   return True
           else:
                   if(waterJugState((a,y,c-(y-b)))):
                      path.append(state)
                      return True    
        
    return False
    
waterJugState(initial_state)

print("path is")
print(" A  B  C")

path.reverse()    
for i in path:
    print(i)    
                   



