def binary_treshhold(result):
    if result<2:
        return 1
    else:
        return 0
    
#x-input
#w-weight
#b-bias
def perceptron(x,w,b) :
    temp=x*w+b
    return binary_treshhold(temp)

def NOTgate(x):
    w=1
    b=1
    return perceptron(x,w,b)

example1=0
example2=1

print("NOT[0]=",NOTgate(example1))
print("NOT[1]=",NOTgate(example2))

