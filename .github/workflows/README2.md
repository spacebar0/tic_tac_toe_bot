# Tic-Tac-Toe AI

This project implements an unbeatable Tic-Tac-Toe AI using the Minimax algorithm, wrapped in a Pygame graphical interface.

## 🎮 How It Works: The Minimax Algorithm

The core of this project is the **Minimax algorithm**, a recursive decision-making algorithm used in game theory and AI for two-player turn-based games.

### The Concept
Minimax views the game as a tree of possible future states.
- **The Root**: The current state of the board.
- **Branches**: Possible moves.
- **Leaves**: Terminal states (Win, Loss, or Tie).

### The Logic
The algorithm assumes the opponent plays optimally. It assigns a value to every possible board state:
- **+1**: X wins
- **-1**: O wins
- **0**: Tie

### The Process
1. **Recursion**: The AI simulates playing the game forward, move by move, until it reaches a game-over state.
2. **Maximizing vs. Minimizing**:
    - **X (The Maximizer)**: Wants to choose the move that leads to the highest score (+1).
    - **O (The Minimizer)**: Wants to choose the move that leads to the lowest score (-1).
3. **Backtracking**: Once a terminal state is reached, the value is passed back up the tree.
    - If it's X's turn, I pick the move with the *maximum* value returned from the children.
    - If it's O's turn, I pick the move with the *minimum* value returned from the children.

By doing this, the AI guarantees that it makes the move that leads to the best possible outcome, assuming the opponent also plays perfectly. Since Tic-Tac-Toe is a solved game, perfect play from both sides always results in a tie. **The AI will never lose.**

## 🛠️ What I Did

I implemented the game logic and AI intelligence in `tictactoe.py`.

### Key Functions Implemented:
- **`player(board)`**: Determines whose turn it is based on the current board state.
- **`actions(board)`**: Returns a set of all possible legal moves.
- **`result(board, action)`**: Returns the new board state after a move is applied (without modifying the original).
- **`winner(board)`**: Checks if X or O has won horizontally, vertically, or diagonally.
- **`terminal(board)`**: Checks if the game has ended (win or tie).
- **`utility(board)`**: Assigns a score to the terminal state:
    - `1` for X win
    - `-1` for O win
    - `0` for Tie
- **`minimax(board)`**: The brain of the AI. It recursively calls `max_value` and `min_value` to determine the best possible move.

## 🚀 Getting Started

### Prerequisites
- Python 3
- Pygame

### Installation
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game
Run the game using the runner script:
```bash
python runner.py
```

Select a player (X or O) and try to beat the AI!
