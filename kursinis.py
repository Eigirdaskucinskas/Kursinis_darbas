import re
import os
from abc import ABC, abstractmethod


class HistoryManager:
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.filename = "conversion_history.txt"
        return cls._instance

    def save_result(self, input_val, output_val, mode):
        entry = f"[{mode}] Input: {input_val} -> Output: {output_val}\n"
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(entry)

    def show_history(self):
        print("\n--- 📜 CONVERSION HISTORY ---")
        if not os.path.exists(self.filename):
            print("No history found yet. Start converting!")
            return

        with open(self.filename, "r", encoding="utf-8") as file:
            content = file.readlines()
            if not content:
                print("The history file is empty.")
            else:
                for line in content:
                    print(line.strip())
        print("-----------------------------\n")

    def clear_history(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("🗑 History deleted.")


class Converter(ABC):

    @abstractmethod
    def convert(self, value):
        pass


class RomanToDecimal(Converter):

    def __init__(self):
        self._roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        # Standard Roman numeral validation pattern
        self._validation_regex = (
            r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        )

    def convert(self, roman: str) -> int:
        roman = roman.upper().strip()

        if not roman or not re.match(self._validation_regex, roman):
            raise ValueError(f"'{roman}' is not a valid Roman numeral.")

        total = 0
        prev_value = 0
        for char in reversed(roman):
            current_value = self._roman_map.get(char, 0)
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        return total


class DecimalToRoman(Converter):

    def __init__(self):
        self._decimal_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convert(self, number: int) -> str:
        if not (0 < number < 4000):
            raise ValueError("Decimal must be between 1 and 3,999.")

        res = []
        for val, symbol in self._decimal_map:
            while number >= val:
                res.append(symbol)
                number -= val
        return "".join(res)


def main():
    history = HistoryManager()
    converters = {
        "1": ("Roman to Decimal", RomanToDecimal()),
        "2": ("Decimal to Roman", DecimalToRoman())
    }

    while True:
        print("\n--- Roman & Decimal System ---")
        print("1. Roman to Decimal")
        print("2. Decimal to Roman")
        print("3. View History")
        print("4. Clear History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "4":
            history.clear_history()
        elif choice == "3":
            history.show_history()
        elif choice in converters:
            mode_name, converter = converters[choice]
            val = input(f"Enter value for {mode_name}: ")

            try:
                process_val = int(val) if choice == "2" else val
                result = converter.convert(process_val)
                print(f"✅ Result: {result}")
                history.save_result(val, result, mode_name)
            except ValueError as e:
                print(f"❌ Input Error: {e}")
            except Exception as e:
                print(f"🔥 Unexpected Error: {e}")
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()

