# Iterated Prisoner's Dilemma: An Adaptive AI Player

This repository contains a Python AI agent designed to compete in the Iterated Prisoner's Dilemma, a classic game theory scenario.

The agent, implemented in the `MyPlayer` class, uses a multi-layered adaptive strategy. It does not rely on a single simple tactic (like Tit-for-Tat), but instead analyzes the game state and opponent's behavior to inform its decisions.

---

### ► The Strategy Explained

The core logic of this player is a hybrid of several strategies, making it robust against a variety of opponents.

1.  **Probing Opening Gambit:** The player begins with a fixed sequence of 6 moves (`Cooperate, Cooperate, Defect, Defect, Cooperate, Cooperate`). This sequence acts as a probe to gauge the opponent's response and serves as a unique "fingerprint."

2.  **Self-Recognition & Mirroring:** After the opening, the player checks if its own history matches the opening gambit. If it does (meaning it's likely playing against a clone of itself), it switches to a **pure Copycat (Tit-for-Tat)** strategy. This ensures optimal, mutually cooperative play against an identical agent.

3.  **Rational Payoff Analysis:** If not playing against itself, the core of the strategy is a rational, payoff-based decision. Given the opponent's last move, it calculates whether it's more profitable to `COOPERATE` or `DEFECT` based on the provided `payoff_matrix`.

4.  **Anti-Oscillation Mechanism:** The player tracks how many consecutive rounds the moves have been different (e.g., C vs D, D vs C). If this alternating pattern continues for 5 rounds (a state of mutual retaliation), the player attempts to break the cycle by cooperating, acting as a "forgiveness" mechanism.

5.  **Guaranteed Endgame Defection:** If the total number of iterations is known, the player will automatically `DEFECT` on the final move if betraying provides a higher payoff than mutual cooperation. This is a classic winning move in a finite game.

---

### ► How It Works

The logic is contained within the `MyPlayer` class:

-   `__init__(self, payoff_matrix, number_of_iterations)`: Initializes the player with the game's payoff rules and (optionally) the total number of rounds.
-   `select_move(self)`: The main decision-making engine. It analyzes the game history and applies the adaptive strategy to choose `COOPERATE` or `DEFECT`.
-   `record_last_moves(self, my_last_move, opponent_last_move)`: Updates the player's internal history after each round.

---

### ► How to Use

To use the player, import the class, define a payoff matrix, and instantiate the player.

```python
from my_player_file import MyPlayer, COOPERATE, DEFECT

# Define the payoff matrix for the game
# (My_Move, Opponent_Move) -> (My_Payoff, Opponent_Payoff)
payoff = {
    (COOPERATE, COOPERATE): (3, 3),
    (COOPERATE, DEFECT):   (0, 5),
    (DEFECT, COOPERATE):    (5, 0),
    (DEFECT, DEFECT):      (1, 1)
}

# Create an instance of the player
player = MyPlayer(payoff_matrix=payoff, number_of_iterations=100)

# In a game loop, you would:
# 1. Get the move from the player
my_move = player.select_move()

# 2. Get the opponent's move
opponent_move = get_opponent_move() # From the other player

# 3. Record the results for the next iteration
player.record_last_moves(my_move, opponent_move)
