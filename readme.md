# Route Inspector

**Route Inspector** is a simple CLI tool to compare and visualize two vessel routes from an Excel file.

It automatically loads the first two sheets, interpolates their paths based on longitude, calculates the similarity between the routes using Euclidean and Mean Absolute Distance, and visualizes them.

---

## ✨ Features

- Automatically detects and compares the **first two sheets** in an Excel file
- Interpolates latitude values based on a **shared longitude range**
- Calculates route similarity:
  -  1. Euclidean Distance
  -  2. Mean Absolute Distance
- Displays **matplotlib-based route visualization**
- CLI-based input (compatible with `.exe` builds)

---

## 🚀 How to Use

### 1. Run the program

Using Python:

```bash
python main.py

Or using the compiled .exe file:
./main.exe