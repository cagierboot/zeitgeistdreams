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
subreddits = ["worldnews"]

# Store all posts from different categories
all_posts_data = []

for subreddit_name in subreddits:
    top_posts = reddit.subreddit(subreddit_name).hot(limit=1000)
    
    for post in top_posts:
        created_date = datetime.utcfromtimestamp(post.created_utc).strftime('%B %d, %Y')

        post_info = {
            'prompt': f"This was the headline for {created_date}:",
            'completion': f"\n{post.title}\n",
            'system_message': "You are an AI bot that is trained on world news current events and can perform analyses on this data you are training on."
        }
        all_posts_data.append(post_info)

# Writing data to a JSON file
with open('top_posts.json1', 'w', encoding='utf-8') as f:
    json.dump(all_posts_data, f, ensure_ascii=False, indent=4)

print("Top posts have been saved to 'top_posts.json1'")
