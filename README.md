# Minesweeper

A classic command-line Minesweeper game implemented in Python with ASCII art interfaces.

---

## Features

- **Difficulty Levels**:
  - **Easy**: 8×8 grid with 10 mines
  - **Average**: 9×9 grid with 20 mines
  - **Hard**: 10×10 grid with 40 mines
- **Recursive Zero-Expansion**: Automatically reveals neighboring empty cells when a `0` cell is uncovered.
- **Flagging System**: Flag and unflag suspected mine locations.
- **Save & Load**: Save your current progress and load previous games.
- **ASCII Art UI**: Visual banners, instructions, and win/loss screens.

---

## Requirements

- Python 3.6 or higher
- Standard library modules only (`random`, `os`, `pickle` — no additional pip packages required)

---

## How to Run

1. Clone or download this project folder.
2. Open a terminal / command prompt in the project directory.
3. Run:

```bash
python minesweeper.py
```

---

## How to Play

### In-Game Controls

| Action | Command Format | Example |
| :--- | :--- | :--- |
| **Reveal a cell** | `<Row> <Column>` | `1 A` |
| **Flag / Unflag a cell** | `<Row> <Column> F` | `1 A F` |
| **Save current game** | `S` | `S` |
| **Load saved game** | `L` | `L` |
| **Return to main menu** | `M` | `M` |

### Rules
- Uncover numbers indicating how many mines are adjacent to that square (horizontally, vertically, or diagonally).
- Use flags (`F`) to mark squares you believe contain mines.
- Reveal all non-mine cells on the board to win.
- Stepping on a mine ends the game!

---

## Project Structure

- `minesweeper.py`: Main game logic, grid rendering, input handling, and save/load system.
- `graphics.py`: ASCII art displays for menu, banner, instructions, win, and game-over screens.
