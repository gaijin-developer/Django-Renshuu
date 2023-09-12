def sum_numbers(name):
    return f"hello "+name

    
def checker(number):
    if(number>100):
        return "greater than 100"
    else:
        return "less than 100"
    
#result = checker(103) 
#print(result)
def calculator(a,b,operator):
    if(operator == "+"):
        return a + b
    else:
        return a - b

result = calculator(7,3,"-")
print(result)