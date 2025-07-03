# PythonProjectWithAI_1

A simple Tic-Tac-Toe game implemented in Python with both console and GUI modes. The project is structured using OOP principles and includes automated tests.

## Features
- Play Tic-Tac-Toe in the console, with a graphical user interface (GUI), or in a web browser
- Mode selection via command line argument
- Clean, maintainable code using an abstract base class
- Automated tests for core game logic using pytest

## Requirements
- Python 3.7+
- tkinter (usually included with Python)
- pytest (for running tests)
- Flask (for web mode)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/kirshamir/PythonProjectWithAI_1.git
   cd PythonProjectWithAI_1
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```
3. Install dependencies:
   ```sh
   pip install pytest
   pip install flask
   ```

## Usage
Run the game in console mode:
```sh
python main.py console
```

Run the game in GUI mode:
```sh
python main.py gui
```

Run the game in web mode:
```sh
python main.py web
```
Open http://127.0.0.1:5000/ in your browser to play.

## Running Tests
To run the automated tests:
```sh
pytest
```

## Project Structure
- `main.py` - Entry point, mode selection
- `tictactoe_base.py` - Abstract base class for shared game logic
- `tictactoe_console.py` - Console implementation
- `tictactoe_gui.py` - GUI implementation
- `tictactoe_web.py` - Web (Flask) implementation
- `templates/tictactoe.html` - HTML template for web mode
- `test_tictactoe_base.py` - Automated tests for core logic

## License
MIT
