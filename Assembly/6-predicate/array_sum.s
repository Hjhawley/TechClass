                .global array_sum
                .text

# int array_sum(int *array, int count)
array_sum:
                # Set up stack frame and save callee-saved registers
                addi sp, sp, -16
                sd s0, 8(sp)
                sd ra, 0(sp)
                # Move stack pointer to frame pointer
                add s0, sp, 16
                # Initialize sum to 0, stored in t0
                li t0, 0
                # Initialize loop counter i to 0, stored in t1
                li t1, 0

            1:
                # Check if i < count
                bge t1, a1, 3f
                # Load array[i] into t2
                slli t3, t1, 3  # i * 8 (since each int is 8 bytes)
                add t3, a0, t3  # array + i * 8
                ld t2, 0(t3)    # load array[i] into t2
                # Call predicate function
                mv a0, t2       # Move element to a0 for function argument
                call predicate
                # Check return value of predicate
                beqz a0, 2f
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
                # Restore callee-saved registers and tear down stack frame
                ld ra, 0(sp)
                ld s0, 8(sp)
                addi sp, sp, 16
                ret
