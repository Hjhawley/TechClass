                .global _start, threshold
                .equ    sys_exit, 93

                .data
                # each element is stored as a 64 value
				.balign	8
test_array_1:   .8byte  5
                .equ    test_len_1, 1
test_array_2:   .8byte  2, 13, 16, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_2, 10

threshold:      .8byte  0
newline:        .asciz  "\n"

                .text
_start:
				.option	push
				.option norelax
				la		gp, __global_pointer$
				.option pop

                # test the function with the arrays above
                # using various threshold values
                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 10
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 0
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 5
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      t0, 6
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 0
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 2
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 3
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 10
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 13
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      t0, 14
                la      t1, threshold
                sd      t0, (t1)
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                # call the exit system call
                li      a0, 0
                li      a7, sys_exit
                ecall
