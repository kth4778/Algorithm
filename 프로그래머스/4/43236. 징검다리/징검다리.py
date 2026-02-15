def solution(distance, rocks, n):
    rocks.sort()

    def available(size, end, n):
        start = 0
        used_count = 0

        for rock in rocks:

            if rock - start < size:
                used_count += 1
                if used_count > n:
                    return False
            else:
                start = rock

        if end - start < size:
            used_count += 1
            if used_count > n:
                return False

        return True

    left = 0
    right = distance

    while left <= right:
        mid = (left + right) // 2
        if available(mid, distance, n):
            left = mid + 1
        else:
            right = mid - 1
        
    return right