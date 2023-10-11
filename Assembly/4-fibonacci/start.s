                .global _start
                .equ    sys_exit, 93

                .data
                .balign 8
inputs:         .8byte  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40
                .equ    test_count, 13

msg_calling:    .asciz  "Calling fibonacci with input "
msg_newline:    .asciz  "\n"
msg_got:        .asciz  "  return value was ========> "

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                # for i = 0; i < 21; i++
                li      s0, 0
1:
                la      t0, inputs
                slli    t1, s0, 3
                add     t2, t0, t1
                ld      s1, (t2)
                la      a0, msg_calling
                call    puts
                mv      a0, s1
                call    print_n
                la      a0, msg_newline
                call    puts
                la      a0, msg_got
                call    puts
                mv      a0, s1
                la      a4, fibonacci
                call    call_function
                call    print_n
                la      a0, msg_newline
                call    puts
                addi    s0, s0, 1
                li      t0, test_count
                blt     s0, t0, 1b

                li      a0, 0
                li      a7, sys_exit
                ecall
