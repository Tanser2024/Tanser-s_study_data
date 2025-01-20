
def searchRange(self, nums, target):
    if target not in set(nums):
        return [-1, -1]
    left = 0;right = len(nums) - 1
    while nums[left] < target<nums[right]:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            break
    while nums[right] > target:
                right -= 1
    while nums[left] < target:
                left += 1
    return [left,right]

