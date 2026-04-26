# Roman & Decimal Conversion System Coursework Report

## Introduction

The goal of this coursework is to design and implement a Python-based program that converts numbers between Roman numerals and decimal (Arabic) numbers while maintaining a history of user conversions. The program demonstrates object-oriented programming principles, and the Singleton design pattern.

The chosen topic is Converter for Roman and Decimal numbers, which provides users with two-way conversion functionality:

Roman numeral to decimal number
Decimal number to Roman numeral

The application is a command-line interface (CLI) tool that also stores previous conversions in a text file for future reference.

### How to Run the Program

Ensure Python is installed on your computer.
Save the code in a file, for example: roman_decimal_converter.py
Open a terminal or command prompt.
Run the program using:
python roman_decimal_converter.py

### How to Use the Program

After launching, the menu provides five options:

1. Roman to Decimal
2. Decimal to Roman
3. View History
4. Clear History
5. Exit

Users select an option, enter the required value, and the program displays the result while automatically saving it to history.

## Body / Analysis

### 1. Abstraction

Abstraction involves hiding the complex implementation details and showing only the necessary features of an object. It focuses on what an object does rather than how it does it.

``` python
class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass
```
### 2. Inheritance

Inheritance allows a class (child) to derive attributes and methods from another class (parent), promoting code reusability.

``` python
class RomanToDecimal(Converter):
...

class DecimalToRoman(Converter):
```

### 3. Polymorphism

Polymorphism (meaning "many forms") allows different classes to be treated as instances of the same general class through the same interface. In Python, this often means calling the same method name on different objects and getting different results.

``` python
result = converter.convert(process_val)
```

### 4. Encapsulation

Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class). It also involves restricting direct access to some components (data hiding).

``` python
class RomanToDecimal(Converter):
    def __init__(self):
        self._roman_map = {...} 
        self._validation_regex = r"..."
```

### 5. Singleton Pattern

The HistoryManager class ensures only one instance manages the history file throughout the application.

``` python
class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.filename = "conversion_history.txt"
        return cls._instance
```
This implementation prevents duplicate history managers and centralizes file operations such as saving, viewing, and deleting history.

### 6. Composition
In Composition, the "child" object is owned strictly by the "parent" object. If the parent is destroyed, the child is destroyed too. The child generally cannot exist meaningfully on its own.

``` python
class RomanToDecimal(Converter):
    def __init__(self):
        self._roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
```

## Results and Summary

Application was successfully created using OOP principles in python.

A Singleton design pattern was utilized through HistoryManager class to
manage the history file.

All four OOP pillars were applied.


6 unit test were written and all passed.

### Results

The program accurately converts Roman numerals such as XIV into 14 and decimal numbers such as 58 into LVIII.
Regular expression validation successfully blocks invalid Roman numeral patterns like IIII or VX.
The Singleton design pattern ensures that conversion history is managed consistently through a single file.
One major challenge was implementing strict Roman numeral validation rules due to formatting complexity.
Another challenge was designing a modular object-oriented structure while keeping the program simple and easy to use.

## Conclusions

This coursework successfully achieved the creation of a functional Roman & Decimal Conversion System using Python. The project demonstrates practical understanding of object-oriented programming through abstraction, inheritance, and design patterns.

The final result is a reliable command-line application capable of converting between numeral systems, validating user input, and storing conversion history. This work provides both educational and practical value.

## Future Prospects

Possible future improvements include:

Developing a graphical user interface (GUI)
Supporting extended Roman numeral systems beyond 3,999
Exporting conversion history to CSV or PDF
Adding support for additional numeral systems such as binary, hexadecimal, or octal

Overall, this coursework demonstrates successful software development, algorithm design, and problem-solving skills.
