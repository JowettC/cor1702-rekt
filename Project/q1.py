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
    
    decision_list = []
    
    decision_list.append(greedy_algo(W, packages))
    
    decision_list.append(stingy_algo(W, packages))
       
    if (decision_list[0][1] > decision_list[1][1]):
        return(decision_list[0][0])
        
    elif (decision_list[0][1] == decision_list[1][1]):
        return(decision_list[0][0])
    
    else:
        return(decision_list[1][0])
    
def greedy_algo(W, packages):
    value_list = []
    tabulate_weight = 0
    selected_list =[]
    total_value = 0
    last_weight = 0
    last_value = 0.00
    
    for i in range(len(packages)):
        value = packages[i][1] / packages[i][2]
        value_list.append([packages[i][0],packages[i][1],packages[i][2],value])
        
    value_list.sort(key=lambda x:x[3],reverse=True)
    
    j = 0
    
    while tabulate_weight < W:
        selected_list.append(value_list[j][0])
        #selected_list.append(value_list[j])
        total_value += value_list[j][1]
        tabulate_weight += value_list[j][2]
        lastweight = value_list[j][2]
        lastvalue = value_list[j][1]
        
        j += 1
        
    del selected_list[-1]
    total_value -= lastvalue
    tabulate_weight -= lastweight
    
    return(selected_list,total_value,tabulate_weight)
    
def stingy_algo(W, packages):
    total_value = 0.00
    total_reward = 0
    selection_list = []
    current_weight = 0
    tabulate_value = 0
    
    for i in range(len(packages)):
        value = packages[i][1] / packages[i][2]
        packages[i].append(value)
        total_value += value
        total_reward += packages[i][1]
        
    avg_value = total_value / len(packages)
    avg_reward = total_reward / len(packages)
    
    packages.sort(key=lambda x:x[2])
    
    for j in range(len(packages)):
        if (packages[j][1] >= avg_reward and packages[j][3] >= avg_value and (packages[j][2] + current_weight <= W)):
            current_weight += packages[j][2]
            #selection_list.append(packages[j])
            selection_list.append(packages[j][0])
            tabulate_value += packages[j][1]
            
    packages.sort(key=lambda x:x[3],reverse=True)    
    
    for k in range(len(packages)):
        if ((packages[k][0] not in selection_list) and (packages[k][2] + current_weight <= W)):
            current_weight += packages[k][2]
            selection_list.append(packages[k][0])
            tabulate_value += packages[k][1]
                 
    return (selection_list, tabulate_value, current_weight)
    
# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.