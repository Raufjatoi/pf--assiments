from datetime import datetime
import random 
confession_data = [
    {'timestamp': '2024-01-28 14:30', 'likes': 20, 'comments': 5, 'length': 150, 'content': 'study stress exam'},
    {'timestamp': '2024-01-28 18:45', 'likes': 30, 'comments': 8, 'length': 120, 'content': 'procrastination help'},
    {'timestamp': '2024-01-29 09:00', 'likes': 15, 'comments': 3, 'length': 180, 'content': 'friendship college life'}
]

for i in range(20):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    likes = random.randint(1,100)
    comments = random.randint(1,20)
    length = random.choice(['short','medium','long'])
    content = random.choice(['entertainment', 'sports','study'])
    new_confession_data = {'timestamp': timestamp, 'likes': likes, 'comments': comments, 'length' : length , 'content': content}
    confession_data.append(new_confession_data)  
for data in confession_data: 

 print(data)



