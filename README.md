# 🎓 Student Data Collector

An educational command-line utility built in Python. The script serves as a practical demonstration of user input handling, explicit data type casting, basic arithmetic operations, and Python's internal memory management tracking.

## 📌 How It Works

1. **Input Collection**: Prompts the user for personal metrics.
2. **Type Conversion**: Converts raw inputs into specific Python primitives (`str`, `int`, `float`).
3. **Data Analysis**: Calculates the user's estimated birth year using a reference calendar year of 2026.
4. **Metadata Inspection**: References and outputs the underlying data types via `type()` and unique RAM storage locations using `id()`.

## ⚙️ Quick Start

### Running the Script

Ensure you have Python 3 installed, then execute the script directly from your terminal:

```bash
python main.py
```

### Sample Console Output

```text
Welcome to the Interactive Student Data Collector!

Please enter your name: Sam
Please enter your age: 20
Please enter your height in meters: 1.82
Please enter your favourite number: 42


Thank you! Here is the information we collected:


Your Name is : Sam (Type: <class 'str'>, Memory Address: 13998314112)

Your age is : 20 (Type: <class 'int'>, Memory Address: 13998305424)

Your height is : 1.82 (Type: <class 'float'>, Memory Address: 13998312912)

Your favourite number is: 42 (Type: <class 'int'>, Memory Address: 13998306128)


Your birth year is approximately: 2006 (based on your age of 20)


Thank you for using the Student Data Collector. Goodbye!
```

## 📝 Code Architecture Details

- **Type Enforcement**: Uses `int()` and `float()` wrappers to strictly type-cast console inputs.
- **Memory Profiling**: Leverages the built-in `id()` function to expose the variable's identity pointer.
- **Dynamic Strings**: Utilizes Python f-strings for clean variable interpolation.