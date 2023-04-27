# fixie-game
A hackathon attempt at conflict resolution simulation between two AI LLM agents

## Requirements

* Python >= 3.10

* An account at https://app.fixie.ai

## Install Instructions

1. Create a .env file in this folder with:
    * a valid api key - FIXIE_API_KEY
    * your fixie username - FIXIE_USERNAME

2. Initialize a python virtual environment. https://docs.python.org/3/library/venv.html

3. Activate the python virtual environment by running `.venv/bin/activate`

4. Install dependencies with `pip install -r requirements.txt` 

5. Run the game with `python main.py`

6. Make Red and Blue friends again!


## Useful In-Game Commands

    !exit - Exits the game.            
    !red  - Talk to Red.               
    !blue - Talk to Blue.              
    !meet - Make the agents chat with each other.                
    !help - See this command list.     

NOTE: There is no "end" state. The game will not end on its own. 
