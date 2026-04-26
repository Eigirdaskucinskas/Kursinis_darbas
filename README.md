# Roman & Decimal Conversion System Coursework Report

## 

The goal of this coursework is to design and implement a Python-based program that converts numbers between Roman numerals and decimal (Arabic) numbers while maintaining a history of user conversions. The program demonstrates object-oriented programming principles such as abstraction, inheritance, and the Singleton design pattern.

The chosen topic is a **Roman & Decimal Conversion System**, which provides users with two-way conversion functionality:
- Roman numeral to decimal number
- Decimal number to Roman numeral

The application is a command-line interface (CLI) tool that also stores previous conversions in a text file for future reference.

### How to Run the Program
1. Ensure Python is installed on your computer.
2. Save the code in a file, for example: `roman_decimal_converter.py`
3. Open a terminal or command prompt.
4. Run the program using:
   ```bash

   How to Use the Program

After launching, the menu provides five options:

Convert Roman numeral to decimal
Convert decimal to Roman numeral
View conversion history
Clear history
Exit the application

Users select an option, enter the required value, and the program displays the result while automatically saving it to history.



Body / Analysis

The program is structured using multiple classes to ensure modularity, maintainability, and code reusability.

1. Singleton Pattern for History Management

The HistoryManager class ensures only one instance manages the history file throughout the application.

class HistoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.filename = "conversion_history.txt"
        return cls._instance

This implementation prevents duplicate history managers and centralizes file operations such as saving, viewing, and deleting history.

2. Abstract Base Class for Conversion

The Converter abstract class defines a common structure for all converter types.

class Converter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

This ensures all subclasses implement their own convert() method.

3. Roman to Decimal Conversion

The RomanToDecimal class validates Roman numerals using regular expressions before conversion.

if not roman or not re.match(self._validation_regex, roman):
    raise ValueError(f"'{roman}' is not a valid Roman numeral.")

The algorithm processes numerals from right to left, adding or subtracting values based on Roman numeral rules.

4. Decimal to Roman Conversion

The DecimalToRoman class uses a descending value-symbol mapping.

for val, symbol in self._decimal_map:
    while number >= val:
        res.append(symbol)
        number -= val

This greedy algorithm ensures accurate Roman numeral generation.

5. Functional Requirements Achieved

The program successfully meets the following objectives:

Accurate Roman numeral validation
Bidirectional conversion
Exception handling for invalid inputs
Persistent conversion history
User-friendly interactive menu
Results
The program successfully converts valid Roman numerals (e.g., XIV → 14) and decimal numbers (e.g., 58 → LVIII) with high accuracy.
Regular expression validation effectively prevents invalid Roman numeral inputs such as IIII or VX.
The Singleton history manager ensures all conversions are consistently saved in one file without duplication issues.
One challenge was implementing correct Roman numeral validation rules, as Roman syntax contains strict formatting constraints.
Another challenge involved balancing modular object-oriented design with simplicity for command-line usability.
Conclusions

This coursework successfully achieved the development of a fully functional Roman & Decimal Conversion System using Python. The project demonstrates practical implementation of object-oriented concepts including abstraction, inheritance, and design patterns. The final program provides reliable number conversion, robust error handling, and history tracking.

The result of this work is an efficient educational tool for numeral system conversion. Future improvements could include:

A graphical user interface (GUI)
Support for larger Roman numeral formats
Exporting history to different file formats
Additional numeral systems such as binary or hexadecimal

Overall, this project highlights both software design skills and problem-solving in algorithm implementation.







   python roman_decimal_converter.py
