Write a RISC-V function to count some of the values in an array.

Your function should implement this interface:

    int array_count(int *array, int count, int threshold)

(all `int` values mean 64-bit integers)

`array` is the address of an array of 64-bit integers, and
`count` is the number of entries in the array (so the total memory
used by the array is `8 × count`).

You should compute and return the sum of the elements in the array
that are greater or equal to `threshold`. Ignore values in the array
that are less than `threshold`.

Pseudo-code for this function might look something like:

```
int array_count(int *array, int count, int threshold) {
    sum = 0
    for i = 0; i < count; i++ {
        if array[i] >= threshold {
            sum += array[i]
        }
    }
    return sum
}
```

Note that this is a leaf function so there is no need to set up a
stack frame. You can do everything using scratch registers.

Write your code in the file `array_sum.s`.
