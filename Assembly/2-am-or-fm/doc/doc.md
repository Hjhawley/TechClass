Back when your parents were still hunting food with clubs and
carving figures into cave walls, people listened to music on
broadcast radio. Stations were broadcast in either the AM band
(535–1605 kHz) or the FM band (88–108 MHz). If someone told you a
frequency number but did not specify which band it was in, you could
figure it out based on which range of numbers it fit in.

Write an assembly language function (not a complete program, just a
function) that does this. It should work like this Python function:

``` python
def am_or_fm(freq):
    if freq >= 535 and freq <= 1605:
        return 1
    if freq >= 88 and freq <= 108:
        return 2
    return 0
```

In other words, it takes a single argument and returns 1 if the
argument is in the right range to be an AM station, or 2 if the
arbument is in the right range to be an FM station. It returns 0 if
the number is not in either range.

Write your function in `am_or_fm.s`. Run `make` from the command
line to test your function.
