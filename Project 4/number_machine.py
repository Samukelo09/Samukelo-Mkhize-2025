class NumberMachine:
    def process(self, number: int):
        #Runs all three transformations on the given number.
        print(f"--- Processing Number: {number} ---")
        print(f"1. Reversed:    {self.reverse_number(number)}")
        print(f"2. Sum of Digits: {self.sum_of_digits(number)}")
        print(f"3. +1 Transformed: {self.add_one_to_digits(number)}")
        print("-" * 30)

    def reverse_number(self, n: int) -> int:
        """
        Reverses an integer using math only.
        Logic: Extract the last digit and build a new number.
        """
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

    def sum_of_digits(self, n: int) -> int:
        # Calculates the sum of all digits.
        total = 0
        temp_n = n

        while temp_n > 0:
            digit = temp_n % 10
            total += digit
            temp_n = temp_n // 10
            
        return total

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

machine = NumberMachine()

# Test case 1: Standard sequence
machine.process(12345)

# Test case 2: Your specific example for the +1 logic
machine.process(12391)