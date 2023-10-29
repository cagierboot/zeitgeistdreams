import praw
import json
from datetime import datetime

# Reddit API Credentials
client_id = 'm94LTsIrdVY19IZENHTKqg'
client_secret = 'ODRb0IOHJzubnQZTKWnIomj90OG-8g'
user_agent = 'app:v1.0 cagierboot)'

# Setup Reddit Client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Subreddits to fetch data from
subreddits = ["news", "Art", "science"]

# Store all posts from different categories
all_posts_data = []

for subreddit_name in subreddits:
    top_posts = reddit.subreddit(subreddit_name).hot(limit=5)
    
    for post in top_posts:
        created_date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d')

        post_info = {
            'prompt': f"This was trending on {created_date}:",
            'completion': f"\n{post.title}\n"
        }
        all_posts_data.append(post_info)

# Writing data to a JSON file
with open('top_posts.json', 'w', encoding='utf-8') as f:
    json.dump(all_posts_data, f, ensure_ascii=False, indent=4)

print("Top posts have been saved to 'top_posts.json'")
