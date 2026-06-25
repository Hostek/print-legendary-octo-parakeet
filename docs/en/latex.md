# XeLaTeX: Local Installation and Compilation

XeLaTeX is an extension of the LaTeX typesetting system that allows you to use your operating system's native fonts (such as Arial or Times New Roman) and natively supports Unicode/UTF-8 encoding.

---

## 1. Installing XeLaTeX

To use XeLaTeX locally, you need to install a TeX distribution.

### Windows
**MiKTeX** is a recommended and easy-to-use option.
1. Download the installer from [miktex.org/download](https://miktex.org/download).
2. Run the installer and follow the wizard. It is recommended to choose *Yes* for the option *"Install missing packages on-the-fly"* to automate package management.

### macOS
**MacTeX** is the standard distribution for macOS.
1. Download the installer package from [tug.org/mactex](https://tug.org/mactex/).
2. Open the `.pkg` file and complete the installation process.

### Linux (Ubuntu/Debian)
Install the TeX Live packages through your package manager:
```bash
sudo apt update
sudo apt install texlive-xetex
```

---

## 2. Compiling a XeLaTeX Document

### Step 1: Create your document
1. Create a plain text file named `document.tex`.
2. Paste the following example code inside:
   ```latex
   \documentclass{article}
   \usepackage{fontspec} % Required by XeLaTeX to load system fonts
   \setmainfont{Arial}    % You can replace this with any system font

   \begin{document}
   Hello World! This document is compiled using the XeLaTeX engine.
   \end{document}
   ```

### Step 2: Compile via Command Line (Windows, macOS, Linux)
1. Open your terminal (Command Prompt on Windows / Terminal on macOS or Linux).
2. Go to the directory where your file is saved, for example:
   ```bash
   cd Desktop
   ```
3. Run the XeLaTeX compiler:
   ```bash
   xelatex document.tex
   ```
4. Once the process is complete, a PDF file named `document.pdf` will be created in the same folder.

---
[← Back to Beginner's Guide](README.md)