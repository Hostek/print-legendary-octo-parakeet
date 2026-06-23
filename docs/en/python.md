# Python: Installation and Execution

Python is a versatile and beginner-friendly programming language. Below you will find steps to install it and run your first script.

---

## 1. Installing Python

### Windows
1. Visit the official website: [python.org/downloads](https://www.python.org/downloads/).
2. Click the yellow button marked **Download Python [version]**.
3. Run the downloaded `.exe` installer.
4. **Important:** At the bottom of the installer window, check the box that says **"Add python.exe to PATH"**. If you skip this, your system will not recognize Python commands in the terminal.
5. Click **Install Now** and wait for the process to complete.

### macOS
1. The easiest method is to use the official installer from [python.org/downloads](https://www.python.org/downloads/).
2. Download the installer package for macOS (`.pkg`) and follow the on-screen steps.
3. *Alternative via Homebrew:* If you use a terminal and have Homebrew installed, run:
   ```bash
   brew install python
   ```

### Linux (Ubuntu/Debian)
Python is typically pre-installed on most Linux distributions. To ensure you have the required packages, open your terminal and run:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 2. How to Run a Python Script

Let's write and run a simple "Hello World" program to verify the installation.

### Step 1: Create the script file
1. Open a plain text editor (e.g., Notepad on Windows, TextEdit on macOS, or Gedit on Linux).
2. Enter the following line of code:
   ```python
   print("Hello from Python!")
   ```
3. Save the file as `script.py` (make sure the extension is `.py` and not `.txt`). Save it to a convenient location, such as your Desktop.

### Step 2: Execute the script

#### Windows (Command Prompt or PowerShell)
1. Open the Start menu, type `cmd`, and open the **Command Prompt**.
2. Navigate to the folder where you saved the file. For example:
   ```cmd
   cd Desktop
   ```
3. Run the script by typing:
   ```cmd
   python script.py
   ```
4. You should see `Hello from Python!` printed in the console.

#### macOS & Linux (Terminal)
1. Open the **Terminal**.
2. Navigate to the folder containing your script:
   ```bash
   cd Desktop
   ```
3. Run the script using the `python3` command:
   ```bash
   python3 script.py
   ```