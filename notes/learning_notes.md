# Two Pointer — Learning Notes
# By Kushagra Bansal | Project Lab India

## When To Use Two Pointers
- Sorted array + pair/triplet sum → Opposite ends
- Find duplicates in sorted array → Same direction
- Linked list: cycle/middle/kth end → Fast+slow
- Palindrome check → Both ends inward
- Trapping water/container → Move shorter side

## Core Templates
# Opposite ends (sorted array)
l, r = 0, len(nums)-1
while l < r:
    if condition: return result
    elif too_small: l += 1
    else: r -= 1

# Same direction (duplicates/window)
slow = 0
for fast in range(1, len(nums)):
    if condition: slow += 1; arr[slow] = arr[fast]

## Key Patterns
| Problem | Pointer Movement | Key Insight |
|---------|-----------------|-------------|
| Two Sum | Move based on sum vs target | Sort first |
| Three Sum | Fix i, two-pointer j,k | Skip duplicates |
| Container | Move shorter height | Taller determines max |
| Dutch Flag | 3 pointers: lo,mid,hi | Invariant maintenance |
