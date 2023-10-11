                .global _start
                .equ    sys_exit, 93

                .data
msg_calling:    .asciz  "Calling hw with no input\n"
msg_got:        .asciz  "  hw returned =========> "
msg_newline:    .asciz  "\n"

                .text
_start:
                .option push
                .option norelax
                la      gp, __global_pointer$
                .option pop

                la      a0, msg_calling
                call    puts
                la      a0, msg_got
                call    puts
                la      a4, hw
                call    call_function
                call    print_n
                la      a0, msg_newline
                call    puts

                li      a0, 0
                li      a7, sys_exit
                ecall
