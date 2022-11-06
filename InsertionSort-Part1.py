def insertion(nums):
    # nums = list(map(int, nums))
    i = 0

    for _ in range(len(nums) - 1):

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1] 
                nums[i + 1] = temp
                print(*nums)


    return ''

print(insertion([1, 4, 3, 5, 6, 2]))