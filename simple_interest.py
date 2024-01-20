def simple_interest(x,y,z):
    print("The principle is ",x)
    print("The time period is ",y)
    print("The rate of interest is ",z)
    
    si=(x*y*z)/100
    return si
p=int(input("Enter principle:"))
r=int(input("Enter time period:"))
t=int(input("Enter rate of interest:"))
v=simple_interest(p,t,r)
print("The simple interest is:",v)
