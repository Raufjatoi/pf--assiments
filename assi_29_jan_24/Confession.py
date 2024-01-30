from datetime import datetime

conf_data = [
    {"confession post1": {"timestamp": "2024-01-28 14:30", "likes": 10, "comments": 2, "length": "long"}},
    {"Confession post2": {"timestamp": "2024-01-28 14:45", "likes": 9, "comments": 0, "length": "medium"}},
    {"Confession post3": {"timestamp": "2024-01-28 14:50", "likes": 7, "comments": 1, "length": "short"}},
    {'Confession post4': {'timestamp': '2024-01-29 17:56', 'likes': 2, 'comments': 3, 'length': 'medium'}},
{'Confession post5': {'timestamp': '2024-01-29 17:56', 'likes': 6, 'comments': 3, 'length': 'long'}},
{'Confession post6': {'timestamp': '2024-01-29 17:56', 'likes': 15, 'comments': 4, 'length': 'medium'}},
{'Confession post7': {'timestamp': '2024-01-29 17:56', 'likes': 10, 'comments': 5, 'length': 'medium'}},
{'Confession post8': {'timestamp': '2024-01-29 17:56', 'likes': 19, 'comments': 1, 'length': 'short'}},
{'Confession post9': {'timestamp': '2024-01-29 17:56', 'likes': 8, 'comments': 3, 'length': 'short'}},
{'Confession post10': {'timestamp': '2024-01-29 17:56', 'likes': 18, 'comments': 1, 'length': 'long'}},
{'Confession post11': {'timestamp': '2024-01-29 17:56', 'likes': 16, 'comments': 2, 'length': 'short'}},
{'Confession post12': {'timestamp': '2024-01-29 17:56', 'likes': 11, 'comments': 1, 'length': 'medium'}},
{'Confession post13': {'timestamp': '2024-01-29 17:56', 'likes': 17, 'comments': 1, 'length': 'long'}},
{'Confession post14': {'timestamp': '2024-01-29 17:56', 'likes': 12, 'comments': 0, 'length': 'medium'}},
{'Confession post15': {'timestamp': '2024-01-29 17:56', 'likes': 1, 'comments': 4, 'length': 'medium'}},
{'Confession post16': {'timestamp': '2024-01-29 17:56', 'likes': 2, 'comments': 4, 'length': 'long'}},
{'Confession post17': {'timestamp': '2024-01-29 17:56', 'likes': 19, 'comments': 1, 'length': 'short'}},
{'Confession post18': {'timestamp': '2024-01-29 17:56', 'likes': 9, 'comments': 2, 'length': 'short'}},
{'Confession post19': {'timestamp': '2024-01-29 17:56', 'likes': 15, 'comments': 1, 'length': 'short'}},
{'Confession post20': {'timestamp': '2024-01-29 17:56', 'likes': 18, 'comments': 1, 'length': 'short'}},
{'Confession post21': {'timestamp': '2024-01-29 17:56', 'likes': 14, 'comments': 3, 'length': 'medium'}},
{'Confession post22': {'timestamp': '2024-01-29 17:56', 'likes': 2, 'comments': 2, 'length': 'long'}},
{'Confession post23': {'timestamp': '2024-01-29 17:56', 'likes': 3, 'comments': 4, 'length': 'long'}},
{'Confession post24': {'timestamp': '2024-01-29 17:56', 'likes': 9, 'comments': 4, 'length': 'long'}},
{'Confession post25': {'timestamp': '2024-01-29 17:56', 'likes': 12, 'comments': 0, 'length': 'short'}},
{'Confession post26': {'timestamp': '2024-01-29 17:56', 'likes': 2, 'comments': 3, 'length': 'medium'}},
{'Confession post27': {'timestamp': '2024-01-29 17:56', 'likes': 11, 'comments': 5, 'length': 'long'}},
{'Confession post28': {'timestamp': '2024-01-29 17:56', 'likes': 9, 'comments': 5, 'length': 'medium'}},
{'Confession post29': {'timestamp': '2024-01-29 17:56', 'likes': 19, 'comments': 4, 'length': 'short'}},
{'Confession post30': {'timestamp': '2024-01-29 17:56', 'likes': 20, 'comments': 0, 'length': 'medium'}},
{'Confession post31': {'timestamp': '2024-01-29 17:56', 'likes': 7, 'comments': 5, 'length': 'long'}},
{'Confession post32': {'timestamp': '2024-01-29 17:56', 'likes': 5, 'comments': 4, 'length': 'short'}},
]

def analyze_confession_engagement(confession_data):
    total_likes = 0
    total_comments = 0
    longest_post = 0
    longest_post_length = 0
    active_time = 0


    for data in conf_data:
        for post,details in data.items():
            total_likes += details["likes"]
            total_comments += details["comments"]
            if len(details["length"]) > longest_post_length:
                longest_post = post
                longest_post_length = len(details["length"])
    return total_likes, total_comments, longest_post

likes, comments, longest_post = analyze_confession_engagement(conf_data)
print(f"Total likes: {likes}")
print(f"Total comments: {comments}")
print(f"Longest post: {longest_post}")







