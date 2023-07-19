import numpy  as np
def binary_treshhold(result):
    if result>1:
        return 1
    else:
        return 0
    
#x-input
#w-weight
#b-bias
def perceptron(x,w,b) :
    temp=x.dot(w)+b
    return binary_treshhold(temp)

def ORgate(x):
    w=np.array([1,1,1])
    b=1
    return perceptron(x,w,b)

example1=np.array([0,0,0])
example2=np.array([0,0,1])
example3=np.array([0,1,0])
example4=np.array([0,1,1])
example5=np.array([1,0,0])
example6=np.array([1,0,1])
example7=np.array([1,1,0])
example8=np.array([1,1,1])

print("OR[0,0,0]=",ORgate(example1))
print("OR[0,0,1]=",ORgate(example2))
print("OR[0,1,0]=",ORgate(example3))
print("OR[0,1,1]=",ORgate(example4))
print("OR[1,0,0]=",ORgate(example5))
print("OR[1,0,1]=",ORgate(example6))
print("OR[1,1,0]=",ORgate(example7))
print("OR[1,1,1]=",ORgate(example8))
