# World Cup Bracket Predictor

A simple interactive command-line tool to simulate World Cup match outcomes based on user-defined probabilities.

You assign probability weights (out of 10) for three outcomes of a match:

1. **Draw** — probability of the match ending in a tie
2. **Team A win** — probability of Team A winning
3. **Team B win** — calculated automatically as the remainder (`10 - draw - teamA`)

The tool then rolls a random number and prints the simulated result.

## Usage

```bash
python3 bracket.py
```

After each result, the tool loops and prompts for the next match. Press **Ctrl+C** to exit.

