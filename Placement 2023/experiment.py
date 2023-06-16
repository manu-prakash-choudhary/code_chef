from typing import List
def find_min_greater(arr, indx):
    ele = arr[indx]
    min_greater = max(arr[indx:])
    min_greater_index = arr.index(min_greater, indx)
    for i in range(indx, len(arr)):
        if arr[i] > ele and arr[i] < arr[min_greater_index]:
            min_greater_index = i
    arr[indx], arr[min_greater_index] = arr[min_greater_index], arr[indx]
    arr[indx+1:] = sorted(arr[indx+1:])
    
    return arr

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found_yet = False
        find_pos_to_change = None
        
        for i in range(len(nums)):
            if nums[i] == max(nums[i:]):
                if i == 0:
                    continue
                index = i - 1
                if nums[index] < nums[i]:
                    find_pos_to_change = i - 1
        if find_pos_to_change is not None:
            nums = find_min_greater(nums, find_pos_to_change)
            found_yet = True
        
        if not found_yet:
            nums[:] = sorted(nums)
        print(nums)
    
nums = [2,2,3,4,2,3,1,1,2]

Solution().nextPermutation(nums=nums)
print(nums)
