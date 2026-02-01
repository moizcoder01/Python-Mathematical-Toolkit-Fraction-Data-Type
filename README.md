# Python Mathematical Toolkit: Fraction Data Type

A custom Python implementation of a **Fraction** data type that allows users to perform standard arithmetic operations on rational numbers. This project demonstrates Object-Oriented Programming (OOP) principles, specifically **Operator Overloading**, to make custom objects behave like native Python numbers.

## 🚀 Key Features

* **Operator Overloading:** Uses Python "Magic Methods" (`__add__`, `__sub__`, `__mul__`, `__truediv__`) to allow natural mathematical syntax between Fraction objects.
* **Input Validation:** Robust error handling using `try...except` blocks to catch malformed inputs (e.g., missing slashes or non-integer values).
* **Zero Division Safety:** Includes a critical logic check to ensure denominators are never zero, preventing runtime crashes.
* **Interactive CLI:** A continuous loop-based Command Line Interface (CLI) that allows users to perform multiple calculations without restarting the script.

## 📐 Mathematical Logic

The class calculates fractions using the following standard formulas:

| Operation | Mathematical Formula |
| :--- | :--- |
| **Addition** | (a/b) + (c/d) = (ad + bc) / (bd) |
| **Subtraction** | (a/b) - (c/d) = (ad - bc) / (bd) |
| **Multiplication** | (a/b) * (c/d) = (ac) / (bd) |
| **Division** | (a/b) / (c/d) = (ad) / (bc) |



## 💻 How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/moizcoder01/Python-Mathematical-Toolkit-Fraction-Data-Type.git)
    ```
2.  **Run the Script:**
    ```bash
    python "Datatype creation 1.py"
    ```
3.  **Follow the Prompts:**
    * Select an operation (1-4).
    * Enter fractions in the format `a/b` (e.g., `1/2`).
    * View the result and continue or exit.
