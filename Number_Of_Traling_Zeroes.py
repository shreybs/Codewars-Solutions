def zeros(n):
    zeroCount=0
    i=5
    while(n/i >= 1 ):
        zeroCount=zeroCount+ n/i
        i=i*5
    return int(zeroCount)