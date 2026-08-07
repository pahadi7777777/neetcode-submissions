class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        left = 0
        right = len(nums)-1

        while right >= left:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid-1

            else:
                left = mid + 1