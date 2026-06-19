def yequation():
    while True:
        try:
            x1,y1=input("Enter x1 & y1 values separated by space : ").split()
            x1,y1=int(x1),int(y1)
            break
        except ValueError:
            print("Check inputs again whether you have entered them according to instructions or not!")
    while True:
        try:
            x2,y2=input("Enter x2 & y2 values separated by space : ").split()
            x2,y2=int(x2),int(y2)
            break
        except ValueError:
            print("Check inputs again whether you have entered them according to instructions or not!")


    if x1==x2 and y1==y2:
        print(f"To use this programme at least you want primary knowledge in algebra.You can not find the equation if you have only one point!!!")
    else:
        if x1==x2 or y1==y2:
            if x1==x2:
                print(f"The equation : x={x1}")
            elif y1==y2:
                print(f"The equation : y={y1}")
        else:
            a=(y1-y2)/(x1-x2)
            b=0
            if x1<x2:
                if x1==0:
                    b=y1
                elif x1>0:
                    while x1!=0:
                        x1-=1
                        y1-=a
                else:
                    while x1!=0:
                        x1+=1
                        y1+=a

                b=y1
            elif x1>x2:
                if x1==0:
                    b=y1
                elif x1>0:
                    while x2!=0:
                        x2-=1
                        y2-=a
                else:
                    while x2!=0:
                        x2 += 1
                        y2 += a
                if x1!=0:
                    b=y2

            if b>0:
                print(f"The equation : y={a:.2f}X+{b:.2f}")
            else:
                print(f"The equation : y={a:.2f}X-{(b+(-2*b)):.2f}")



print("Do not enter floating point numbers!")
print()
yequation()