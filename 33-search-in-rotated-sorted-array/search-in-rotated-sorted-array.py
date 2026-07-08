'''when a sorted array is rotated, we have one pivot where the array changes from increasing to decreasing. if we divide the array in to two at the pivot, we got two sorted arrays. but if we devide it in any other position, the part with the pivot won't be sorted but the other part is guaranteed to be sorted. we look for that sorted part and check if target is in that range as a condition to half the search space.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]: # is the left part sorted
                # is target in the left sorted part
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # is the right part sorted
                # is target in the right sorted part
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1