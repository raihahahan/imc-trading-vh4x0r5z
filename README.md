# IMC Trading Prosperity Hackathon

## Useful links
- Main page: https://prosperity.imc.com/
- Wiki: https://imc-prosperity.notion.site/IMC-Prosperity-Wiki-a59e66f3a9ca43c5a36545cfaf0debb5
- Island Simulation: https://prosperity.imc.com/leaderboard

## Development Process
### Important Caveats!!!
- Ensure the `run` method in `Trade` class doesn't exceed 900ms or it will time out!
- There is a position limit imposed on each product. Ensure any order made will not violate this, else the entire order will be rejected.
