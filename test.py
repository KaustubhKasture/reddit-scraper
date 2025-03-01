import praw
import datetime

# Initialize Reddit (Non-Authenticated)
reddit = praw.Reddit(
    client_id="IPCT_0TSAVi-4CoyZ6vRIA",
    client_secret="W6_2ukA62FeOIlUuZ8wSXNQXnpKItw",
    user_agent="my_scraper",
)

subreddit = reddit.subreddit("TrueOffMyChest")

# Open a file to save the data
with open("reddit_posts.txt", "w", encoding="utf-8") as f:
    f.write("Reddit Scraper Output\n")
    f.write("=" * 80 + "\n")

    # Fetch 10 posts from "hot" section
    for post in subreddit.top(time_filter="week",limit=10):
        title = post.title
        score = post.score  # Upvotes - Downvotes
        created_time = datetime.datetime.utcfromtimestamp(post.created_utc)  # Convert UNIX timestamp
        num_comments = post.num_comments
        post_text = post.selftext.strip() if post.selftext else "No text content"  # Get post content
        
        # Write post details to file
        f.write(f"Title: {title}\n")
        f.write(f"Score (Upvotes - Downvotes): {score}\n")
        f.write(f"Time of Upload: {created_time} UTC\n")
        f.write(f"Comments: {num_comments}\n")
        f.write("Post Content:\n")
        f.write(post_text + "\n")
        f.write("=" * 80 + "\n\n")

print("✅ Scraped data saved to reddit_posts.txt")