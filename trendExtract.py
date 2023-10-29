

import praw
import json

# Reddit API Credentials
client_id = 'm94LTsIrdVY19IZENHTKqg'
client_secret = 'ODRb0IOHJzubnQZTKWnIomj90OG-8g'
user_agent = 'app:v1.0 (by /u/cagierboot)'

# Setup Reddit Client
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Subreddit to fetch data from
subreddit_name = "worldnews"

# Store all posts with their top comments
all_posts_data = []

top_posts = reddit.subreddit(subreddit_name).hot(limit=100)
for post in top_posts:
    # Ensure the post has been loaded correctly
    post.comment_sort = 'top'
    post.comments.replace_more(limit=0)  # Load all top-level comments, replace "more comments" links
    top_comment = post.comments[0].body if post.comments else "No comments available."

    post_info = {
    'prompt': f"{post.title}",
    'completion': f"\n{top_comment}\n",
    'system_message': "You are an AI bot that is trained on world news current events and can perform analyses on this data you are training on."
}

    all_posts_data.append(post_info)

# Writing data to a JSON file
with open('top_posts_with_comments.json', 'w', encoding='utf-8') as f:
    json.dump(all_posts_data, f, ensure_ascii=False, indent=4)

print("Top posts with their top comments have been saved to 'top_posts_with_comments.json'")
