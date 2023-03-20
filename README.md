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


### Important Caveats!!!
- Ensure the `run` method in `Trade` class doesn't exceed 900ms or it will time out!
- There is a position limit imposed on each product. Ensure any order made will not violate this, else the entire order will be rejected.
