def search(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:  # item found, return the index value
            return i
    return -1  # loop finished, item was not in list

def main():
    data = [1, 2, 5, 1, 3]
    x = 3
    print(search(x, data))

main()