import numpy  as np

def binary_treshhold(result):
    if result<2:
        return 1
    else:
        return 0
    
#x-input
#w-weight
#b-bias
def perceptron(x,w,b) :
    temp=x.dot(w)+b
    return binary_treshhold(temp)

def NORgate(x):
    w=np.array([1,1])
    b=1
    return perceptron(x,w,b)

example1=np.array([0,0])
example2=np.array([0,1])
example3=np.array([1,0])
example4=np.array([1,1])

print("NOR[0,0]=",NORgate(example1))
print("NOR[0,1]=",NORgate(example2))
print("NOR[1,0]=",NORgate(example3))
print("NOR[1,1]=",NORgate(example4))

