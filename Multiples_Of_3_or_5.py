def solution(number):
    totalSum=0
    sum=0
    for i in range(number):
        totalSum=totalSum+i
    for r in range(number):
        if(r%3!=0 and r%5!=0):
            sum=sum+r
    return (totalSum-sum)