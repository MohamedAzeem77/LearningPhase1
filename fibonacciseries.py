def fibo(n1,n2,count):
    while count<11:
        print(n1,end=" ")
        n1,n2=n2,n1+n2
        count+=1

n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
count=int(input("Enter count:"))

fibo(n1,n2,count)
