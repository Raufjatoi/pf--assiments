from datetime import datetime
from collections import Counter

def analyze_confession_engagement(confession_data):
    def calculate_average_time(confession_data):
        total_length = sum(post['length'] for post in confession_data)
        return total_length / len(confession_data)

    # Function to extract hour from timestamp
    def extract_hour(timestamp):
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M").hour

    # Calculate average time spent per confession post
    average_time_spent = calculate_average_time(confession_data)

    # Extract hours and calculate overall engagement (likes + comments) for each hour
    hour_engagement = Counter()
    for post in confession_data:
        hour = extract_hour(post['timestamp'])
        engagement = post['likes'] + post['comments']
        hour_engagement[hour] += engagement

    # Identify the top 3 hours with the highest overall engagement
    most_engaged_hours = [hour for hour, _ in hour_engagement.most_common(3)]

    # Extract keywords and identify popular topics
    all_posts_text = ' '.join(post.get('content', '') for post in confession_data)
    # Assuming keywords are simply space-separated words
    all_keywords = all_posts_text.split()
    popular_topics = [topic for topic, _ in Counter(all_keywords).most_common(3)]

    return average_time_spent, most_engaged_hours, popular_topics

# Example usage:
confession_data = [
    {'timestamp': '2024-01-28 14:30', 'likes': 20, 'comments': 5, 'length': 150, 'content': 'study stress exam'},
    {'timestamp': '2024-01-28 18:45', 'likes': 30, 'comments': 8, 'length': 120, 'content': 'procrastination help'},
    {'timestamp': '2024-01-29 09:00', 'likes': 15, 'comments': 3, 'length': 180, 'content': 'friendship college life'}
]

average_time, engaged_hours, popular_topics = analyze_confession_engagement(confession_data)

print("Average time spent per confession post:", average_time)
print("Top 3 hours with the highest overall engagement:", engaged_hours)
print("Most common confession topics:", popular_topics)
