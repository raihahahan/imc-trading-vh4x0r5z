# IMC Trading Prosperity Hackathon

## Useful links
- Main page: https://prosperity.imc.com/
- Wiki: https://imc-prosperity.notion.site/IMC-Prosperity-Wiki-a59e66f3a9ca43c5a36545cfaf0debb5
- Island Simulation: https://prosperity.imc.com/leaderboard

## Development Process
### Getting Started with the Code

Firstly, In the root directory of the project, run the following code:   
```bash
virtualenv venv
```
This creates a virtual environment folder called "venv" with the necessary script. (Don't worry, this dir is already mentioned in.gitignore and will be ignored by git)

Next, run the following for **Mac**:
```bash
source venv/bin/activate
```
OR this for **Windows**:"
```bash
venv\Scripts\activate
```
This activated (i.e. enters) the virtual environment.

Finally, run the following:
```bash
pip install -r requirements.txt
```
This installs all dependencies locally as declared in the requirements.txt file (sth like `npm i` except that reads package.json automatically)

## Simulations
- Go to `src/simulator/simulator_instructions.md` to read on how to simulate the run algorithm against the given csv files.

### Important Caveats!!!
- Ensure the `run` method in `Trade` class doesn't exceed 900ms or it will time out!
- There is a position limit imposed on each product. Ensure any order made will not violate this, else the entire order will be rejected.

## Quick references
### Trader class
```py
from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order

class Trader:
    def run(self, state: TradingState) -> Dict[str, List[Order]]:
		"""
		Takes all buy and sell orders for all symbols as an input,
		and outputs a list of orders to be sent
		"""
        result = {}
        return result
```

## Some trading strategies
- **Trend following strategy:** This strategy involves identifying the direction of the trend and taking positions in the same direction. For example, if product A has been consistently increasing in price, you could take a long position (buy order) for A, expecting the trend to continue. Conversely, if product A has been consistently decreasing in price, you could take a short position (sell order) for A, expecting the trend to continue.

- **Mean reversion strategy:** This strategy involves taking positions in the opposite direction of the trend, assuming that prices will eventually revert to their mean. For example, if product A has experienced a sharp increase in price, you could take a short position for A, expecting the price to eventually come back down to its average. Conversely, if product A has experienced a sharp decrease in price, you could take a long position for A, expecting the price to eventually recover.
