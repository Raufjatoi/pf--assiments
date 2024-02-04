from datetime import datetime
from collections import Counter

data = [
{'timestamp': '2024-01-28 14:30', 'likes': 20, 'comments': 5, 'length': 150, 'content': 'study stress exam'},
{'timestamp': '2024-01-28 18:45', 'likes': 30, 'comments': 8, 'length': 120, 'content': 'procrastination help'},
{'timestamp': '2024-01-29 09:00', 'likes': 15, 'comments': 3, 'length': 180, 'content': 'friendship college life'},
{'timestamp': '2024-01-31 17:00', 'likes': 82, 'comments': 7, 'length':  90, 'content': 'entertainment'},
{'timestamp': '2024-01-31 17:21', 'likes': 72, 'comments': 11, 'length': 100, 'content': 'entertainment'},
{'timestamp': '2024-01-31 18:57', 'likes': 6, 'comments': 5, 'length': 110, 'content': 'study'},
{'timestamp': '2024-01-31 16:57', 'likes': 86, 'comments': 12, 'length': 120, 'content': 'study'},
{'timestamp': '2024-01-31 15:57', 'likes': 83, 'comments': 12, 'length': 100, 'content': 'entertainment'},
{'timestamp': '2024-01-31 17:22', 'likes': 75, 'comments': 5, 'length': 80, 'content': 'entertainment'},
{'timestamp': '2024-01-31 17:52', 'likes': 39, 'comments': 13, 'length': 70, 'content': 'study'},
{'timestamp': '2024-01-31 17:00', 'likes': 83, 'comments': 16, 'length': 120, 'content': 'sports'},
{'timestamp': '2024-01-31 20:57', 'likes': 75, 'comments': 12, 'length': 180, 'content': 'entertainment'},
{'timestamp': '2024-01-31 22:57', 'likes': 78, 'comments': 13, 'length': 110, 'content': 'sports'},
{'timestamp': '2024-01-31 12:57', 'likes': 81, 'comments': 1, 'length': 130, 'content': 'study'},
{'timestamp': '2024-01-31 13:57', 'likes': 52, 'comments': 8, 'length': 125, 'content': 'entertainment'},
{'timestamp': '2024-01-31 11:57', 'likes': 98, 'comments': 14, 'length': 112, 'content': 'entertainment'},
{'timestamp': '2024-01-31 13:57', 'likes': 2, 'comments': 20, 'length': 65, 'content': 'study'},
{'timestamp': '2024-01-31 17:07', 'likes': 49, 'comments': 4, 'length': 122, 'content': 'sports'},
{'timestamp': '2024-01-31 12:57', 'likes': 75, 'comments': 17, 'length': 123, 'content': 'study'},
{'timestamp': '2024-01-31 12:57', 'likes': 41, 'comments': 1, 'length': 140, 'content': 'sports'},
{'timestamp': '2024-01-31 13:57', 'likes': 72, 'comments': 10, 'length': 144, 'content': 'study'},
{'timestamp': '2024-01-31 13:57', 'likes': 94, 'comments': 20, 'length': 153, 'content': 'entertainment'},
{'timestamp': '2024-01-31 12:57', 'likes': 18, 'comments': 5, 'length': 122, 'content': 'entertainment'}
]
def analyze_engagement(data):
    def avg_time (data):
        total_length = sum(p['length'] for p in data)
        return total_length / len(data)
    def extract_hour(timestamp):
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M").hour
    
    avg_time_spend = avg_time(data)
    
    hour_engagement = Counter()
    for p in data:
        hour = extract_hour(p['timestamp'])
        engagement = p['likes'] + p['comments']
        hour_engagement[hour] += engagement
    
    most_engaged_hours = [hour for hour, _ in hour_engagement.most_common(3)]
    return avg_time_spend,most_engaged_hours
avg_time_spend,most_engaged_hours = analyze_engagement(data)  

print(f"avg time was {round(avg_time_spend,0)} mins ")
print(f"most common hours were {most_engaged_hours}")

    