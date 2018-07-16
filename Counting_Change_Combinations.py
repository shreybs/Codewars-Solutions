#This program needs to be solved with a dynamic programming approach, to 
#learn the algorithm, visit https://www.youtube.com/watch?v=jaNZ83Q3QGc ( I don't own this vid)

def count_change(money, coins):
    combinations=[1]+[0]*money
    for coins in coins:
        for i in range(coins,money+1):
            combinations[i] += combinations[i-coins]
    return combinations[money]



            

    

    
            
