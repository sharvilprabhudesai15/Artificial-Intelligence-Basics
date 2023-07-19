jugA=int(input("Enter the capacity of jug A:::"))
jugB=int(input("Enter the capacity of jug B:::"))
jugAi=int(input("Enter the initial state of jug A:::"))
jugBi=int(input("Entere the initial state of jug B:::"))
jugAf=int(input("Enter the Final state of jug A:::"))

print("Operation 1:Fill the Jug A completely")
print("Operation 2:Fill the Jug B completely")
print("Operation 3:Empty the Jug A compltely on ground")
print("Operation 4:Empty the Jug B compltely on ground ")
print("Operation 5:Pour the water from Jug A to Jug B completely or until Jug A becomes empty")
print("Operation 6:Pour the water from Jug B to Jug A completely or until Jug B becomes empty ")
print("Operation 7:Pour all the water from Jug B to Jug A ")
print("Operation 8:Pour all the water from Jug A to Jug B ")

while(jugAi!=jugAf):
   op=int(input("Enter the Operation Number:::"))
   if op==1:
        jugAi=jugA
   if op==2:
        jugBi=jugB
   if op==3 :
        jugAi=0;
   if op==4:
        jugBi=0
   if op==5:
        if jugB-jugBi >jugAi :
            jugBi=jugBi+jugAi
            jugAi=0
        else:
            
            jugAi=jugAi-(jugB-jugBi)
            jugBi=jugB
   if op==6:
         if jugA-jugAi >jugBi :
             jugAi=jugAi+jugBi
             jugBi=0
         else:
             
             jugBi=jugBi-(jugA-jugAi)
             jugAi=jugA
   if op==7:
          jugAi=jugAi+jugBi
          jugBi=0
   if op==8:
          jugBi=jugBi+jugAi
          jugAi=0

            
   print(jugAi,"    ",jugBi)
    
