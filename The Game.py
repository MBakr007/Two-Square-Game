array=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
print (array[0]+"   "+array[1]+"   "+array[2]+"   "+array[3])
print (array[4]+"   "+array[5]+"   "+array[6]+"   "+array[7])
print (array[8]+"  "+array[9]+"  "+array[10]+"  "+array[11])
print (array[12]+"  "+array[13]+"  "+array[14]+"  "+array[15])
player=0
test=[]
bool=True
b=0
n1=0
n2=0
c=0
while bool:
    if player==0 or player==1 or player==2:
        if player==0:
            player+=1
        elif player==1:
            player+=1
        elif player==2:
            player-=1
        print ("player"+str(player)+" : ")
        num1=int(input())
        num2=int(input())
        if ((num1%4==0 and num2==num1+1) or (num2%4==0 and num1==num2+1)):

            print("error,try again")
            if player==1:
                player=0
            if player==2:
                player=1

        elif (num1-num2==1 or num1-num2==4 or num1-num2==-1 or num1-num2==-4)and (str(num1) in array)and (str(num2) in array):
           n1=num1
           n2=num2
           array[num1-1]="X"
           array[num2-1]="X"
           print (array[0]+"  "+array[1]+"  "+array[2]+"  "+array[3])
           print (array[4]+"  "+array[5]+"  "+array[6]+"  "+array[7])
           print (array[8]+"  "+array[9]+"  "+array[10]+"  "+array[11])
           print (array[12]+"  "+array[13]+"  "+array[14]+"  "+array[15])
        else:
            print("error,try again")
            if player==1:
                player=0
            if player==2:
                player=1

        for i in range (0,16):
            if(array[i]=="X"):
                b+=1
            elif(array[i]!="X"):
                test.append(array[i])
        if(b==16):
            bool=False
            z=b
        elif(b==14):
            test[0]=int(test[0])
            test[1]=int(test[1])
            if((test[0]-test[1]!=-1) and (test[0]-test[1]!=1) and (test[0]-test[1]!=-4) and (test[0]-test[1])!=4):
                bool=False
                z=b
            else:
                b=0
                test=[]
        elif(b==12):
            for i in range (0,4):
                if(i!=3):
                    test[i]=int(test[i])
                    test[i+1]=int(test[i+1])
                    if((test[i]-test[i+1]!=-1)and(test[i]-test[i+1]!=1)and (test[i]-test[i+1]!=4)and(test[i]-test[i+1]!=-4)):
                        c+=1
                elif(i==3):
                    test[i]=int(test[i])
                    test[i-1]=int(test[i-1])
                    if((test[i]-test[i-1]!=-1)and(test[i]-test[i-1]!=1)and (test[i]-test[i-1]!=4)and(test[i]-test[i-1]!=-4)):
                        c+=1
                
            if(c==4):
                bool=False
                z=b
            else:
                b=0
                test=[]
        else:
            b=0
            test=[]
if(z==16 or z==12):
    print ("player 2 is the winner :) ")
elif(z==14):
    print("player 1 is the winner :) " )
