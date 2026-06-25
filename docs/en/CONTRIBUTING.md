# Contributor Guidelines

Welcome! This document outlines the standards and design principles for the repository. By following these rules, you help keep the generators clean, reliable, and accessible to everyone.

## Table of Contents
- [Contributor Guidelines](#contributor-guidelines)
  - [Table of Contents](#table-of-contents)
  - [1. The "Unity" Rule for Generators](#1-the-unity-rule-for-generators)
    - [A. Output Filename](#a-output-filename)
    - [B. Mandatory Command-Line Arguments](#b-mandatory-command-line-arguments)
    - [C. Optional Standard Arguments](#c-optional-standard-arguments)
  - [2. Adding a New Game](#2-adding-a-new-game)
    - [Steps to Submit:](#steps-to-submit)
  - [3. Adding a New Language to an Existing Game](#3-adding-a-new-language-to-an-existing-game)
  - [4. Updating or Fixing Translations](#4-updating-or-fixing-translations)

---

## 1. The "Unity" Rule for Generators

Every game generator script must adhere to a strict CLI contract. This consistency ensures that any automated tool, wrapper script, or beginner user can interact with any game in the repository using the exact same interface pattern.

All game generator scripts must satisfy the following architectural rules:

### A. Output Filename
*   The script **must** output its generated LaTeX source file named exactly `game.tex`.
*   The generated file **must** be compiled using the `xelatex` engine.

### B. Mandatory Command-Line Arguments
Every script must implement at least the following arguments using `argparse`:

*   `--lang [CODE]`: Specify the language dictionary. 
    *   *Default*: Must default to `"en"`.
    *   *Constraint*: The code must match the global registry in [docs/LANGUAGES.md](../LANGUAGES.md).
*   `--seed [VALUE]`: Initialize the random number generator.
    *   *Requirement*: Setting a seed must produce a completely deterministic layout.
*   `--lang-list`: Scan the local `./lang` folder and list available translation files with their full names, then exit immediately.

### C. Optional Standard Arguments
*   `--words [PATH]`: If applicable, allows passing custom word files.
*   `--type [INT]`: Layout options. Use `1` for the default/standard layout.

---

## 2. Adding a New Game

When introducing a new print-and-play game, use the following structure:

```text
games/
└── [game-name]/
    ├── gen.py               # The Python generator script
    ├── README.md            # Language selector / Redirect
    ├── docs/
    │   ├── en/
    │   │   └── README.md    # Instructions on how to generate and play (English)
    │   └── pl/
    │       └── README.md    # Instructions on how to generate and play (Polish)
    └── lang/
        ├── en.json          # Default English config and vocabulary
        └── pl.json          # Polish config and vocabulary
```

### Steps to Submit:
1. Create your folder inside `games/`.
2. Write `gen.py` following the [Unity Rule](#1-the-unity-rule-for-generators).
3. Populate `lang/en.json` and other translation files.
4. Write clear setup and gameplay rules in the game's localized `README.md` documents.
5. Update the root-level `README.md` file to link to your new game directory.

---

## 3. Adding a New Language to an Existing Game

To add support for a new language to a game (for example, German `de`):

1. Verify that the language code is registered in [docs/LANGUAGES.md](../LANGUAGES.md). If not, register it first.
2. Navigate to `games/[game-name]/lang/`.
3. Create a new JSON file named `[code].json` (e.g., `de.json`).
4. Copy the key-value structures from `en.json` and translate the contents (such as UI text, labels, and word lists).
5. Ensure the `babel_lang` property in the JSON corresponds to the correct package name used by LaTeX's `babel` package.

---

## 4. Updating or Fixing Translations

If you spot a typo or want to improve a game's vocabulary:
1. Locate the language file inside `games/[game-name]/lang/[code].json`.
2. Modify the values inside the JSON file. Do not change the JSON keys, as this will break the parser in `gen.py`.
3. Test your changes locally by running the generator and compiling the resulting PDF:
   ```bash
   python gen.py --lang [code]
   xelatex game.tex
   ```

---
[← Back to Main Contributor Page](../../CONTRIBUTING.md) | [← Back to Repository Root](../../README.md)