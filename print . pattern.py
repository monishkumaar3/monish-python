a=float(input("entr the starting number you want:"))
b=int(input("enter the number of rows to be printed:"))
for i in range(b):
    for j in range(i+1):
        print("%.1f"%a,end="")
        a=a+0.1
    print()
