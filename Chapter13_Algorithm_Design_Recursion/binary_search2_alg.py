def recBinSearch(x, nums, low, high):
    if low > high:  # No place left to look, return -1
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:  # Found it! Return the index
        return mid
    elif x < item:  # Look in lower half
        return recBinSearch(x, nums, low, mid - 1)
    else:  # Look in upper half
        return recBinSearch(x, nums, mid + 1, high)


def search(x, nums):
    return recBinSearch(x, nums, 0, len(nums) - 1)
