"""
Student: [Sagi Menahem]
ID: [208645937]
Assignment: Maman 12

This file contains solutions for all questions in Maman 12.
It includes functions for checking prime numbers (Q1),
compressing strings (Q2), and calculating happy numbers (Q3).
"""

# --- Constants ---

# Q1: Prime Numbers
FIRST_PRIME = 2  # The first prime number.
FIRST_ODD_DIVISOR = 3  # The first odd number to check as a divisor for primality.
DIVISOR_STEP = 2  # The step to take when checking odd divisors (to check only odd numbers).
TERMINATION_THRESHOLD = 1  # The value used to signal the end of user input for prime number checking.
DEFAULT_MAX_PRIME = 1  # The default value returned if no prime numbers are found in user input.

# Q2: String Compression
MIN_RUN_LENGTH_FOR_ENCODING = 2  # The minimum number of consecutive characters needed for compression encoding.

# Q3: Happy Numbers
HAPPY_NUMBER_TARGET = 1  # The target number in the happy number calculation sequence.
MAXIMUM_ITERATIONS = 10  # The maximum number of iterations allowed when checking for happy numbers.
HAPPY_COUNT_RANGE_START = 1  # The start of the range for counting happy numbers.
HAPPY_COUNT_RANGE_END = 100  # The end of the range for counting happy numbers.
BASE = 10  # The base for digit extraction.


# --- Question 1 Functions ---

def is_prime(number):
    """
    Checks if a number is prime.

    This function determines if a given number is a prime number
    (divisible only by 1 and itself).

    Args:
        number (int): The number to check. Must be greater than 1.

    Returns:
        bool: True if the number is prime, False if not.
    """

    # Handle the smallest prime number
    if number == FIRST_PRIME:
        return True
    # Handle even numbers greater than 2
    if number % FIRST_PRIME == 0:
        return False
    # Check for odd divisors up to the square root of number
    divisor = FIRST_ODD_DIVISOR
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += DIVISOR_STEP
    return True


def max_prime():
    """
    Finds the largest prime number from user input.

    This function reads numbers from the user until a number less than 1 is entered.
    It then returns the largest prime number that was entered.

    Returns:
        int: The largest prime number entered by the user.
             Returns 1 if no prime number greater than 1 was entered.
    """

    max_prime_found = DEFAULT_MAX_PRIME
    while True:
        input_str = input("Enter a natural number (or < 1 to stop): ")
        current_number = int(input_str)

        if current_number < TERMINATION_THRESHOLD:
            break  # Stop if the number is less than 1

        if current_number > 1:
            if is_prime(current_number):
                if current_number > max_prime_found:
                    max_prime_found = current_number  # Update the maximum prime found

    return max_prime_found


# --- Question 2 Function ---

def compression(input_string):
    """
    Compresses a string using run-length encoding.

    This function compresses a string by replacing consecutive repeating
    characters with the character followed by the number of repetitions.

    Args:
        input_string (str): The string to compress.

    Returns:
        str: The compressed string.
    """

    n = len(input_string)
    if n == 0:
        return ""  # Handle empty string

    compressed_string = ""
    i = 0  # Index for iterating through the string
    while i < n:
        current_char = input_string[i]
        count = 1  # Count occurrences of the current character
        j = i + 1  # Index to check next characters
        while j < n and input_string[j] == current_char:
            count += 1  # Increment count if next char is the same
            j += 1

        compressed_string += current_char  # Add the character to the compressed string
        if count >= MIN_RUN_LENGTH_FOR_ENCODING:
            compressed_string += str(count)  # Add the count if it meets the threshold
        i = j  # Move the index past the processed characters

    return compressed_string


# --- Question 3 Functions ---

def sum_square(number):
    """
    Calculates the sum of the squares of a number's digits.

    This function takes a number and calculates the sum of the squares
    of its individual digits.

    Args:
        number (int): The number to process. Assumed to be >= 0.

    Returns:
        int: The sum of the squares of the digits.
    """

    if number < 0:
        return 0  # Handle negative input

    sum_of_squares = 0
    temp_number = number  # Temporary variable to manipulate the number

    if temp_number == 0:
        return 0  # Handle zero input

    while temp_number > 0:
        digit = temp_number % BASE  # Get the last digit
        sum_of_squares += digit * digit  # Add the square of the digit to the sum
        temp_number //= BASE  # Remove the last digit

    return sum_of_squares


def is_happy(number):
    """
    Checks if a number is a happy number.

    A happy number is one where the repeated sum of the squares of its
    digits eventually reaches 1. This function checks if a number is happy.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is happy, False otherwise.
    """

    current_number = number  # Variable to store the current number in the sequence

    for _ in range(MAXIMUM_ITERATIONS):
        current_number = sum_square(current_number)  # Calculate the next number in the sequence
        if current_number == HAPPY_NUMBER_TARGET:
            return True  # It's a happy number!

    return False  # It's not a happy number


def count_happy_numbers():
    """
    Counts happy numbers in the range 1-100.

    This function counts the number of happy numbers within the
    range of 1 to 100 (inclusive).

    Returns:
        int: The total count of happy numbers in the range.
    """

    happy_count = 0  # Initialize the count of happy numbers

    for i in range(HAPPY_COUNT_RANGE_START, HAPPY_COUNT_RANGE_END + 1):
        if is_happy(i):
            happy_count += 1  # Increment the count if the number is happy

    return happy_count