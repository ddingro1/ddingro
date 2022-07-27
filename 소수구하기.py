x=int(input('1 이상의 정수를 입력하시오 : '))
z=[0 for i in range(x+1)]
c=0
for i in range(2, x+1): 
   if(z[i]==0):
    c+=1
    for j in range(2*i,x+1,i):
       z[j]=1
print('소수의 개수는 ',c)
