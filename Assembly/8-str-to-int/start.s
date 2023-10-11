                .global _start
                .equ    sys_exit, 93

# a macro is code that is pasted into place when the macro is used
# so everywhere do_test appears in _start, this chunk of code is pasted in
.macro do_test label, expected
                la      a0, msg_testing
                call    puts
                la      a0, \label
                call    puts
                la      a0, msg_expected
                call    puts
                li      a0, \expected
                call    print_n
                la      a0, msg_actual
                call    puts
                la      a0, \label
                la      a4, stoi
                call    call_function
                call    print_n
                la      a0, msg_newline
                call    puts
.endm

                .data
test0:          .asciz  "0"
test1:          .asciz  ""
test2:          .asciz  "notanumber"
test3:          .asciz  " 123"

test4:          .asciz  "1"
test5:          .asciz  "9"
test6:          .asciz  "5"

test7:          .asciz  "34"
test8:          .asciz  "90"
test9:          .asciz  "55"
test10:         .asciz  "01"
test11:         .asciz  "23junk"
test12:         .asciz  "00 123"

test13:         .asciz  "100"
test14:         .asciz  "999"
test15:         .asciz  "123456"
test16:         .asciz  "987654321"
test17:         .asciz  "987654321-0"

test18:         .asciz  "-100"
test19:         .asciz  "-"
test20:         .asciz  "-999"
test21:         .asciz  "-123456"
test22:         .asciz  "-987654321"
test23:         .asciz  "-987654321-0"
test24:         .asciz  "--987654321-0"

msg_testing:    .asciz  "\nCalling stoi with the string \""
msg_expected:   .asciz  "\"\nExpecting the result: "
msg_actual:     .asciz  "\nActual return value : "
msg_newline:    .asciz  "\n"

                .text
_start:
				.option	push
				.option norelax
				la		gp, __global_pointer$
				.option pop

                # tests that should all return zero
                do_test test0, 0
                do_test test1, 0
                do_test test2, 0
                do_test test3, 0

                # one-digit tests
                do_test test4, 1
                do_test test5, 9
                do_test test6, 5

                # two-digit tests
                do_test test7, 34
                do_test test8, 90
                do_test test9, 55
                do_test test10, 1
                do_test test11, 23
                do_test test12, 0

                # multi-digit tests
                do_test test13, 100
                do_test test14, 999
                do_test test15, 123456
                do_test test16, 987654321
                do_test test17, 987654321

                # negative tests
                do_test test18, -100
                do_test test19, 0
                do_test test20, -999
                do_test test21, -123456
                do_test test22, -987654321
                do_test test23, -987654321
                do_test test24, 0

                # exit system call
                li      a0, 0
                li      a7, sys_exit
                ecall
