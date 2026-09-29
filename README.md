# DNA Sequence Analyzer

A simple Python command-line tool that validates a DNA sequence and reports its composition, GC/AT content, complement strand, and reverse sequence.

## Features

- Validates that the input contains only valid DNA bases (`A`, `T`, `G`, `C`)
- Counts the frequency of each base (A, T, G, C)
- Calculates GC content and AT content as percentages
- Generates the complement strand (A↔T, G↔C)
- Generates the reverse of the input sequence

## Project Structure

```
.
├── dna_analyzer.py    # Main script
└── README.md          # This file
```

> Note: if you named your script differently (for example `main.py` or `dna.py`), simply replace `dna_analyzer.py` with your file name in the commands below.

## Requirements

- **Python 3.6 or later** (any modern Python 3.x works)
- No third-party packages are required. The script uses only Python's standard library.

Check your Python version:

```bash
python --version
# or, depending on your system:
python3 --version
```

## Setup Instructions

Follow these steps from a clean machine.

### Step 1: Get the code

Clone the repository (or download and extract the project folder):

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### Step 2: (Optional but recommended) Create a virtual environment

This keeps the project isolated from your system Python. On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install dependencies

No installation is needed because the project has no external dependencies. If you later add packages, list them in a `requirements.txt` and install with:

bash
pip install -r requirements.txt


### Step 4: Configuration

No configuration is required. The script reads the DNA sequence interactively from the keyboard at runtime. If you want to analyze a different sequence, just enter it when prompted.

## How to Run

Run the script from the project folder:

bash
python dna_analyzer.py
# or:
python3 dna_analyzer.py


You will be prompted for input:


Enter DNA sequence:


Type or paste a DNA sequence (for example `ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG`) and press Enter.

### Example


Enter DNA sequence:ATGGCC
--- DNA Sequence Analyzer ---
DNA Sequence: ATGGCC
Length: 6
A: 1
T: 1
G: 2
C: 2
GC Content: 66.67 %
AT Content: 33.33 %
Complement: TACCGG
Reverse: CCGGTA


### Invalid input

If the sequence contains characters other than A, T, G, C (spaces, numbers, or lowercase letters are converted to uppercase first, so `atgc` is accepted), the program prints:


Invalid DNA sequence!

and exits without further output.

## Troubleshooting

- **`python: command not found`** — try `python3` instead, or install Python from [python.org](https://www.python.org/downloads/).
- **`No such file or directory`** — make sure you are inside the folder that contains the script (`cd` into it first).
- **Nothing happens after entering the sequence** — make sure you pressed Enter after pasting the sequence.
