def insertion(nums):
    i = 1
    shift = []
    count  = 0

    while i < len(nums):
        temp = nums[i]
        j = i
        while j > 0 and nums[j - 1] > temp:
            nums[j] = nums[j - 1] 
            j -= 1
            count += 1
        nums[j] = temp
        shift.append(count)
        count = 0
        i += 1

    return sum(shift)

print(insertion([2, 1, 3, 1, 2]))