Write a RISC-V function to count some of the values in an array.

Your function should implement this interface:

    int array_sum(int *array, int count)

(all `int` values mean 64-bit integers)

`array` is the address of an array of 64-bit integers, and
`count` is the number of entries in the array (so the total memory
used by the array is `8 × count`).

For each element in the array, you should call another function
that I provide:

    int predicate(int element)

It will return 0 if you should skip the element and 1 if you should
add it to the sum.

Pseudo-code for this function might look something like:

```
int array_sum(int *array, int count) {
    sum = 0
    for i = 0; i < count; i++ {
        if predicate(array[i]) {
            sum += array[i]
        }
    }
    return sum
}
```

Because `array_sum` calls another function, you must set up a
stack frame and use callee-saved registers. 

Write your code in the file `array_sum.s`.
