# Minimum and Maximum of an array

def minMax(nums):
  for i in range(0, len(nums) - 1):
    for j in range(i):
      if nums[j] > nums[j + 1]:
        temp = nums[j]
        nums[j] = nums[j + 1]
        nums[j + 1] = temp

  return [nums[0], nums[-1]]


nums = [4, 2, 8, 5, 1, 6, 3, 7]

print(minMax(nums))
