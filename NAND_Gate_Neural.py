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

def NANDgate(x):
    w=np.array([1,1])
    b=0.5
    return perceptron(x,w,b)

example1=np.array([0,0])
example2=np.array([0,1])
example3=np.array([1,0])
example4=np.array([1,1])

print("NAND[0,0]=",NANDgate(example1))
print("NAND[0,1]=",NANDgate(example2))
print("NAND[1,0]=",NANDgate(example3))
print("NAND[1,1]=",NANDgate(example4))

