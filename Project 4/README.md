# NumberMachine — Code Explanation

This Python class performs three different mathematical transformations on integers using only arithmetic operations, without converting numbers to strings.

---

## Class Overview: `NumberMachine`

The class is designed to:

- **Reverse** the digits of a number mathematically.
- **Sum** all digits of a number.
- **Transform** each digit by adding 1 (with wrap‑around: 9 becomes 0).
- Display all three transformations in a clean, formatted way.

---

## Code Breakdown

### 1. Main Processing Method

```python
def process(self, number: int):
    # Runs all three transformations on the given number.
    print(f"--- Processing Number: {number} ---")
    print(f"1. Reversed:    {self.reverse_number(number)}")
    print(f"2. Sum of Digits: {self.sum_of_digits(number)}")
    print(f"3. +1 Transformed: {self.add_one_to_digits(number)}")
    print("-" * 30)
```

- Accepts an integer and runs all three transformations.
- Prints formatted results for easy reading.

---

### 2. Reverse Number Method

```python
def reverse_number(self, n: int) -> int:
    reversed_n = 0
    temp_n = n  # Create a copy so we don't destroy the original 'n'

    while temp_n > 0:
        # Get the last digit (e.g., 12345 % 10 = 5)
        digit = temp_n % 10
        
        # Shift the existing reversed number to the left and add the new digit
        # (e.g., 5 becomes 50, then add 4 -> 54)
        reversed_n = (reversed_n * 10) + digit
        
        # Remove the last digit from the original number (e.g., 12345 // 10 = 1234)
        temp_n = temp_n // 10
        
    return reversed_n
```

**How it works:**

- Extracts digits from right to left using % 10.
- Builds the reversed number by shifting left (* 10) and adding the digit.
- Removes processed digits using integer division (// 10).

Example: `12345` → `54321`

---

### 3. Sum of Digits Method

```python
def sum_of_digits(self, n: int) -> int:
    # Calculates the sum of all digits.
    total = 0
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        total += digit
        temp_n = temp_n // 10
        
    return total
```

**How it works:**

- Extracts each digit using modulus.
- Accumulates the sum in the `total` variable.

Example: `12345` → `1+2+3+4+5 = 15`

---

### 4. Add One to Digits Method

```python
def add_one_to_digits(self, n: int) -> int:
    # Adds 1 to each digit. If a digit is 9, it becomes 0.
    new_number = 0
    multiplier = 1  # Tracks position: 1s, 10s, 100s, etc.
    temp_n = n

    while temp_n > 0:
        digit = temp_n % 10
        
        # Add 1 and wrap around 9 -> 0 using modulus
        new_digit = (digit + 1) % 10
        
        # Place the digit in the correct position
        new_number = new_number + (new_digit * multiplier)
        
        # Move to the next digit and update position multiplier
        temp_n = temp_n // 10
        multiplier *= 10
        
    return new_number
```

**How it works:**

- Uses `(digit + 1) % 10` to add 1 with wrap‑around.
- `multiplier` tracks the digit position (ones, tens, hundreds…)e.

Example: 

- `12345` → `23456`
- `12391` → `23402` (9+1 wraps to 0)

---

## Summary

This script demonstrates:

- Pure mathematical digit manipulation without string conversion.
- Modular arithmetic for digit extraction and wrap‑around logic.
- Algorithmic thinking for number transformation.

- Clean, well‑documented code with single‑responsibility methods.
