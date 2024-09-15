
#pro4.write a program binary search...
def binary_search(arr, target):

    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    user_input = input("Enter a sorted list of integers: ")
    arr = list(map(int, user_input.split()))
    target = int(input("Enter the value to search: "))
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")
