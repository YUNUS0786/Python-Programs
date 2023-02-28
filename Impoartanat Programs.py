
print("---------------1---------------------")

x=int(input("Enter the 1st number"))
y=int(input("Enter the 2nd number"))
print("The numbers before SWappin are:",x,y)
temp=x
x=y
y=temp
print("The numbers after swapping are:",x,y)

print("---------------2---------------------")


x=int(input("Enter the 1st number"))
y=int(input("Enter the 2nd number"))
print("The numbers before SWappin are:",x,y)
x=x+y
y=x-y
x=x-y
print("The numbers after swapping are:",x,y)


print("--------------3----------------------")

def fun(num):
    if num>0:
        print(num,"is a positive number.")
    elif num<0:
        print(num,"is a negative number.")
    else:
        print(num,"is Zero.")
num=int(input("Enter a number"))
fun(num)

print("--------------4---------------------")


def fun(num):
    if num%2==0:
        print(num,"is Even number.")
    else:
        print(num,"is odd numbber.")
num=int(input("Enter a number."))
fun(num)        

print("--------------5----------------------")

def fun(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num,"is a prime number")
    else:
            print(num,"is a not a primwe number")
num=int(intput("Enter a number:"))
fun(num)        
                






