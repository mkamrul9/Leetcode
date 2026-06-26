# this version is manual hashmap

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

# smaller same approach gives O(n) for time and space 

def containsDuplicate(nums):
    return len(nums) != len(set(nums))