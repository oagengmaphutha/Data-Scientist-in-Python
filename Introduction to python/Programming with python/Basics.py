# Python Basics Notes

Personal study notes covering the fundamentals of Python.

## Contents

1. [Introduction](#1-introduction)
2. [The print() Function](#2-the-print-function)
3. [Programming in Python](#3-programming-in-python)
4. [Python Syntax](#4-python-syntax)
5. [Computer Programs](#5-computer-programs)
6. [Code Comments](#6-code-comments)
7. [Arithmetic Operations](#7-arithmetic-operations)
8. [Review](#8-review--quick-cheat-sheet)

---

## 1. Introduction

- **Python** is a high-level, general-purpose, interpreted programming language.
- Created by Guido van Rossum, first released in 1991.
- Used for web development, data analysis, automation, AI/ML and scripting.
- Readable syntax, huge library ecosystem, runs on Windows, macOS and Linux.
- **Interpreted** means code runs line by line, with no separate compile step.
- Python files use the extension `.py`.

```python
# Check your version in a terminal
python --version
```

## 2. The print() Function

`print()` displays output on the screen.

```python
print("Hello, World!")
print(42)
print("Age:", 30)          # multiple values, separated by a space
```

- Text (a *string*) goes inside quotes: `"double"` or `'single'`.
- Numbers don't need quotes.
- Each `print()` ends with a new line by default.

| Option | Purpose | Example |
|---|---|---|
| `sep` | Change the separator | `print("a", "b", sep="-")` → `a-b` |
| `end` | Change what comes at the end | `print("Hi", end="!")` |
| `\n` | New line inside a string | `print("Line1\nLine2")` |
| `\t` | Tab inside a string | `print("A\tB")` |

## 3. Programming in Python

- **Programming** = writing step-by-step instructions a computer can follow.
- Workflow: write code → run it → read the output or errors → fix and repeat.
- **Interactive mode** (`>>>` prompt): type one line, get an instant result.
- **Script mode**: save code in a `.py` file and run `python filename.py`.

**Variables** store data under a name:

```python
name = "Oageng"
age = 25
price = 19.99
is_student = True
```

| Type | Meaning | Example |
|---|---|---|
| `str` | Text | `"hello"` |
| `int` | Whole number | `10` |
| `float` | Decimal number | `3.14` |
| `bool` | True or False | `True` |

- Check a type with `type(x)`.
- Variable names: letters, digits and underscores only; can't start with a digit; case-sensitive; can't be a reserved word like `if` or `for`.
- Convention: `snake_case` (e.g. `total_price`).

## 4. Python Syntax

**Syntax** is the set of rules for how code must be written.

- **Indentation matters.** Python uses indentation (normally 4 spaces) to define blocks.

```python
if 5 > 2:
    print("Five is greater than two")
```

- Python is **case-sensitive**: `print` works, `Print` does not.
- One statement per line.
- Quotes and brackets `()`, `[]`, `{}` must always be closed.

| Error | Usually caused by |
|---|---|
| `SyntaxError` | Typo, missing quote, bracket or colon |
| `IndentationError` | Wrong or inconsistent spacing |
| `NameError` | Using a variable that doesn't exist yet |
| `TypeError` | Mixing incompatible types, e.g. `"5" + 5` |

## 5. Computer Programs

- A **program** is a sequence of instructions that tells a computer what to do.
- Most programs follow: **Input → Process → Output**.
- Python runs a program **top to bottom**, one statement at a time.
- Building blocks: statements, variables, expressions, control flow (`if`, `for`, `while`) and functions.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

- `input()` always returns a **string**. Convert with `int()` or `float()` for numbers.

## 6. Code Comments

Comments are notes in the code that Python **ignores**.

```python
# This is a single-line comment
print("Hello")   # comment after code

"""
This is a multi-line string,
often used as a block comment.
"""
```

- Explain the *why*, not the obvious *what*.
- Keep comments short and up to date.
- Use `#` to temporarily disable a line while testing.

## 7. Arithmetic Operations

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | Division (always a float) | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 2` | `1` |
| `**` | Exponent | `2 ** 3` | `8` |

**Order of operations:** parentheses → exponents → `* / // %` (left to right) → `+ -` (left to right)

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```

**Assignment shortcuts**

```python
x = 10
x += 5    # 15
x -= 3    # 12
x *= 2    # 24
x /= 4    # 6.0
```

- `n % 2 == 0` checks if a number is even.
- Dividing by zero raises a `ZeroDivisionError`.
- Floats can have tiny precision errors; use `round(x, 2)` to tidy output.

## 8. Review – Quick Cheat Sheet

| Concept | Remember |
|---|---|
| Output | `print()` |
| Input | `input()` (returns a string) |
| Comment | `# ...` |
| Variable | `name = value` |
| Types | `str`, `int`, `float`, `bool` |
| Blocks | Defined by indentation (4 spaces) |
| Arithmetic | `+ - * / // % **` |
| Case | Python is case-sensitive |

**Mini practice program**

```python
# Calculate the total cost with 15% VAT
price = 200
vat = price * 0.15
total = price + vat
print("Total:", total)   # Total: 230.0
```

**Self-check questions**

1. What does `print(10 // 3)` output? *(3)*
2. What does `print(10 % 3)` output? *(1)*
3. Which symbol starts a comment? *(`#`)*
4. Why does `Print("Hi")` fail? *(Python is case-sensitive)*
5. What type does `input()` return? *(string)*

---

*Further reading: [W3Schools Python Tutorial](https://www.w3schools.com/python/)*
