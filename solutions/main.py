# DSA-Two-Pointer-Patterns — Solutions
# Author: Kushagra Bansal — Project Lab India

def two_sum_sorted(nums, target):
    """Sorted array two pointer | O(n) T, O(1) S"""
    l, r = 0, len(nums)-1
    while l < r:
        s = nums[l]+nums[r]
        if s == target: return [l+1, r+1]  # 1-indexed
        elif s < target: l += 1
        else: r -= 1
    return []

def three_sum(nums):
    """Sort + fix one + two pointer | O(n²) T, O(1) S"""
    nums.sort(); result = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue  # skip dup
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s == 0:
                result.append([nums[i],nums[l],nums[r]])
                while l < r and nums[l]==nums[l+1]: l += 1
                while l < r and nums[r]==nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0: l += 1
            else: r -= 1
    return result

def container_water(height):
    """Greedy move shorter side | O(n) T, O(1) S"""
    l, r = 0, len(height)-1; best = 0
    while l < r:
        best = max(best, min(height[l],height[r])*(r-l))
        if height[l] < height[r]: l += 1
        else: r -= 1
    return best

def sort_colors(nums):
    """Dutch National Flag — 3-way partition | O(n) T, O(1) S"""
    lo = mid = 0; hi = len(nums)-1
    while mid <= hi:
        if nums[mid] == 0:   nums[lo],nums[mid]=nums[mid],nums[lo]; lo+=1; mid+=1
        elif nums[mid] == 1: mid += 1
        else:                nums[mid],nums[hi]=nums[hi],nums[mid]; hi -= 1
    return nums

def remove_duplicates(nums):
    """In-place overwrite | O(n) T, O(1) S"""
    if not nums: return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]; k += 1
    return k

def is_palindrome(s):
    """Two ends toward center | O(n) T, O(1) S"""
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True

def trap_rain(height):
    """Two pointer left/right max | O(n) T, O(1) S"""
    l, r = 0, len(height)-1
    lmax = rmax = water = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water += lmax-height[l]; l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax-height[r]; r -= 1
    return water

def four_sum(nums, target):
    """Sort + fix two + two pointer | O(n³) T"""
    nums.sort(); n=len(nums); result=[]
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]: continue
        for j in range(i+1, n-2):
            if j>i+1 and nums[j]==nums[j-1]: continue
            l, r = j+1, n-1
            while l < r:
                s = nums[i]+nums[j]+nums[l]+nums[r]
                if s==target:
                    result.append([nums[i],nums[j],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: l+=1
                    while l<r and nums[r]==nums[r-1]: r-=1
                    l+=1; r-=1
                elif s<target: l+=1
                else: r-=1
    return result

def minimum_size_subarray(target, nums):
    """Variable window min length | O(n) T, O(1) S"""
    l = total = 0; best = float('inf')
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            best = min(best, r-l+1); total -= nums[l]; l += 1
    return best if best != float('inf') else 0

if __name__ == "__main__":
    print("="*58)
    print("  DSA Two Pointer Patterns — Project Lab India")
    print("="*58)
    print(f"  TwoSumSorted([2,7,11,15],9):        {two_sum_sorted([2,7,11,15],9)}")
    print(f"  ThreeSum([-1,0,1,2,-1,-4]):          {three_sum([-1,0,1,2,-1,-4])}")
    print(f"  ContainerWater([1,8,6,2,5,4,8,3,7]):{container_water([1,8,6,2,5,4,8,3,7])}")
    print(f"  SortColors([2,0,2,1,1,0]):           {sort_colors([2,0,2,1,1,0])}")
    print(f"  TrapRain([0,1,0,2,1,0,1,3,2,1,2,1]):{trap_rain([0,1,0,2,1,0,1,3,2,1,2,1])}")
    print(f"  isPalindrome('racecar'):             {is_palindrome('racecar')}")
    print("="*58)
