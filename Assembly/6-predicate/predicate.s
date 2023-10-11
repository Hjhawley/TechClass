                .global predicate
                .text

                # return 0 if the argument is < threshold, 1 if it is >=
predicate:
                # scribble all over the scratch registers for fun
                li      a1, 123
                li      a2, 123
                li      a3, 123
                li      a4, 123
                li      a5, 123
                li      a6, 123
                li      a7, 123
                li      t1, 123
                li      t2, 123
                li      t3, 123
                li      t4, 123
                li      t5, 123
                li      t6, 123

                la      t0, threshold
                ld      t0, (t0)
                slt     a0, a0, t0
                xori    a0, a0, 1
                ret
