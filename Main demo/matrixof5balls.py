import numpy as np
#import random
#from itertools import permutations, combinations
from scipy.special import comb
#three balls connected
def shoot3(matrix):
    count=0
    for i in range(5):
        if (matrix[i][0]+matrix[i][1]+matrix[i][2]==3 and matrix[i][3]==0) or (matrix[i][1]+matrix[i][2]+matrix[i][3]==3 and matrix[i][4]==matrix[i][0]==0) or (matrix[i][2]+matrix[i][3]+matrix[i][4]==3 and matrix[i][1]==0):
            count+=1
        if (matrix[0][i]+matrix[1][i]+matrix[2][i]==3 and matrix[3][i]==0) or (matrix[1][i]+matrix[2][i]+matrix[3][i]==3 and matrix[4][i]==matrix[0][i]==0) or (matrix[2][i]+matrix[3][i]+matrix[4][i]==3 and matrix[1][i]==0):
            count+=1
    if (matrix[0][0]+matrix[1][1]+matrix[2][2]==3 and matrix[3][3]==0) or (matrix[1][1]+matrix[2][2]+matrix[3][3]==3 and matrix[4][4]==matrix[0][0]==0) or (matrix[2][2]+matrix[3][3]+matrix[4][4]==3 and matrix[1][1]==0):
        count+=1
    if (matrix[0][4]+matrix[1][3]+matrix[2][2]==3 and matrix[3][3]==0) or (matrix[1][3]+matrix[2][2]+matrix[3][1]==3 and matrix[4][0]==matrix[0][4]==0) or (matrix[2][2]+matrix[3][1]+matrix[4][0]==3 and matrix[1][3]==0):
        count+=1        
    return count

#four balls connected
def shoot4(matrix):
    count=0
    for i in range(5):
        for j in range(2):
            if (matrix[i][0+j]+matrix[i][1+j]+matrix[i][2+j]+matrix[i][3+j]==4 and matrix[i][j-1]==0) or (matrix[0+j][i]+matrix[1+j][i]+matrix[2+j][i]+matrix[3+j][i]==4 and matrix[j-1][i]==0):
                   count+=1
            #if (matrix[0+j][i]+matrix[1+j][i]+matrix[2+j][i]+matrix[3+j][i]==4 and matrix[j-1][i]==0):
            #       count+=1
    for n in range(2):                   
        if (matrix[n+0][n+0]+matrix[n+1][n+1]+matrix[n+2][n+2]+matrix[n+3][n+3]==4 and matrix[n-1][n-1]==0) or (matrix[n+0][4-n]+matrix[n+1][3-n]+matrix[n+2][2-n]+matrix[n+3][1-n]==4 and matrix[n-1][0-n]==0):
            count+=1
        #if matrix[n+0][4-n]+matrix[n+1][3-n]+matrix[n+2][2-n]+matrix[n+3][1-n]==4 and matrix[n-1][0-n]==0:
        #    count+=1
    return count

#five balls connected
def shoot5(matrix):
    count=0
    for i in range(5):
        if (matrix[i][0]+matrix[i][1]+matrix[i][2]+matrix[i][3]+matrix[i][-1]==5) or (matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]+matrix[-1][i]==5):
            count+=1
        #if matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]+matrix[-1][i]==5:
        #    count+=1
    if (matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3]+matrix[-1][-1]==5) or (matrix[0][4]+matrix[1][3]+matrix[2][2]+matrix[3][1]+matrix[-1][0]==5):
            count+=1
    #if matrix[0][4]+matrix[1][3]+matrix[2][2]+matrix[3][1]+matrix[-1][0]==5:
    #        count+=1
    return count

count=[0,0,0]
grid=[0]*20+[1]*5


#https://stackoverflow.com/questions/6284396/permutations-with-unique-values

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1


branchcase=0
#brutal force method on getting results
print("direct result:", comb(25,5))
bundle = list(perm_unique([0]*20+[1]*5))
print("list length:", len(bundle))
for cp in bundle:
    present=np.reshape(cp,(5,5))
    #print(present)
    count[0]+=shoot3(present)
    count[1]+=shoot4(present)
    count[2]+=shoot5(present)

print(count)


'''
#statistical method on apprxomiating results
stat=5000
branchcase=0
for i in range(stat):
    np.random.shuffle(grid)    
    #print(grid)
    grid1=np.reshape(grid,(5,5)) 
    #print("before flip:")
    #print(grid1)
    #print(shoot3(grid2), shoot4(grid2), shoot5(grid2))
    #count[0]+=shoot3(grid1)
    for j in range(len(grid)):        
        if grid[j]==0:
            grid[j]=1
            grid2=np.reshape(grid,(5,5)) 
            #print("after flip:", "branchcase:", branchcase)
            #print(grid2)
            #print(shoot3(grid2), shoot4(grid2), shoot5(grid2))
            count[0]+=shoot3(grid2)
            count[1]+=shoot4(grid2)
            count[2]+=shoot5(grid2)
            branchcase+=1
            grid[j]=0
print("total branchcase:", branchcase, count)
percentage=[0]*3
for i in range(3):
    percentage[i]=count[i]/branchcase
print(percentage)
'''

#print(count)


#print(comb(25,5))


'''
#manual test 
grid1=[[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
grid1=np.reshape(grid1,(5,5))
print(grid1)

print("total: ", shoot3(grid1))
'''