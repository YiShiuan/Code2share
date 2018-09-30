import random as rd
import math
import matplotlib.pyplot as plt


'''
a=[rd.randint(0,9) for x in range(5)]

x0, y0 = [0, 9], [0, 0]
x00, y00 = [0, 0], [0, 9]
x1,y1 = [a[0],a[1]], [a[1],a[2]]
x2,y2 = [a[1],a[2]], [a[2],a[3]]
x3,y3 = [a[2],a[3]], [a[3],a[4]]
x4,y4 = [a[3],a[4]], [a[4],a[0]]
#x5,y5 = [a[4],a[0]], [a[0],a[1]]

plt.plot(x0, y0, x00, y00, color='black')
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, marker = '.')


plt.show()
'''


'''
#走田埂
a=[rd.randint(0,9) for x in range(5)]
x0, y0 = [-9, 9], [0, 0]
x00, y00 = [0, 0], [-9, 9]
x1,y1 = [0, a[0]], [0, 0]
x2,y2 = [a[0], a[0]], [0,a[1]]
x3,y3 = [a[0], a[0]-a[2]], [a[1],a[1]]
x4,y4 = [a[0]-a[2], a[0]-a[2]], [a[1],a[1]-a[3]]
#x5,y5 = [a[0]-a[2], a[0]-a[2]+a[4]], [a[1]-a[3], a[1]-a[3]]
#x6,y6 = [a[0]-a[2]+a[4], ], [a[1]-a[3], ]
#x7,y7 = 
#x8,y8 =
#x9,y9 =
plt.plot(x0, y0, x00, y00, color='black')
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, marker = '.')


plt.show()
print(a)
'''


'''
count=[0]*7
count1=[0]*7
for s1 in range(10):
    for s2 in range(10):
        for s3 in range(10):
            for s4 in range(10):
                for s5 in range(10):
                    location=[s1-s3+s5, s2-s4]
                    #x0, y0 = [-9, 9], [0, 0]
                    #x00, y00 = [0, 0], [-9, 9]
                    #x1,y1 = [0, s1], [0, 0]
                    #x2,y2 = [s1,s1], [0,s2]
                    #x3,y3 = [s1,s1-s3], [s2,s2]
                    #x4,y4 = [s1-s3,s1-s3], [s2,s2-s4]                    
                    #plt.plot(x0, y0, x00, y00, x1, y1, x2, y2, x3, y3, x4, y4, marker = '.')
                    #plt.show()
                    if location[0]>0 and location[1]>0:
                        count[0]+=1
                    if location[0]<0 and location[1]>0:
                        count[1]+=1
                    if location[0]<0 and location[1]<0:
                        count[2]+=1
                    if location[0]>0 and location[1]<0:
                        count[3]+=1
                    if location[0]!=0 and location[1]==0:
                        count[4]+=1
                    if location[0]==0 and location[1]!=0:
                        count[5]+=1
                    if location[0]==0 and location[1]==0:
                        count[6]+=1
print(count)
for i in range(len(count)):
    count1[i]=count[i]/100000
    count[i]=100000/count[i]
print(count1, count)
'''


                    
'''
                    if s5 is (0,2,4,6,8):
                        location=[s1-s3, s2-s4]
                        x, y = [0, location[0]], [0, location[1]
                        #plt.plot(x0, y0, x00, y00, x, y, marker = '.')
                        #plt.show()

                    if s5 is (1,3,5,7,9):
                        location=[s2-s4, s1-s3]
                        x, y = [0, location[0]], [0, location[1]
                        #plt.plot(x0, y0, x00, y00,x,y, marker = '.')
                        #plt.show()
'''



#鬥地主
#farm=np.zeros((10,10))
a=[rd.randint(0,9) for x in range(4)]
x1,y1 = [a[0], 9], [0, a[1]]
x2,y2 = [9, a[2]], [a[1] , 9]
x3,y3 = [a[2], 0], [9, a[3]]
x4,y4 = [0, a[0]], [a[3], 0]
plt.plot( x1, y1, x2, y2, x3, y3, x4, y4, marker = '.')
plt.fill_between(x1, y1, facecolor='gold')
plt.fill_between(x2, y2, 9, facecolor='gold')
plt.fill_between(x3, 9, y3, facecolor='gold')
plt.fill_between(x4, y4, facecolor='gold')
plt.show()
eacharea=[1/2*(9-a[0])*a[1], 1/2*(9-a[1])*(9-a[2]), 1/2*a[2]*(9-a[3]), 1/2*a[0]*a[3]]
sumarea=1/2*(9-a[0])*a[1]+1/2*(9-a[1])*(9-a[2])+1/2*a[2]*(9-a[3])+1/2*a[0]*a[3]
landlord=81-(1/2*(9-a[0])*a[1]+1/2*(9-a[1])*(9-a[2])+1/2*a[2]*(9-a[3])+1/2*a[0]*a[3])
print("農夫", eacharea, sumarea, "地主", landlord)



'''
count=0
for s1 in range(10):
    for s2 in range(10):
        for s3 in range(10):
            for s4 in range(10):                
                eacharea=[1/2*(9-s1)*s2, 1/2*(9-s3)*(9-s2), 1/2*s3*(9-s4), 1/2*s4*s1]
                sumarea=1/2*(9-s1)*s2+ 1/2*(9-s3)*(9-s2)+ 1/2*s3*(9-s4)+ 1/2*s4*s1
                landlord=81-sumarea
                print(landlord)
                #print( "個別面積",eacharea, "總農夫面積",sumarea, "地主面積", landlord)
                if eacharea[0]==eacharea[1]:
                    count+=1
print(count)
'''


