def big_sorting():
    nums = ['8', '1', '2', '100', '12303479849857341718340192371', '3084193741082937'
            '3084193741082938', '111', '200']

    # TECHNIQUE 1
    nums.sort(key = lambda x: (len(x), x))

    # TECHNIQUE 2
    nums = list(map(int, nums))

    for _ in range(len(nums) - 1):

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    nums = list(map(str, nums))
        
    return nums

print(big_sorting())