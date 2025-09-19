# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while loop) to control rows
while row < size:
    # Inner loop (for loop) to control columns
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Print a newline after finishing a row
    row += 1  # Move to the next row
