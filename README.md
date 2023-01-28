#Documentation

##Data Types
- String
- Number 
- Boolean

##Arithmetic Operators
- \+
- \-
- \\
- \*
- % (modulo)

##Logical Operators
- && (And)
- || (Or)
- ! (Not)

##Comparators
- ==
- !=
- \>
- <
- \>=
- <=

## Input and Output
Use 'stdout' to output data.

    stdout "Hello, World!"

Initialise a variable with the type you want to be entered and then use 'stdin' to input data.

    name = ""
    stdin name

The above will get a string input from the user and store the value in the variable 'name'.

    age = 0
    stdin age

The above will get a Number input from the user and store the value in the variable 'name'.

## Conditionals
### If-else 
    if (age >= 18) {
        stdout "You are an adult"
    } 
    else {
        if (age >= 13) {
            stdout "You are a teenager"
        } 
        else {
            stdout "You are a child"
        }
    }

Note: the parenthesis around the condition are not required.

### Switch
    switch (operator) {
        case "+" {
            output = a + b
        }
        case "-" {
            output = a - b
        }
        case "/" {
            output = a / b
        }
        case "*" {
            output = a * b
        }
        case default {
            output = "Operator not recognised"
        }
    }

##Loops
###While
    moreData = "y"
    while (moreData == "y") {
        stdin data
        stdout "Do you want to add more data? (y/n):"
        stdin moreData
    }

## Functions
###Definitions
Functions can be defined using the 'func' keyword.
    
    func isEven(num) {
        if (n % 2 == 0) {
            stdout "Yes"
        }
        else {
            stdout "No"
        }
    }
