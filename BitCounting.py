count=0
def countBits(n):
    global count
    count=0
    global binaryString
    binaryString=format(n, "b")
    for i in range(len(binaryString)):
        if binaryString[i]=='1':
            count += 1
    return count