# Game of Nim
## Game Variant Details
This particular variant of Nim involves 2-5 (inclusive) piles, with 2n+1 items (such that n is the number of piles) distributed roughly evenly between the piles. Two subsequent game modes have been implemented: standard and misere. A player and an AI (implemented by a naive minimax algorithm) take turns selecting any amount of items from one and only one pile.

### Standard
In standard play, the person to pick up the last item wins.

### Misere
In misere play, the person to pick up the last item loses.

## How to Run
In your terminal emulator, situate yourself in the game-of-nim directory and enter `python src/driver.py` or `python3 src/driver.py`, depending on your environment.
