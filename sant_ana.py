#Develop a function that analyzes a social media post and returns the sentiment (positive, negative, neutral) and keywords used.
#Expand the function to identify emojis and potential trends.
"""
def comment_analyze (bad_comment,good_comment,neutral_comment):
    if comment in bad_comment:
        print ("your commment is negative :(  ")
    elif comment in good_comment:
        print("your comment is positive :)   ")
    elif comment in neutral_comment:
        print("your comment is neutral :\ ")
    else:
        print("cant understand the comment, can u define it ? ")

comment = input("enter ur comment :")
bad_comment = ["bad","not","not good","ugly","worst"]
good_comment = ["good","nice","yes","wow","cool","beautiful"]
neutral_comment = ["huh","what","idk"]

comment_analyze (bad_comment,good_comment,neutral_comment)
"""



















##

import re

def comment_analyze(comment):
    # Define lists of keywords for sentiment analysis
    bad_keywords = ["bad", "not", "not good", "ugly", "worst"]
    good_keywords = ["good", "nice", "yes", "wow", "cool", "beautiful"]
    neutral_keywords = ["huh", "what", "idk"]

    # Check for sentiment
    sentiment = None
    for word in comment.split():
        if word.lower() in bad_keywords:
            sentiment = "negative"
            break
        elif word.lower() in good_keywords:
            sentiment = "positive"
            break
        elif word.lower() in neutral_keywords:
            sentiment = "neutral"
            break

    if sentiment:
        print(f"Your comment is {sentiment} :) ")
    else:
        print("Unable to determine sentiment. Can you provide more context?")

    # Extract keywords
    keywords = [word for word in comment.split() if word.lower() in (bad_keywords + good_keywords + neutral_keywords)]

    if keywords:
        print("Keywords found:", keywords)
    else:
        print("No specific keywords identified.")

    # Identify emojis
    emojis = re.findall(r'[^\w\s,]', comment)
    
    if emojis:
        print("Emojis found:", emojis)
    else:
        print("No emojis found.")

    # Potential trends (simple check for hashtags)
    hashtags = re.findall(r'#\w+', comment)
    
    if hashtags:
        print("Trends identified:", hashtags)
    else:
        print("No trends identified.")

# Example usage
user_comment = input("Enter your comment: ")
comment_analyze(user_comment)






### import re 

"""
import re

text = "Hello, my email is john@example.com"

# Using re.search() to find the email address
match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

if match:
    print("Email found:", match.group())
else:
    print("No email found.")


"""