import random as rd
import matplotlib.pyplot as plt
import math
#line = plt.figure(num=None, figsize=(8,6),dpi=80, facecolor='w', edgecolor='k')

stat=1 #有多少1000局 (cycle)

for w in range(stat):
    count1=0 #玩家破產次數
    result=[] #每局最後玩家結果
    time=1000 #執行多少局
    
    high=[]
    withdraw=2000
    leftwith=[]
    savingshistory=[]

    for j in range(time):
        #house=100000000 #莊家的資本
        player=1000 #玩家的資本
        basebethistory=[]
        history=[]
        bethistory=[]
        househistory=[]
        flip=[0,0,0,0]
        rate=1.98 #賠率，1/2機率中獎，莊家抽1%                  
        n=500
        
        savings=0
        #玩家進場投擲N次硬幣，這樣是一局
        for i in range(n):
                #丟硬幣
                flip[0]=flip[1]
                flip[1]=flip[2]
                flip[2]=flip[3]
                flip[3]=rd.randint(0,1)
                #print(flip)
                if player<=2000:
                    basebet=100
                elif player>2000:
                    basebet=200                   
                #basebethistory.append(basebet)
                #玩家歷史金額
                history.append(player)
                #househistory.append(house)
                #玩家還沒破產，就再投一次
                #if i==182:                        
                #    flag=max(history)
                #    print(i, flag)
                if len(bethistory)==0:
                    player=player+basebet*(rate*flip[3]-1)
                    bethistory.append(basebet)
                    #if player> flag:
                    #    print("leave")
                    #    break
                    #if player>withdraw:                    
                    #    savings+=(player-1000)
                    #    player=1000
                elif player>bethistory[-1]*1.975 and flip[2]==1 and len(bethistory)!=0 and player<=withdraw:
                    if flip[0]==1 and flip[1]==1:
                        player=player+basebet*(rate*flip[3]-1)
                        bethistory.append(basebet)
                    else:
                        player=player+bethistory[-1]*1.975*(rate*flip[3]-1)
                        bethistory.append(bethistory[-1]*1.975)
                    #if player> flag:
                    #    print("leave")
                    #    break
                        #if player>leave:
                    #    savings+=(player-1000)
                    #    player=1000
                elif player>basebet and flip[2]==0 and player<=withdraw:
                    player=player+basebet*(rate*flip[3]-1)
                    bethistory.append(basebet)
                    #if player> flag:
                    #    print("leave")
                    #    break
                        #if player>leave:
                    #    savings+=(player-1000)
                    #    player=1000
                #玩家破產，結束
                elif player<basebet or (player<bethistory[-1]*1.975 and flip[2]==1 and len(bethistory)!=0 and player<=withdraw):
                    count1+=1
                    break
                
                elif player>withdraw:
                    savings+=math.floor(player*1/3)                    
                    player=player-math.floor(player*1/3)

				#莊家破產，結束
                #if house<0:
                    #break
                
        #print(len(history))
        savingshistory.append(savings)
        leftwith.append((savingshistory[-1]+player))
    #result.append(count1)
    #history.append(player)
    #househistory.append(house)    
    #print(bethistory, player, max(bethistory))
    #print(history)
    #玩家破產次數
    #high.append(max(history))
    #print(max(history))
    #print(count1)
#print(history)
    #print(leftwith, savingshistory, history)
    
'''
    intervalcount=[0]*12
    intervalpercentage=[0]*12

    for s in range(len(leftwith)):
        if leftwith[s]<1000:
            intervalcount[0]+=1
        elif leftwith[s]<2000 and leftwith[s]>=1000:
            intervalcount[1]+=1
        elif leftwith[s]<3000 and leftwith[s]>=2000:
            intervalcount[2]+=1
        elif leftwith[s]<4000 and leftwith[s]>=3000:
            intervalcount[3]+=1
        elif leftwith[s]<5000 and leftwith[s]>=4000:
            intervalcount[4]+=1
        elif leftwith[s]<6000 and leftwith[s]>=5000:
            intervalcount[5]+=1
        elif leftwith[s]<7000 and leftwith[s]>=6000:
            intervalcount[6]+=1
        elif leftwith[s]<8000 and leftwith[s]>=7000:
            intervalcount[7]+=1
        elif leftwith[s]<9000 and leftwith[s]>=8000:
            intervalcount[8]+=1
        elif leftwith[s]<10000 and leftwith[s]>=9000:
            intervalcount[9]+=1
        elif leftwith[s]<11000 and leftwith[s]>=10000:
            intervalcount[10]+=1
        elif leftwith[s]<20000 and leftwith[s]>=10000:
            intervalcount[11]+=1
    
    
    for w in range(12):
        intervalpercentage[w]=intervalcount[w]/time
        
    print(intervalcount, intervalpercentage)

'''
#print(savingshistory[-1])

line = plt.figure(num=None, figsize=(8,6),dpi=80, facecolor='w', edgecolor='k')
x1=[r+1 for r in range(len(history))]
y1=[history[s] for s in range(len(history))]
plt.bar(x1,y1, color="royalblue")


#print("Money left and savings:", savingshistory[-1]+player, leftwith[-1])

#print(leftwith)



        
#print(basebethistory)



'''
total=[]
for i in range(len(leftwith)):
    total.append(leftwith[i] + savingshistory[i])
#print("left total", total)

ave=0
for m in total:
    ave+=m
print("ave", ave/len(total))    
'''    

'''
#玩家平均每一局存活下來剩餘的錢
total=0
for m in result:
    total=total+m
    
print("ave", total/stat)
'''

'''
total=0
for m in high:
    total=total+m
    
print("ave", total/stat)
'''