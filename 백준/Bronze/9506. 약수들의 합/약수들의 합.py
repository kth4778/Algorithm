while True:
    a=int(input())
    if a==-1:
        break
    else:
        result=[i for i in range(1,a) if a%i==0]
        if sum(result)==a:
            result=str(result)
            result=result.replace(',',' +')
            print(f"{a} = {result[1:-1]}")
        else:
            print(f"{a} is NOT perfect.")