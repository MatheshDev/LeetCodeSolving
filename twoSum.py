# Brute Force Method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


#Dictionary method

def twoSum(nums, target):
  seen = {}
  for i, num in enumerate(nums):
    if (target - num) in seen:
      return [seen[target - num], i]
    else:
      seen[num] = i
