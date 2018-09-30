import numpy as np
#import random
#from itertools import permutations, combinations


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
    if (matrix[0][4]+matrix[1][3]+matrix[2][2]==3 and matrix[3][1]==0) or (matrix[1][3]+matrix[2][2]+matrix[3][1]==3 and matrix[4][0]==matrix[0][4]==0) or (matrix[2][2]+matrix[3][1]+matrix[4][0]==3 and matrix[1][3]==0):
        count+=1        
    return count
#four balls connected
def shoot4(matrix):
    count=0
    for i in range(5):
        for j in range(2):
            if (matrix[i][0+j]+matrix[i][1+j]+matrix[i][2+j]+matrix[i][3+j]==4 and matrix[i][j-1]==0) or (matrix[0+j][i]+matrix[1+j][i]+matrix[2+j][i]+matrix[3+j][i]==4 and matrix[j-1][i]==0):
                   count+=1
    for n in range(2):                   
        if (matrix[n+0][n+0]+matrix[n+1][n+1]+matrix[n+2][n+2]+matrix[n+3][n+3]==4 and matrix[n-1][n-1]==0) or (matrix[n+0][4-n]+matrix[n+1][3-n]+matrix[n+2][2-n]+matrix[n+3][1-n]==4 and matrix[n-1][0-n]==0):
            count+=1
    return count

#five balls connected
def shoot5(matrix):
    count=0
    for i in range(5):
        if (matrix[i][0]+matrix[i][1]+matrix[i][2]+matrix[i][3]+matrix[i][4]==5) or (matrix[0][i]+matrix[1][i]+matrix[2][i]+matrix[3][i]+matrix[4][i]==5):
            count+=1
    if (matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3]+matrix[4][4]==5) or (matrix[0][4]+matrix[1][3]+matrix[2][2]+matrix[3][1]+matrix[4][0]==5):
            count+=1
    return count





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
#print("direct result:", comb(25,5))
bundle = list(perm_unique([0]*20+[1]*5))
#print("list length:", len(bundle))
timer=0

base=[0,0,0]
branch=[0,0,0]
difference=[]
for cp in bundle:
    count=[0,0,0]
    component=list(cp)
    case=np.reshape(component,(5,5))
    count[0]=shoot3(case)
    count[1]=shoot4(case)
    count[2]=shoot5(case)
    base[0]+=shoot3(case)
    base[1]+=shoot4(case)
    base[2]+=shoot5(case)
    
    #enter into branches
    for j in range(25):
        branchcount=[0,0,0]
        #branchlist=list(cp)
        if cp[j]==0:   
            #print(cp)
            branchcomponent=list(cp)
            branchcomponent[j]=1
            #print(branchcomponent)
            branchcase=np.reshape(branchcomponent,(5,5)) 
            #print("after flip:")
            #print(branchcase)
            branchcount[0]=shoot3(branchcase)
            branchcount[1]=shoot4(branchcase)
            branchcount[2]=shoot5(branchcase)
            branch[0]+=shoot3(branchcase)
            branch[1]+=shoot4(branchcase)
            branch[2]+=shoot5(branchcase)
      
        #diff=[0,0,0]

            if branchcount!=count:
                diff=[branchcount[0]-count[0],branchcount[1]-count[1],branchcount[2]-count[2]]
                #print("------")
                #print(branchcount)
                #print(count)
                #print("------")
                if diff not in difference:
                    difference.append(diff)
                '''
                #manual search particular change 
                if count==[0,0,0] and diff==[1, 0, 0]:
                    print("------")
                    #print(count)
                    print(case)
                    #print(branchcount)
                    print(branchcase)
                    print("------")
                    break
                '''
            branchcomponent[j]=0

    timer+=1
    if timer in range(0,1000000, 10000):
        print("still going!")        
            #print("branch count:", branchcount)
            #if count==[0]*3 and branchcount[0]!=0 and branchcount[1]==branchcount[2]==0: #nothing to some shoot3 no others

#print(difference)
print("base", base)
print("branch", branch)

            



'''
#statistical method on apprxomiating results
grid=[0]*20+[1]*5
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



'''
#manual test 
grid1=[[1,1,1,1,1],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
grid1=np.reshape(grid1,(5,5))
print(grid1)

print("total: ", shoot5(grid1))
'''