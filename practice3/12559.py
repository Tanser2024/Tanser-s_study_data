from functools import cmp_to_key
def custom_compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
def largest_number(nums):
    nums.sort(key=cmp_to_key(custom_compare))
    result = ''.join(nums)
    return result
def smallest_number(nums):
    nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1 if x + y > y + x else 0))
    result = ''.join(nums)
    return result
n = int(input())
nums1 =  input().split()
largest = largest_number(nums1)
smallest = smallest_number(nums1)
print(f"{largest} {smallest}")

