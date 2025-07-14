import praw
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_reddit():
    """Initialize Reddit API client using credentials."""
    client_id = os.getenv('REDDIT_CLIENT_ID')
    client_secret = os.getenv('REDDIT_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        raise ValueError("Missing REDDIT_CLIENT_ID or REDDIT_CLIENT_SECRET in environment variables.")
    
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent='reddit_user_scraper/v1.0 (by /u/your_reddit_username)'
    )

def fetch_user_data(username):
    """
    Fetch posts and comments for a given Reddit username.
    Returns a dictionary with user data in JSON-compatible format.
    """
    reddit = initialize_reddit()
    user_data = {
        'username': username,
        'posts': [],
        'comments': []
    }
    
    try:
        redditor = reddit.redditor(username)
        
        # Fetch posts
        for submission in redditor.submissions.new(limit=100):
            post_data = {
                'id': submission.id,
                'title': submission.title,
                'body': submission.selftext if submission.is_self else None,
                'url': f"https://www.reddit.com{submission.permalink}",
                'subreddit': submission.subreddit.display_name
            }
            user_data['posts'].append(post_data)
        
        # Fetch comments
        for comment in redditor.comments.new(limit=100):
            comment_data = {
                'id': comment.id,
                'body': comment.body,
                'url': f"https://www.reddit.com{comment.permalink}",
                'subreddit': comment.subreddit.display_name
            }
            user_data['comments'].append(comment_data)
            
    except Exception as e:
        print(f"Error fetching data for {username}: {str(e)}")
        return None
    
    return user_data