#Product and Sum

#What is the run time of the below code ?

def foo(array):
    sum = 0     #-----------------------------------O(1)
    product = 1     #-----------------------------------O(1)

    for i in array:     #-----------------------------------O(n)
        sum += 1        #-----------------------------------O(1)

    for i in array:     #-----------------------------------O(n)
        product *= i    #-----------------------------------O(1)
    
    print(f'sum = {sum}, product = {product}')  #-----------------------------------O(1)

foo([1,2,3,4,5])

#Time complexity = O(N)