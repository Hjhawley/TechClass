                .global _start
                .equ    sys_exit, 93

                .data

                # each element is stored as a 64 value
                .balign 8
test_array_1:   .8byte  5
                .equ    test_len_1, 1
test_array_2:   .8byte  2, 13, 16, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_2, 10
test_array_3:   .8byte  2, 13, 16, 10000, 24, 5, 7, 11, 10, 6, 13
                .equ    test_len_3, 11

newline:        .asciz  "\n"

                .text
                # test the function with the arrays above
_start:
				.option	push
				.option norelax
				la		gp, __global_pointer$
				.option pop

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 10
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 5
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_1
                li      a1, test_len_1
                li      a2, 6
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 2
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 3
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 10
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 13
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_2
                li      a1, test_len_2
                li      a2, 14
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                la      a0, test_array_3
                li      a1, test_len_3
                li      a2, 0
                la      a4, array_sum
                call    call_function
                call    print_n
                la		a0, newline
				call	puts

                li      a0, 0
                li      a7, sys_exit
                ecall
