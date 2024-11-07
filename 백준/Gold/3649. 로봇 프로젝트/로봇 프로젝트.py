import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input().strip())
        x *= 10 ** 7

        n = int(input().strip())
        nums = sorted(list(int(input()) for _ in range(n)))

        answer = "danger"
        l = 0
        r = n - 1

        while l < r:
            p = nums[l] + nums[r]

            if p == x:
                answer = f"yes {nums[l]} {nums[r]}"
                break

            if p < x:
                l += 1

            else:
                r -= 1
        
        print(answer)
        

    except:
        sys.exit()