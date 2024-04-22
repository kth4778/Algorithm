a=int(input())
int_5=a//5
int_3=(a-(int_5*5))//3
while int_3*3+int_5*5!=a:
    if int_5==-1:
        break
    else:
        int_5-=1
        int_3=(a-(int_5*5))//3
if int_5<0:
    print(-1)
else:
    print(int_3+int_5)