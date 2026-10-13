
"""
PYTHON OPERATORS
Description, examples, and practical uses
"""

# 1. ARITHMETIC OPERATORS
# Used for mathematical calculations.

a = 10
b = 3

print("ARITHMETIC OPERATORS")
print("Addition (+):", a + b)                 # 13
print("Subtraction (-):", a - b)              # 7
print("Multiplication (*):", a * b)           # 30
print("Division (/):", a / b)                 # 3.333...
print("Floor Division (//):", a // b)         # 3
print("Modulus (%):", a % b)                  # 1
print("Exponentiation (**):", a ** b)         # 1000

# @ is the matrix multiplication operator.
# Example: NumPy arrays A @ B


# 2. COMPARISON OPERATORS
# Compare values and return True or False.

print("\nCOMPARISON OPERATORS")
print("Equal (==):", a == b)                  # False
print("Not Equal (!=):", a != b)              # True
print("Greater Than (>):", a > b)             # True
print("Less Than (<):", a < b)                # False
print("Greater Than or Equal (>=):", a >= b)  # True
print("Less Than or Equal (<=):", a <= b)     # False


# 3. ASSIGNMENT OPERATORS
# Assign values or update existing variables.

print("\nASSIGNMENT OPERATORS")
x = 10
print("Assignment (=):", x)

x += 5
print("Add and Assign (+=):", x)              # 15

x -= 3
print("Subtract and Assign (-=):", x)         # 12

x *= 2
print("Multiply and Assign (*=):", x)         # 24

x /= 4
print("Divide and Assign (/=):", x)           # 6.0

x //= 2
print("Floor Divide and Assign (//=):", x)    # 3.0

x %= 2
print("Modulus and Assign (%=):", x)          # 1.0

x **= 3
print("Power and Assign (**=):", x)           # 1.0

# Other augmented assignments:
# &=, |=, ^=, >>=, <<=, @=
# These perform bitwise or matrix operations and assign the result.


# 4. LOGICAL OPERATORS
# Combine or reverse conditions.

print("\nLOGICAL OPERATORS")
age = 20
has_id = True

print("AND:", age >= 18 and has_id)           # True
print("OR:", age < 18 or has_id)              # True
print("NOT:", not has_id)                     # False


# 5. BITWISE OPERATORS
# Work on the binary representation of integers.

print("\nBITWISE OPERATORS")
p = 5   # Binary: 0101
q = 3   # Binary: 0011

print("AND (&):", p & q)                      # 1
print("OR (|):", p | q)                       # 7
print("XOR (^):", p ^ q)                      # 6
print("NOT (~):", ~p)                         # -6
print("Left Shift (<<):", p << 1)             # 10
print("Right Shift (>>):", p >> 1)            # 2


# 6. MEMBERSHIP OPERATORS
# Check whether a value exists in a collection.

print("\nMEMBERSHIP OPERATORS")
languages = ["Python", "C", "Java"]

print("'Python' in languages:", "Python" in languages)       # True
print("'Ruby' not in languages:", "Ruby" not in languages)   # True


# 7. IDENTITY OPERATORS
# Check whether two references point to the same object.

print("\nIDENTITY OPERATORS")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)          # True
print("list1 is list3:", list1 is list3)          # False
print("list1 is not list3:", list1 is not list3)  # True

# == compares values.
# is compares object identity.


# 8. CONDITIONAL EXPRESSION
# Select a value based on a condition.
# Often called the ternary operator.

print("\nCONDITIONAL EXPRESSION")
marks = 75
result = "Pass" if marks >= 40 else "Fail"
print("Result:", result)  # Pass


# 9. WALRUS OPERATOR (:=)
# Assign a value inside an expression.

print("\nWALRUS OPERATOR")
if (length := len("Python")) > 5:
    print("String length:", length)  # 6


# 10. OPERATOR PRECEDENCE
# Multiplication is evaluated before addition.

print("\nOPERATOR PRECEDENCE")
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(2 ** 3 ** 2)    # 512


# PRACTICAL EXAMPLE: STUDENT RESULT

print("\nSTUDENT RESULT")
student_marks = 85
passing_marks = 40

passed = student_marks >= passing_marks
grade = "Pass" if passed else "Fail"

print("Marks:", student_marks)
print("Passed:", passed)
print("Result:", grade)