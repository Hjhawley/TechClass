                .global _start
                .equ    sys_exit, 93

                .data
				.balign 8
array1:         .8byte  1
array2:         .8byte  -1
array3:         .8byte  -1, -1, -1
array4:         .8byte  0, 2, -3, -1, 2, -1, -5, 0, 0, -4
array5:         .8byte  20, 9, 9, 9, 9, 9, 9, 9, 9, 9
                .8byte  -10, -10, -10, -10, -10, -10, -10, -10, -10, -10
msg_testing:    .asciz  "\nTesting with the array: "
msg_comma:      .asciz  ", "
msg_newline:    .asciz  "\n"
msg_expected:   .asciz  "\nExpecting return value of:  "
msg_actual:     .asciz  "\nGot actual return value of: "

                .text
_start:
				.option	push
				.option norelax
				la		gp, __global_pointer$
				.option pop

                # test the function with each of the arrays above
                la      a0, array1
                li      a1, 1
                li      a2, 1
                call    run_test

                la      a0, array2
                li      a1, 1
                li      a2, 1
                call    run_test

                la      a0, array3
                li      a1, 3
                li      a2, 3
                call    run_test

                la      a0, array4
                li      a1, 10
                li      a2, 7
                call    run_test

                la      a0, array5
                li      a1, 20
                li      a2, 20
                call    run_test

                li      a0, 0
                li      a7, sys_exit
                ecall


run_test:
                addi    sp, sp, -48
                sd      ra, 40(sp)
                sd      s3, 32(sp)
                sd      s2, 24(sp)
                sd      s1, 16(sp)
                sd      s0, 8(sp)

                mv      s0, a0
                mv      s1, a1
                mv      s2, a2

                la      a0, msg_testing
                call    puts

                li      s3, 0
1:
                beqz    s3, 2f
                la      a0, msg_comma
                call    puts
2:
                slli    t0, s3, 3
                add     t0, s0, t0
                ld      a0, (t0)
                call    print_n
                addi    s3, s3, 1
                blt     s3, s1, 1b

                la      a0, msg_expected
                call    puts
                mv      a0, s2
                call    print_n
                la      a0, msg_actual
                call    puts

                mv      a0, s0
                mv      a1, s1
                la      a4, count_jumps
                call    call_function
                call    print_n
                la      a0, msg_newline
                call    puts

                ld      ra, 40(sp)
                ld      s3, 32(sp)
                ld      s2, 24(sp)
                ld      s1, 16(sp)
                ld      s0, 8(sp)
                addi    sp, sp, 48
                ret
