#   Python Basic Algorithms

This project contains Python implementations of several basic algorithms, including prime number checking, string compression, and happy number calculations.

This project was developed as part of the 20606 course of the Open University.

The full assignment instructions are available in [Task 2.pdf](Task%202.pdf).

##   Table of Contents

* [Project Description](#project-description)
* [Algorithms Implemented](#algorithms-implemented)
    * [Prime Number Check](#prime-number-check)
    * [String Compression](#string-compression)
    * [Happy Number Calculation](#happy-number-calculation)
* [Usage](#usage)
* [Author](#author)

##   Project Description

The project provides Python functions to perform the following tasks:

* Determine if a given number is a prime number.
* Compress a string using run-length encoding.
* Calculate the sum of the squares of a number's digits and check if a number is a happy number.
* Count the number of happy numbers within a specified range.

##   Algorithms Implemented

###   Prime Number Check

The `is_prime(number)` function checks if a given number is prime by verifying that it is only divisible by 1 and itself[cite: 3]. The `max_prime()` function finds the largest prime number from a series of user-provided inputs[cite: 3].

###   String Compression

The `compression(input_string)` function compresses a string by replacing consecutive repeating characters with the character followed by the number of repetitions[cite: 4, 5].

###   Happy Number Calculation

The `sum_square(number)` function calculates the sum of the squares of a number's digits[cite: 8]. The `is_happy(number)` function determines if a number is a happy number, where the repeated sum of the squares of its digits eventually reaches 1[cite: 8, 9]. The `count_happy_numbers()` function counts the happy numbers within the range of 1 to 100[cite: 10].

##   Usage

To use the code in this repository:

1.  Ensure you have Python 3.x installed.
2.  Save the `mmn12.py` file.
3.  Run the script from the command line.
4.  Follow the prompts to provide input for the algorithms.

##   Author

Sagi Menahem.
