a=input("A의 나이를 입력하시오")
b=input("B의 나이를 입력하시오")
c=input("C의 나이를 입력하시오")
d=input("D의 나이를 입력하시오")
e=input("E의 나이를 입력하시오")
age1=list=[a,b,c,d,e]
print(age1)
age2=age1.copy()
age2[0]=input("A의 나이를 입력하시오")
age2[1]=input("B의 나이를 입력하시오")
age2[2]=input("C의 나이를 입력하시오")
age2[3]=input("D의 나이를 입력하시오")
age2[4]=input("E의 나이를 입력하시오")
print(age1)
print(age2)