'''
a=[rd.randint(1,6) for x in range(3)]

x01, y01 = [0,6], [0,0]
x1,y1 = [a[0], 6-a[1]*math.cos(60/180*math.pi)], [0, a[1]*math.sin(60/180*math.pi)]
x02, y02 = [6,3], [0, 6*math.sin(60/180*math.pi)]
x2,y2 = [6-a[1]*math.cos(60/180*math.pi), (6-a[2])*math.cos(60*math.pi/180)], [a[1]*math.sin(60/180*math.pi), (6-a[2])*math.sin(60*math.pi/180)]
x03, y03 = [3,0], [6*math.sin(60/180*math.pi),0]
x3,y3 = [a[0], (6-a[2])*math.cos(60*math.pi/180)], [0, (6-a[2])*math.sin(60*math.pi/180)]
plt.plot(x01, y01, x1, y1, x02, y02, x2, y2, x03, y03, x3, y3, marker = '.')
plt.show()

eacharea=[1/2*a[0]*(6-a[2])*math.sin(60/180*math.pi), 1/2*(6-a[0])*a[1]*math.sin(60/180*math.pi), 1/2*(6-a[1])*a[2]*math.sin(60/180*math.pi)]
totalarea = 36*math.sqrt(3)/4
farmersum=eacharea[0]+eacharea[1]+eacharea[2]
landlord=totalarea-eacharea[0]-eacharea[1]-eacharea[2]
print("農夫" ,farmersum, "地主",landlord)
'''


'''
count=0
totalarea=10.8253175473
for s1 in range(6):
    for s2 in range(6):
        #if s2!=s1:
            for s3 in range(6):
                #if s3!=s2 and s3!=s1:
                    eacharea=[1/2*s1*s2*math.sin(60/180*math.pi), 1/2*s2*s3*math.sin(60/180*math.pi), 1/2*s1*s3*math.sin(60/180*math.pi)]
                    farmersum= eacharea[0] +eacharea[1] +eacharea[2]
                    landlord=totalarea-farmersum
                    if farmersum>landlord:
                        count+=1
print(count/216)
'''






            


'''
a=[rd.randint(0,9) for x in range(5)]
side=9*math.sin(72/180*math.pi)/math.sin(54/180*math.pi)
trianglearea=0.5*side*9*math.sin(54/180*math.pi)
totalarea=trianglearea*5

eacharea=[1/2*a[0]*a[1]*math.sin(72/180*math.pi), 1/2*a[1]*a[2]*math.sin(72/180*math.pi), 1/2*a[2]*a[3]*math.sin(72/180*math.pi), 1/2*a[3]*a[4]*math.sin(72/180*math.pi), 1/2*a[4]*a[0]*math.sin(72/180*math.pi)]
farmer=[trianglearea-eacharea[0],trianglearea-eacharea[1],trianglearea-eacharea[2],trianglearea-eacharea[3],trianglearea-eacharea[4]]
landlord= eacharea[0]+eacharea[1]+eacharea[2]+eacharea[3]+eacharea[4]
farmersum=totalarea-landlord
print(farmer, farmersum, landlord)
x1,y1 = [0, side], [0, 0]
x2,y2 = [side, side+side*math.cos(72/180*math.pi)], [0, side*math.sin(72/180*math.pi)]
x3,y3 =[side+side*math.cos(72/180*math.pi), side+side*math.cos(72/180*math.pi)-side*math.cos(36/180*math.pi) ], [side*math.sin(72/180*math.pi), side*math.sin(72/180*math.pi)+side*math.sin(36/180*math.pi)]
x4,y4 = [-side*math.cos(72/180*math.pi), -side*math.cos(72/180*math.pi)+side*math.cos(36/180*math.pi)], [side*math.sin(72/180*math.pi), side*math.sin(72/180*math.pi)+side*math.sin(36/180*math.pi)]
x5,y5 = [0, -side*math.cos(72/180*math.pi)], [0, side*math.sin(72/180*math.pi)]

plt.plot( x1, y1, x2, y2,x3,y3,x4, y4, x5,y5, marker = '.')

plt.show()
'''
#print("農夫", eacharea, sumarea, "地主", landlord)


'''
trianglearea=0.5*9*9*math.sin(72/180*math.pi)
totalarea=trianglearea*5
count=0
for s1 in range(10):
    for s2 in range(10):
        for s3 in range(10):
            for s4 in range(10):
                for s5 in range(10):                
                    eacharea=[1/2*(s1+1)*(s2+1)*math.sin(72/180*math.pi),1/2*(s2+1)*(s3+1)*math.sin(72/180*math.pi),1/2*(s3+1)*(s4+1)*math.sin(72/180*math.pi),1/2*(s4+1)*(s5+1)*math.sin(72/180*math.pi), 1/2*(s5+1)*(s1+1)*math.sin(72/180*math.pi)]
                    farmer=[trianglearea-eacharea[0],trianglearea-eacharea[1],trianglearea-eacharea[2],trianglearea-eacharea[3],trianglearea-eacharea[4]]
                    landlord= eacharea[0]+eacharea[1]+eacharea[2]+eacharea[3]+eacharea[4]
                    farmersum=totalarea-landlord
                    #print(farmer, farmersum, landlord)
                    if farmersum>landlord:
                        count+=1
print(count)
'''