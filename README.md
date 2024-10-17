
# Dice Game AI - Human vs Bots
# Liar's Dice - ICT-STRYPES Code Challenge

This is a Python-based dice game where human players compete against bots, with the hardest being AI, across various difficulty levels. The bots utilize their own gameplay logic based on difficulty and dynamic strategies such as safe play, aggressive moves, or bluffing, providing a challenging gaming experience. The game involves bidding on dice quantities and values, as well as calling bluffs or fake bids.

## Features

- **Human vs. AI Bots**: Play against up to 3 bots with adjustable difficulty levels:
  - **Easy**: Random percentage bids.
  - **Medium**: An algorithm calculates risk and possibilities based on the bot's advantages and the current game state.
  - **Hard**: AI-powered bots analyze previous game history logs and adapt their strategies based on this information, employing different playstyles.
- **Wild Ones Mode**: Enable or disable "ones" as wild dice for more complex strategies and unexpected turns.
- **Interactive Game Interface**: Real-time updates of dice, bids, and player actions in a scrollable display.
- **Make Bids / Call Fakes**: Place a bid higher than the current one or call out a bluff.
- **AI Strategies**: The hard bots employ dynamic playstyles based on their difficulty, choosing between safe, aggressive, or bluffing tactics.
- **Round Results**: Get instant feedback on each round’s winner, including the number of dice that match the bid.
- **Hints System**: An option for players to use hints to aid in decision-making.
- **Automatic Updates**: The interface refreshes to display current player actions and game progress.

## AI Used

The AI logic for the bots is built using the following approaches:

- **Analysis**: Analyzing the game history log to understand other players' playstyles and develop strategies to beat them.
- **Safe Strategy**: In lower difficulty levels, bots play conservatively, making bids that are less likely to be challenged and rarely calling bluffs.
- **Aggressive Playstyle**: Higher difficulty bots take more risks by making bold bids and calling out bluffs more frequently.
- **Bluffing Mechanism**: Bots simulate human-like bluffing behavior, attempting to deceive the human player into making risky decisions.
- **Hints**: Use your single hint in the game when the situation becomes serious. This feature is powered by an AI model.

## How to Run

1. Clone the repository.
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
3. Run app.py file
