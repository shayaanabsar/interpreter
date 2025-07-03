
# Interpreter

A lightweight, educational interpreter designed to help you learn the basics of programming languages through a simple custom scripting language. It supports fundamental programming constructs such as variables, arithmetic and logical operations, input/output, conditionals, and loops.

---

## Features

- **Data Types**
  - String
  - Number
  - Boolean

- **Operators**
  - Arithmetic: `+`, `-`, `*`, `/`, `%`
  - Logical: `&&` (AND), `||` (OR), `!` (NOT)
  - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`

- **Input / Output**
  - `stdout` — output text or values to the console
  - `stdin` — read user input and store it in variables

- **Control Flow**
  - Conditional branching with `if` and `else`
  - Looping with `while`

---

## Language Syntax Overview

### Variables

Variables can be declared implicitly by assignment and hold any supported data type.

```plaintext
name = "Alice"
age = 30
isStudent = false
```

### Input and Output

- Output data using `stdout`:

```plaintext
stdout "Hello, World!"
stdout "Your age is: " + age
```

- Read input using `stdin` into a variable:

```plaintext
stdout "Enter your name: "
stdin name
```

### Conditionals

```plaintext
if age >= 18
    stdout "You are an adult."
else
    stdout "You are a minor."
```

### Loops

```plaintext
count = 0
while count < 5
    stdout "Count: " + count
    count = count + 1
```

---

## Example Program

```plaintext
stdout "Enter your name: "
stdin name
stdout "Hello, " + name + "!"

count = 0
while count < 3
    stdout "Count: " + count
    count = count + 1

if count == 3
    stdout "Loop finished."
```

---

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

Clone the repository:

```bash
git clone https://github.com/shayaanabsar/interpreter.git
cd interpreter
```

### Running the Interpreter

Run the interpreter with your script file as an argument:

```bash
python3 run.py your_script.txt
```

Replace `your_script.txt` with the path to your interpreter source file.

---

## Project Structure

- `run.py` — Main script to run the interpreter
- `interpreter.py` — Core interpreter logic (parsing, evaluating)
- `examples/` — Sample scripts demonstrating language features
- `README.md` — This documentation
