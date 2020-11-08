# G7-T22
# BENJAMIN CHEW PIN HSIEN
# NICHOLAS CHEN HAN WEI

# Q1

# Replace the content of this function with your own algorithm
# inputs: 
#   W: weight limit of the vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   1D list of package IDs to represent a package selection. e.g. ["P001", "P003, "P010]

def select_packageSet(W, packages):
    
    val = []
    wt = []
    package = []
    package_select = []
    
    for i in range(len(packages)):
        val.append(packages[i][1])
        wt.append(packages[i][2])
        package.append(packages[i][0])
        
    n = len(val)
    
    selected_wt_index = knapSack(W, wt, val, n)
    
    for wt_index in selected_wt_index:
        package_select.append(package[wt_index])
        
    return(package_select)
    

def knapSack(W, wt, val, n): 

    selected_weight = []
    
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    #print(K)

    #return K[n][W]
    while K[n][W] != 0:
        if K[n][W] != K[n-1][W]:
            selected_weight.append(n-1)
            W -= wt[n-1]
        n -= 1
        
    return selected_weight
    
# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.