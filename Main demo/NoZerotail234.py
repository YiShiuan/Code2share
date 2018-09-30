from math import floor
set0= [i+1 for i in range(49)]

count2=0 #N0二連尾
count3=0 #N0三連尾
count4=0 #N0四連尾

from itertools import combinations
for m in combinations(set0, 7):

    a1=floor(m[0]/10) #head1
    b1=m[0]-a1*10 # tail1
    a2=floor(m[1]/10) #head2
    b2=m[1]-a2*10 # tail2
    a3=floor(m[2]/10) #head3
    b3=m[2]-a3*10 # tail3
    a4=floor(m[3]/10) #head4
    b4=m[3]-a4*10 # tail4
    a5=floor(m[4]/10) #head5
    b5=m[4]-a5*10 # tail5
    a6=floor(m[5]/10) #head6
    b6=m[5]-a6*10 # tail6
    a7=floor(m[6]/10) #head7
    b7=m[6]-a7*10 # tail7
    b=[b1,b2,b3,b4,b5,b6,b7]
    for n in combinations(b,2):
        for w in combinations([1,2],2):            
            if n==w:
                print(n,w, "a match!")
                count2 +=1
                print(m, "不含零二連尾目前總數=", count2)
    for p in combinations(b,3):
        for x in combinations([1,2,3],3):            
            if p==x:
                print(p,x, "a match!")
                count3 +=1
                print(m, "不含零三連尾目前總數=", count3)
    for q in combinations(b,4):
        for y in combinations([1,2,3,4],4):            
            if q==y:
                print(q,y, "a match!")
                count4 +=1
                print(m, "不含零四連尾目前總數=", count4)

print("不含零二三四連尾總數", count2, count3, count4)
        

            

#print("0--二三四連尾總個數=", count2, count3, count4)
#print("1--二三四連尾總個數=", count5, count6, count7)