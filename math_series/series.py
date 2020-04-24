def fibonacci(num):
    if(num == 0):
        return 0

    if(num == 1):
        return 1    

    if(num>1):
        return fibonacci(num-1) + fibonacci(num-2)
    
def lucas(no):
    #print("lucas")
    if(no == 0):
        return 2

    if(no == 1):
        return 1    
    
    if(no>1):
        return lucas(no-1) + lucas(no-2)

def sum_series(num,val1 = 0,val2 = 1):
    if(val1==0 and val2==1):
        return fibonacci(num)
    elif(val1 == 2 and val2==1):
        return lucas(num)

    

