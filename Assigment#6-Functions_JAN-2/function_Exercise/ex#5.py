#Create a function that checks if a given word is a palindrome. Test the function with words like "level" and "python.“
def palindrome():
    w = input("Enter a word : ")
    r = w[::-1]
    if w == r :
        print("Word is palindrome ")
    else:
        print("Word is not palindrome ")

palindrome()