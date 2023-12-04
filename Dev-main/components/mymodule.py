def add(a,b): 
    """ Function which add a to b
     a, b : numbers
     return a+b
       """
    if isinstance(a,int) or isinstance(a,float) or isinstance(b,int)or isinstance(b,float):
        return a+b 
    else :
        return False
    

def mul(a,b): 
    """ Function which makes the product a times b
     a, b : numbers
     return a*b
       """
    if isinstance(a,int) or isinstance(a,float) or isinstance(b,int)or isinstance(b,float):
        return a*b 
    else :
        return False    



if __name__  == "__main__":
    print("addition: ", add(5,3))