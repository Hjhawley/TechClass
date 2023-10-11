                .global am_or_fm

                .text
am_or_fm:
                li t0, 535
                blt a0, t0, 1f
                li t0, 1605
                bgt a0, t0, 1f
                li a0, 1
                ret
            1:  li t0, 88
                blt a0, t0, 2f
                li t0, 108
                bgt a0, t0, 2f
                li a0, 2
                ret
            2:  li a0, 0
                ret
