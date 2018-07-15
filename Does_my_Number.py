def narcissistic( value ):
    sum=0
    digitList=[int(d) for d in str(value)]
    power = len(digitList)
    for i in range(len(digitList)):
        sum=sum+digitList[i] ** power
    if(sum==value): return True
    else: return False
    
    