# Codenames: PDF Generation & How to Play

Welcome to the print-and-play documentation for **Codenames**. This guide will explain how to configure and generate the game components, as well as how to play the game once printed.

---

## 1. How to Generate the Game PDF

The generation process consists of running a Python script to create a LaTeX file, and then compiling that file into a PDF.

### Prerequisites

1. **Python 3** (Refer to the general [Python Guide](../../../../docs/en/python.md) if you need help installing it).
2. **XeLaTeX** (Refer to the general [XeLaTeX Guide](../../../../docs/en/latex.md) or [Overleaf Guide](../../../../docs/en/overleaf.md)).

### Step 1: Run the Python Generator

Open your command-line interface, navigate to the `games/codenames/` directory, and run the generator:

```bash
python gen.py
```

This will create a file named `game.tex` in the directory.

### Customizing Generation (Command Line Arguments)

You can customize the generation using these optional arguments:

- `--lang CODE`: Select the language configuration inside `./lang/`. Examples:
  ```bash
  python gen.py --lang pl
  ```
- `--words PATH`: Use a custom `.txt` word list (one word per line) or flat `.json` string array:
  ```bash
  python gen.py --words custom_list.txt
  ```
- `--seed VALUE`: Provide a custom alphanumeric string to initialize the random generator. Using the same seed will always output the exact same grid and role arrangement:
  ```bash
  python gen.py --seed "mysecretseed123"
  ```
- `--type [1|2]`:
  - `1` (**Default**): Generates a full-sized landscape Spymaster sheet that directly colors the cells with the assigned words. No cutting is required for the key card; the Spymaster holds a copy of the actual word grid with background color overlays (Dark Gray for team A, Light Gray for team B, White for Neutrals, Black for Assassin).
  - `2`: Generates portrait layout keycards with two small 5x5 colored grids labeled **A**, **B**, **--**, and **X**. You must cut along the dashed line to hand each Spymaster their small key card.

### Step 2: Compile to PDF

Compile the generated `.tex` file using XeLaTeX:

```bash
xelatex game.tex
```

This generates `game.pdf`. Print page 1 for the player board, and page 2 for the Spymasters.

---

## 2. Game Rules (How to Play)

Codenames is a social word game played in two teams.

### Objective

The team that correctly identifies all their agents (words) on the board first wins the game.

### Roles & Component Setup

1.  **Divide into Teams**: Split players into two teams: **Team A (Dark Gray)** and **Team B (Light Gray)**.
2.  **Assign Spymasters**: Each team chooses one Spymaster. Both Spymasters must sit on the opposite side of the table from their teammates (**Field Operatives**).
3.  **Place the Main Board**: Print and place the **Main Board** (Page 1) in the center of the table.
    - _Note: The board features duplicate words rotated 180 degrees so players on both sides of the table can read them easily._
4.  **Spymaster Reference**: Give the Spymasters the Spymaster Sheet (Page 2).
    - **If generated using Type 1 (Default)**: Spymasters share a visual representation of the board where each word is directly overlaid with its secret color.
    - **If generated using Type 2**: Cut the spymaster sheet along the dashed line. Each spymaster gets a small abstract grid representing the layout.

### Understanding the Key Grid/Roles

The 25 words on the board belong to one of four categories:

- **Team A (Dark Gray / 9 Words)**: This team starts the game and has an extra word to find.
- **Team B (Light Gray / 8 Words)**: This team goes second and has 8 words to find.
- **Neutrals (White / 7 Words)**: Innocent bystanders. If guessed, the turn ends.
- **The Assassin (Black / 1 Word)**: A deadly trap. If guessed, the guessing team loses immediately.

---

### Gameplay Flow

The game is played in turns, starting with **Team A**.

#### Step A: The Spymaster's Clue

On their turn, the Spymaster gives their Field Operatives a clue consisting of exactly **one word** and **one number** (e.g., _"Ocean: 3"_).

- The **word** should relate to one or more of their team's words on the board.
- The **number** tells the Field Operatives how many words on the board relate to that clue.
- **Clue Restrictions**: The Spymaster must not use any part of the words currently visible on the board, translate words, or give physical clues.

#### Step B: The Field Operatives' Guesses

The Field Operatives discuss and attempt to identify the words.

1.  To guess, an operative must physically touch a word on the printed board.
2.  **Evaluate the Guess**:
    - **If it belongs to their own team**: The guess is successful. They can make another guess (up to the clue number + 1 bonus guess to resolve previous clues).
    - **If it belongs to the opposing team**: The turn ends immediately, and they have accidentally helped the other team.
    - **If it is Neutral**: The turn ends immediately.
    - **If it is the Assassin**: The game ends, and the guessing team loses immediately.
3.  Operatives can choose to stop guessing at any time during their turn.

### Winning the Game

The game ends immediately when:

- A team successfully uncovers all of their words. **They win.**
- A team touches the Assassin. **They lose immediately.**

## 3. Themes & Custom Word Lists

### Using Built-in Themes

You can generate a themed board by using the `--theme` argument. The themes automatically use words in your selected language.

**Available Themes:**
`star-wars`, `math`, `competitive-programming`, `minecraft`, `halloween`, `city-capitals`, `animals`, `biology`, `chemistry`, `school`, `computer`, `food`, `space`.

**Example command:**

```bash
python gen.py --lang en --theme star-wars
```

### Using Your Own Words

If you want to use a specific list of words (e.g., for a birthday or a specific school lesson):

1. Create a `.txt` file with one word or phrase per line.
2. Run the generator with the `--words` argument:

```bash
python gen.py --words my_custom_list.txt
```

_Note: Your list must contain at least 25 words._

---

[← Back to Codenames Main README](../../README.md) | [← Back to Repository Root](../../../README.md)
