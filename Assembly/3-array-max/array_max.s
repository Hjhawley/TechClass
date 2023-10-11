                .global array_max
                .text

# int array_max(int *array, int count)
array_max:
                # a0 = *array
                # a1 = count (length)
                # a2 = max value
                # a3 = i
                ld a2, 0(a0)    # load the 1st value at a0 to a2
                li a3, 1        # set i to 1
            1:  bge a3, a1, 2f  # if i >= count, exit loop
                addi a0, a0, 8  # increment array by 8
                addi a3, a3, 1  # increment i by 1
                ld t1, 0(a0)    # load value at a0 into temp
                ble t1, a2, 1b  # if temp <= a2, go back to 1
                mv a2, t1       # if temp > a2, move temp to a2
                j 1b            # jump to 1
            2:  mv a0, a2       # move a2 to a0
                ret
