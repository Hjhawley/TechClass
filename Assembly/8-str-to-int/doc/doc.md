String to integer
=================

Write a function called `stoi` to convert a string containing a base
10 number to an integer value.

    stoi(char *string) -> n

`stoi` is given the address of a string in memory containing a text
representation of an integer value. Here is the basic algorithm for
doing this:

    n = 0
    i = 0
    loop:
        // note: string is an array of 1-byte values
        c = string[i]
        if c < '0' or c > '9':
            break
        n = n * 10 + (c - '0')
        i += 1
    return n

Note that you do not know in advance how many characters make up the
number. As soon as you read something that is not a digit, you
should assume you have reached the end of the input.

In addition to the outline given above, you should accept an
optional `-` (minus sign) at the beginning of the input, and return
a negative number instead of a positive number. Write your code to
work with non-negative numbers first, then go back and modify it to
do the following:

*   Before the loop begins, check if the first character is a '-'.
    If it is, start at i=1 instead of i=0 and remember that the
    result should be negative (use a spare register to store this
    info).
*   Read the digits as normal.
*   After the loop ends, check if the result should be negative. If
    so, use the 'neg' instruction to flip the sign of the result.

For example, if `stoi` is called with 0x1230 as the value of the
buffer pointer, and memory contains the following:

* 0x1230: '3' (ASCII code 51)
* 0x1231: '8' (ASCII code 56)
* 0x1232: '0' (ASCII code 48)
* 0x1233: '1' (ASCII code 49)
* 0x1234: '2' (ASCII code 50)
* 0x1235: ' ' (ASCII code 32)

Your function should return the number 38012.


Hints
-----

To negate a value, you can just subtract it from zero, or you can
use the `neg` pseudo-instruction.

To multiply a value by 10, use the `mul` instruction. There is no
`muli` instruction so you must load a 10 into a register first to
perform the multiplication.

Start by writing just enough code to convert a single digit, and
test it with suitable inputs ("5", "0", "1", etc.).

Then add the loop structure and try it with two digit numbers, three
digit numbers, etc.

Then add in support for negative numbers at the end.

Each time you add more cases to your code, run `make` to run tests
that exercises the new code you have written.
