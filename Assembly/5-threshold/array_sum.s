                .global array_sum
                .text

# int array_sum(int *array, int count, int threshold)
array_sum:
                # a0 = address of an array
                # a1 = count (number of entries in the array)
                # a2 = threshold (ignore values less than this)

                # Initialize sum to 0, store in t0
                li t0, 0
                # Initialize i to 0, store in t1
                li t1, 0

            1:
                # Check if i < count
                bge t1, a1, 3f

                # Load array[i] into t2
                slli t3, t1, 3  # i * 8 (since each int is 8 bytes)
                add t3, a0, t3  # array + i * 8
                ld t2, 0(t3)    # load array[i] into t2

                # Check if array[i] >= threshold
                blt t2, a2, 2f
                # Add array[i] to sum
                add t0, t0, t2

            2:
                # Increment i
                addi t1, t1, 1
                # Repeat loop
                j 1b

            3:
                # Return sum
                mv a0, t0
                ret
