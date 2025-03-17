import praw
import datetime
import os

# Initialize Reddit (Non-Authenticated)
reddit = praw.Reddit(
    client_id="your_client_id",
    client_secret="your_client_secret",
    user_agent="name_of_app",
)

# Generate sortable timestamp for filenames
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
output_dir = "pop_output"

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

base_filename = os.path.join(output_dir, f"reddit_top_posts_{timestamp}")
posts_filename = f"{base_filename}.txt"
titles_filename = f"{base_filename}_titles.txt"
    

subreddits = ["TrueOffMyChest","confessions","SurvivingInfidelity","tifu","OffMyChest"]

for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(time_filter="week",limit=10)

# Open a file to save the data
with open(posts_filename, "w", encoding="utf-8") as f, open(titles_filename, "w", encoding="utf-8") as title_file:
    f.write("Reddit Scraper Output\n")
    f.write("=" * 80 + "\n")

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = subreddit.top(time_filter="week",limit=10)

        f.write(f"Subreddit: {subreddit_name}\n")
        f.write("=" * 80 + "\n")
        title_file.write(f"Subreddit: {subreddit_name}\n")
        title_file.write("=" * 80 + "\n")

    # Fetch 10 posts from "top of the week" section
        for post in top_posts:
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

            title_file.write(f"-{post.title}\n")
            #title_file.write("-" * 80 + "\n")
        
        f.write("\n")
        title_file.write("\n")

print(f"✅ Scraped data saved to {posts_filename} and {titles_filename}")