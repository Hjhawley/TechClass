                .global count_jumps
                .text

# int count_jumps(int *array, int size)
count_jumps:
                addi t0, a1, -1     # int index = -1 (last item)
                li t1, 0            # int count = 0

            1:  blt t0, x0, 2f      # while index >= 0
                bge t0, a1, 2f      # while index < size
                slli t3, t0, 3      # index * 8 (8-byte integers)
                add t3, a0, t3      # array + index * 8
                ld t2, 0(t3)        # load array[index] into t2
                add t0, t0, t2      # index += array[index]
                addi t1, t1, 1      # increment count
                j 1b
                
            2:  mv a0, t1           # return count
                ret
