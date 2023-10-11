Write a RISC-V function to find the largest element in an array.

Your function should implement this interface:

    int array_max(int *array, int count)

(all `int` values mean 64-bit integers)

`array` is the address of an array of 64-bit integers, and
`count` is the number of entries in the array (so the total memory
used by the array is `8 × count`).

You may assume that the array contains at least one element. Hint: 
start by assuming the first element is the largest, then scan the
rest of the array looking for anything bigger.

Note that this is a leaf function so there is no need to set up a
stack frame. You can do everything using scratch registers.

Write your code in the file `array_max.s`.

As an example, suppose a region of memory looks like this:

    +-----------+-----------+
    | Address   | Value     |
    +===========+===========+
    | ...       | ...       |
    | 9376      | 93        |
    | 9384      | -15       |
    | 9392      | -27       |
    | 9400      | 33        |
    | 9408      | 12        |
    | 9416      | 6         |
    | 9424      | 44        |
    | 9432      | 13        |
    | 9440      | 44        |
    | 9448      | 50        |
    | 9456      | 1000      |
    | ...       | ...       |
    +-----------+-----------+

Say that `array_max` is called with the parameter `array` set to
9384 (the address of the beginning of the array) and `count` set to
8 (the number of elements in the array). It should iterate through
the 8 elements (the values -15 through 44, respectively) and return
44, since that is the largest element in the array. Note that the
values at 9376 and 9448 are NOT part of the array.

If you follow the hint given above, you would proceed like this:

*   Grab element 0 from the array at address 9384, which is -15
*   Start scanning the rest of the list:
    *   element 1 is -27, so keep -15 as the largest element so far
    *   element 2 is 33, which is the new largest element so far
    *   element 3 is 12, so keep 33 as the largest element so far
    *   element 4 is 6, so keep 33 as the largest element so far
    *   element 5 is 44, which is the new largest element so far
    *   element 6 is 13, so keep 44 as the largest element so far
    *   element 7 is 44, so keep 44 as the largest element so far
*   Return 44, which was the largest element found
