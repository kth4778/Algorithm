consonont_lower=['b' ,'k' ,'x','z' ,'n' ,'h','d' ,'c' ,'w' ,'g' ,'p' ,'v','j','q','t','s','r','l','m','f']
consonont_upper=['B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F']
vowel_lower=['a','i','y','e','o','u']
vowel_upper=['A','I','Y','E','O','U']
while True:
    try:
        stirng=input()
        result=''
        for i in stirng:
            if i.isupper():
                if i in vowel_upper:
                    result+=vowel_upper[(vowel_upper.index(i)+3)%6]
                else:
                    result+=consonont_upper[(consonont_upper.index(i)+10)%20]
            elif i.islower():
                if i in vowel_lower:
                    result+=vowel_lower[(vowel_lower.index(i)+3)%6]
                else:
                    result+=consonont_lower[(consonont_lower.index(i)+10)%20]
            else:
                result+=i
        print(result)
    except:
        break