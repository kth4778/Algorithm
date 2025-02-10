while True:
    try:
        s = str(int(input()))

        count = 0
        set_s = s[0]
        set_count = 0


        for i in s[1:]:
            if i == set_s:
                set_count += 1
            else:
                count = max(count, set_count + 1)
                set_s = i
                set_count = 0

        count = max(count, set_count + 1)
        print(count)
    except:
        exit()