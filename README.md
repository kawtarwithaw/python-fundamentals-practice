# Python Fundamentals Practice

A collection of small Python scripts written while learning core fundamentals: loops, conditionals, dictionaries, string manipulation, file handling, and regular expressions.

These are learning exercises, not production tools — built and debugged from scratch as part of practicing Python basics.

## Scripts

### 🎯 Hangman Game
A command-line hangman game. Guess one letter at a time; the game tracks correct/incorrect guesses and reveals letter positions as you find them.

**Run:**
```bash
python hangman.py
```

**Concepts used:** `while` loops, lists, string indexing, conditionals

---

### 📈 Stock Portfolio Tracker
Calculates total investment value based on stock names and share counts entered by the user, using a hardcoded price dictionary.

**Run:**
```bash
python stock_tracker.py
```
Then enter stock tickers and share counts when prompted (comma-separated, e.g. `AAPL,TSLA,GOOGL` and `10,5,3`).

**Concepts used:** dictionaries, list comprehensions, input parsing, arithmetic

---

### 🗂️ JPG File Mover
Moves all `.jpg` files from one folder into a separate destination folder.

**Setup:** edit the `source_folder` and `destination_folder` variables near the top of the script to point to your own folders before running.

**Run:**
```bash
python jpg_mover.py
```

**Concepts used:** `os`, `shutil`, file system operations

---

### 📧 Email Extractor
Extracts all email addresses from a `.txt` file and saves them to a new file, using a regex pattern.

**Run:**
```bash
python email_extractor.py
```
You'll be prompted for the input filename and the output filename.

**Concepts used:** `re` (regular expressions), file reading/writing

---

## Notes
These scripts were built incrementally while learning — some early bugs (like index mismatches, greedy regex matches, and edge cases with duplicate values) were debugged along the way rather than avoided from the start. Known minor limitations (e.g. the email regex can occasionally include trailing punctuation) are left as-is for now.
