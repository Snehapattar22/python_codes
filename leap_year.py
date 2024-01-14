def leap_year(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        print("its leap year")
    else:
        print("not a leap year")
n=int(input("enter the year: "))
leap_year(n)
