import re
def remove_leading_zeros(expression):
    # 정규 표현식을 사용하여 선행 0을 제거
    cleaned_expression = re.sub(r'\b0+(\d)', r'\1', expression)
    return cleaned_expression
a=input()
a=remove_leading_zeros(a)
result=[]
count=1                         #result 리스트 안에 괄호 여부확인

for i in a:
    result+=i
    if count%2!=0 and i=='-':     #열린괄호가 없을떄
        result.append('(')
        count+=1
    elif count%2==0 and i=='-':   #열린괄호가 있을때 닫는 괄호로 덮어주기
        p=result.pop()
        result.append(')')
        result.append(p)
        result.append('(')
if count%2==0:                   #닫힌 괄호가 없을때 검사해서 닫는 괄호로 덮어주기
    result.append(')')
print(eval(''.join(result)))