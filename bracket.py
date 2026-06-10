#!/usr/bin/env python3
import random
import sys
import termios
import tty

def read_int(prompt, lo, hi):
    """Prompt the user and return an int in [lo, hi] on the first valid keypress."""
    while True:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        if ch == '\x03':          # Ctrl+C
            raise KeyboardInterrupt
        if ch.isdigit() and lo <= int(ch) <= hi:
            print(ch)             # echo the accepted digit
            return int(ch)
        # silent reject — just re-prompt

print("World Cup Bracket Helper — Press Ctrl+C to exit\n")

while True:
    try:
        # --- Team A probability ---
        a = read_int(f"Prob of TEAM A winning (1–9): ", 1, 9)

        # --- Draw probability ---
        max_draw = 10 - a
        draw = read_int(f"Prob of DRAW (1–{max_draw}): ", 1, max_draw)

        b = 10 - draw - a

        # Scale to probabilities
        p_draw = draw / 10
        p_a    = a    / 10
        p_b    = b    / 10

        print(f"  Probabilities → A: {p_a:.0%}  B: {p_b:.0%}  Draw: {p_draw:.0%}")

        roll = random.random()
        if roll < p_a:
            result = "⚽  TEAM A WINS"
        elif roll < p_a + p_b:
            result = "⚽  TEAM B WINS"
        else:
            result = "🤝  DRAW"

        print(f"\n  ➜  {result}\n")

    except KeyboardInterrupt:
        print("\n\nGood luck with your bracket!")
        break
