#Write a Python program that generates a list of squares for numbers 1 to 10.
# Create a function to filter out odd squares and return a new list with only even squares.
def generate_squares():
    squares = []
    for i in range(1, 11):
        squares.append(i ** 2)
    return squares

def filter_even_squares(squares):
    even_squares = [square for square in squares if square % 2 == 0]
    return even_squares

# Generate a list of squares
squares_list = generate_squares()

# Print the list of squares
print("List of Squares:", squares_list)

# Filter out odd squares
even_squares_list = filter_even_squares(squares_list)

# Print the list of even squares
print("List of Even Squares:", even_squares_list)
