from datetime import datetime
import random

# Original conf_data
conf_data = [
    {"confession post1": {"timestamp": "2024-01-28 14:30", "likes": 10, "comments": 2, "length": "thirty"}},
    {"Confession post2": {"timestamp": "2024-01-28 14:45", "likes": 9, "comments": 0, "length": "two"}},
    {"Confession post3": {"timestamp": "2024-01-28 14:50", "likes": 7, "comments": 1, "length": "twenty"}}
]

# Expand conf_data to 50 items with random data
for i in range(4, 51):  # Start from 4 to maintain the original 3 items
    post_name = f"Confession post{i}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    likes = random.randint(1, 20)
    comments = random.randint(0, 5)
    length = random.choice(["short", "medium", "long"])

    new_confession = {post_name: {"timestamp": timestamp, "likes": likes, "comments": comments, "length": length}}
    conf_data.append(new_confession)

# Print the expanded conf_data
for data in conf_data:
    print(data)