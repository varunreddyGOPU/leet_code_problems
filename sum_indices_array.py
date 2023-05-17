# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Brute force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

def twosum(nums:list[int], target:int):

    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):

    #         if nums[j]==target-nums[i]:
    #             return [i,j]

    # --------------------------------

    hashmap={}
    for i in range(len(nums)):
            
            hashmap[nums[i]]=i
    for i in range(len(nums)):
            
            complement=target-nums[i]
            if complement in hashmap and hashmap[complement] !=i:
                return [i, hashmap[complement]]


nums = [2, 7, 11, 15]
target = 9

result = twosum(nums, target)
print(result)



