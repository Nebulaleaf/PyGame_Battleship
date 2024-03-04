# Battleship Game

This project is a Python implementation of the classic Battleship game. 
The plan was to enhance it with a graphical interface using Pygame, but that will be tackled later on.

## Game Overview

In this implementation of Battleship, players set up their ships on a grid and then take turns guessing the locations of their opponent's ships. The goal is to sink all of the opponent's ships before they sink all of yours. This version brings an interactive console-based interface to life, enhanced with colorful output thanks to the Colorama library, making the gameplay experience more engaging and visually appealing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python (3.x or higher recommended)
- Pip (Python package manager)

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
    ```bash
    git clone https://github.com/Nebulaleaf/PyGame_Battleship.git
    ```

2. Navigate to the project directory:
    ```bash
    cd PyGame_Battleship
    ```

3. Create a virtual environment:
    - On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python src/main.py
    ```

## Structure

The project is structured as follows:

- `assets/`: Assets related to the project.
- `docs/`: Documentation related to the project.
- `src/`: Contains the source code for the game.
  - `original_code/`: Contains the original code of the previous version (https://github.com/smue-smue/PyLadies_Battleship)
- `tests/`: Test scripts for the game.
- `venv/`: Virtual environment for managing dependencies.


## Authors

- **Sandra** - [smue-smue](https://github.com/smue-smue)
- **Alexandra** - [Nebulaleaf](https://github.com/Nebulaleaf)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgement
