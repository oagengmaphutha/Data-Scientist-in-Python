# Variables and Data Types

## Contents

1. [Introduction](#1-introduction)
2. [Variables](#2-variables)
3. [Variable Names](#3-variable-names)
4. [Updating Variables](#4-updating-variables)
5. [Syntax Shortcuts](#5-syntax-shortcuts)
6. [Integers and Floats](#6-integers-and-floats)
7. [Conversion Between Types](#7-conversion-between-types)
8. [Strings](#8-strings)
9. [Escaping Special Characters](#9-escaping-special-characters)
10. [String Operations](#10-string-operations)
11. [Multi-line Strings](#11-multi-line-strings)
12. [Review](#12-review--quick-cheat-sheet)

---

## 1. Introduction

- A **variable** is a name that refers to a stored value.
- A **data type** describes what kind of value it is and what you can do with it.

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | `42` |
| `float` | Decimal number | `3.14` |
| `str` | Text | `"hello"` |
| `bool` | True or False | `True` |

- Python is **dynamically typed**: you don't declare a type. Python works it out from the value.
- Check a type with `type()`:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hi"))      # <class 'str'>
print(type(True))      # <class 'bool'>
```

## 2. Variables

- Create a variable with `=` (the **assignment operator**). The name goes on the left, the value on the right.
- There is no special keyword for creating a variable. It exists as soon as you assign to it.

```python
name = "Oageng"
age = 25
height = 1.75
is_student = True

print(name, age)
```

**Assigning multiple variables**

```python
a, b, c = 1, 2, 3     # different values
x = y = z = 0         # same value for all
```

**Swapping two values**

```python
a, b = b, a
```

## 3. Variable Names

**Rules (break these and you get an error)**

- Can contain letters, digits and underscores only.
- Cannot start with a digit.
- Cannot contain spaces or symbols like `-`, `$`, `@`.
- Cannot be a reserved keyword (`if`, `for`, `class`, `True`, etc.).
- Names are **case-sensitive**: `age`, `Age` and `AGE` are three different variables.

**Conventions (style, not rules)**

- Use `snake_case` for variable names: `total_price`, `first_name`.
- Choose descriptive names: `student_count` is better than `sc`.
- Constants are written in capitals by convention: `MAX_SPEED = 120`.
- Avoid names that shadow built-ins, like `list`, `str` or `print`.

```python
my_var = 1        # valid
_private = 2      # valid
var2 = 3          # valid

2var = 4          # invalid: starts with a digit
my-var = 5        # invalid: hyphen
class = 6         # invalid: reserved keyword
```

```python
import keyword
print(keyword.kwlist)   # shows all reserved words
```

## 4. Updating Variables

- Assigning a new value to an existing name **replaces** the old value.
- A variable can even change type, because Python is dynamically typed.

```python
score = 10
score = 15            # now 15
score = score + 5     # now 20 (uses the old value to calculate the new one)

x = 5
x = "five"            # allowed, but avoid it: confusing to read
```

- The right side is calculated **first**, then stored.
- Using a variable that has never been assigned gives a `NameError`.

## 5. Syntax Shortcuts

**Augmented assignment operators**

| Shortcut | Same as |
|---|---|
| `x += 3` | `x = x + 3` |
| `x -= 3` | `x = x - 3` |
| `x *= 3` | `x = x * 3` |
| `x /= 3` | `x = x / 3` |
| `x //= 3` | `x = x // 3` |
| `x %= 3` | `x = x % 3` |
| `x **= 3` | `x = x ** 3` |

```python
count = 10
count += 1      # 11
count *= 2      # 22
```

- Python has **no** `++` or `--`. Use `x += 1` or `x -= 1`.
- `+=` also works on strings: `msg += "!"`.

## 6. Integers and Floats

**Integers (`int`)**: whole numbers, positive or negative, with no size limit.

```python
a = 10
b = -3
big = 1_000_000      # underscores make large numbers readable
```

**Floats (`float`)**: numbers with a decimal point.

```python
pi = 3.14
temp = -0.5
sci = 2.5e3          # scientific notation = 2500.0
```

**Mixing them**

- `int` and `float` in one calculation gives a `float`.
- `/` always returns a `float`, even for whole results.
- `//` gives the floor (rounded-down) result.

```python
print(5 + 2.0)    # 7.0
print(10 / 2)     # 5.0
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 10)    # 1024
```

**Useful functions**

| Function | Purpose | Example |
|---|---|---|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `round(x, n)` | Round to n decimals | `round(3.14159, 2)` → `3.14` |
| `min()` / `max()` | Smallest / largest | `max(3, 9, 5)` → `9` |
| `pow(x, y)` | Power | `pow(2, 3)` → `8` |

**Watch out:** floats are stored approximately, so tiny errors appear.

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

## 7. Conversion Between Types

Converting a value from one type to another is called **type conversion** (or **casting**).

| Function | Converts to | Example | Result |
|---|---|---|---|
| `int()` | Integer | `int("42")` | `42` |
| `int()` | Integer | `int(3.9)` | `3` (cuts off decimals, doesn't round) |
| `float()` | Float | `float("2.5")` | `2.5` |
| `float()` | Float | `float(7)` | `7.0` |
| `str()` | String | `str(100)` | `"100"` |
| `bool()` | Boolean | `bool(0)` | `False` |

```python
age = input("Age: ")       # always a string
age = int(age)             # convert before doing maths
print(age + 1)
```

**Combining text and numbers**

```python
print("Age: " + str(25))   # must convert the number to a string
print("Age:", 25)          # commas in print() do it for you
```

**Things that fail**

```python
int("hello")    # ValueError
int("3.5")      # ValueError (convert to float first: int(float("3.5")))
"5" + 5         # TypeError
```

**Truthy and falsy values**

- `bool()` gives `False` for: `0`, `0.0`, `""` (empty string), `None`, and empty collections.
- Almost everything else is `True`, including the string `"False"`.

## 8. Strings

- A **string** is a sequence of characters (text) inside quotes.
- Use single `'...'` or double `"..."` quotes. They work the same.

```python
first = "Oageng"
greeting = 'Hello'
empty = ""
```

- Use the other kind of quote to include a quote inside:

```python
print("It's a nice day")
print('She said "hi"')
```

**Indexing**: each character has a position, starting at **0**. Negative numbers count from the end.

```python
word = "Python"
print(word[0])     # P
print(word[3])     # h
print(word[-1])    # n
```

**Slicing**: `[start:stop]`, where stop is not included.

```python
print(word[0:2])   # Py
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::-1])  # nohtyP (reversed)
```

- Strings are **immutable**: you can't change one character in place. You create a new string instead.

```python
word[0] = "J"      # TypeError
word = "J" + word[1:]   # works: "Jython"
```

## 9. Escaping Special Characters

An **escape character** is a backslash `\` followed by a character. It lets you include characters that would otherwise be hard to type or would break the string.

| Code | Result |
|---|---|
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |
| `\n` | New line |
| `\t` | Tab |

```python
print("She said \"hello\"")
print('It\'s fine')
print("C:\\Users\\Oageng")
print("Line 1\nLine 2")
print("Name\tAge")
```

**Raw strings** ignore escapes. Put `r` before the quote (handy for file paths).

```python
print(r"C:\new\folder")    # C:\new\folder
```

## 10. String Operations

**Concatenation and repetition**

```python
print("Hello" + " " + "World")   # Hello World
print("ha" * 3)                  # hahaha
```

**Length and membership**

```python
text = "Python"
print(len(text))          # 6
print("Py" in text)       # True
print("z" not in text)    # True
```

**Common string methods** (they return a new string; the original doesn't change)

| Method | Purpose | Example | Result |
|---|---|---|---|
| `.upper()` | All capitals | `"hi".upper()` | `"HI"` |
| `.lower()` | All lowercase | `"HI".lower()` | `"hi"` |
| `.title()` | Capitalise each word | `"hello world".title()` | `"Hello World"` |
| `.strip()` | Remove outer spaces | `"  hi  ".strip()` | `"hi"` |
| `.replace(a, b)` | Replace text | `"cat".replace("c", "b")` | `"bat"` |
| `.split()` | Break into a list | `"a b c".split()` | `["a", "b", "c"]` |
| `.find(x)` | Index of first match (`-1` if none) | `"hello".find("l")` | `2` |
| `.count(x)` | Count occurrences | `"banana".count("a")` | `3` |
| `.startswith(x)` | Check the start | `"hello".startswith("he")` | `True` |

**f-strings** (the cleanest way to put variables in text)

```python
name = "Oageng"
age = 25
print(f"{name} is {age} years old")
print(f"Next year: {age + 1}")
print(f"Price: {19.5:.2f}")      # 2 decimal places -> 19.50
```

## 11. Multi-line Strings

- Use **triple quotes** (`"""` or `'''`) for text over several lines. Line breaks are kept.

```python
message = """Dear Sir,

Thank you for your help.

Regards,
Oageng"""

print(message)
```

- Handy for long text, formatted output and docstrings.
- An alternative is `\n` inside a normal string:

```python
print("Line 1\nLine 2\nLine 3")
```

## 12. Review – Quick Cheat Sheet

| Concept | Remember |
|---|---|
| Create a variable | `name = value` |
| Check type | `type(x)` |
| Naming | Letters, digits, `_`; no leading digit; case-sensitive; `snake_case` |
| Update | `x = x + 1` or `x += 1` |
| No `++` | Use `+= 1` |
| Whole numbers | `int` |
| Decimals | `float` (`/` always returns a float) |
| Convert | `int()`, `float()`, `str()`, `bool()` |
| Indexing | Starts at `0`; `-1` is the last |
| Slicing | `s[start:stop]` (stop excluded) |
| Escapes | `\n`, `\t`, `\"`, `\\` |
| Strings | Immutable |
| Format text | `f"{variable}"` |
| Multi-line | `"""..."""` |

**Practice**

```python
name = "Oageng"
price = 200
quantity = 3
total = price * quantity
print(f"{name} owes R{total:.2f}")   # Oageng owes R600.00
```

**Self-check questions**

1. Is `2nd_place` a valid variable name? *(No, it starts with a digit)*
2. What does `int(7.9)` return? *(7)*
3. What is `type(10 / 2)`? *(float)*
4. What does `"Python"[1:4]` return? *(yth)*
5. What does `"ab" * 3` return? *(ababab)*
6. Why does `"Age: " + 25` fail? *(Can't add a str and an int. Use `str(25)`)*
7. What does `x += 5` do? *(Adds 5 to x and stores the result back in x)*

---

*Further reading: [W3Schools Python Variables](https://www.w3schools.com/python/python_variables.asp) and [Python Strings](https://www.w3schools.com/python/python_strings.asp)*
