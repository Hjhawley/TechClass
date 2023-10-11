                .global stoi
                .text
stoi:
                li t0, 0            # Initialize n to 0
                li t1, 0            # Initialize i to 0
                li t4, 0            # Flag for negative numbers (set to false)
                lb t2, 0(a0)        # Load first character into t2
                li t3, 45           # ASCII for '-'
                beq t2, t3, 2f      # Jump to 2 if negative

            1:  lb t2, 0(a0)        # Load string[i] into t2
                li t3, 48           # ASCII for '0'
                blt t2, t3, 3f      # Jump to 3 if not a digit
                li t3, 57           # ASCII for '9'
                bgt t2, t3, 3f      # Jump to 3 if not a digit
                li t3, 10
                mul t0, t0, t3      # Multiply by 10 to move over a digit
                li t3, 48           # ASCII for '0'
                sub t2, t2, t3
                add t0, t0, t2      # n = n + (char - '0')
                addi t1, t1, 1      # Increment i
                addi a0, a0, 1      # Update string pointer
                j 1b                # Repeat loop

            2:  li t4, 1            # Flag for negative numbers (set to true)
                addi t1, t1, 1      # Increment i
                addi a0, a0, 1      # Update string pointer
                j 1b                # Repeat loop

            3:  beqz t4, 4f         # Check if result should be negative
                sub t0, x0, t0      # Subtract t0 from 0 to negate

            4:  mv a0, t0           # Return n
                ret
