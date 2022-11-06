def insertion(nums):
    i = 1

    while i < len(nums):
        temp = nums[i]
        j = i
        while j > 0 and nums[j - 1] > temp:
            nums[j] = nums[j - 1] 
            j -= 1
        nums[j] = temp

        print(*nums)

        i += 1

    return ''

print(insertion([1, 4, 3, 5, 6, 2]))

# print(" ".join(map(str, nums)))