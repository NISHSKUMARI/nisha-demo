class solution:
  def twosum(self, nums, target):
     dict_nums = {}

for idx, nums in range(nums):
      dict_nums[nums] = idx
for idx, nums in enumerate(nums):