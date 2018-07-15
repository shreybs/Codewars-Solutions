def longest_slide_down(pyramid):
    pyramid.reverse()
    
    for i in range(1,len(pyramid)):
        slideSum=[]
        for j in range(len(pyramid[i])):
            slideSum.append(max(pyramid[i][j]+pyramid[i-1][j],
            pyramid[i][j]+pyramid[i-1][j+1]))
        pyramid[i] = slideSum
    return pyramid[-1][0]