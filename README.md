    # Reddit Scraper

## Overview
This project is a Reddit scraper built using Python and the `praw` library. It is designed to scrape posts from subreddits where people share personal experiences. The scraped content is primarily intended for use in creating text-based content for YouTube.

## Features
- Scrapes posts from a single subreddit
- Scrapes posts from multiple commonly used subreddits for sharing personal experiences
- Scrapes posts from subreddits focused on paranormal and horror experiences
- Extracts post titles, score, time of upload, comments, and content

## Dependencies
Make sure you have the following dependencies installed before running the scraper:
```bash
pip install praw
```

## Files
- `test.py`: Scrapes posts from a single subreddit
- `pop_scraper.py`: Scrapes posts from two general experience-sharing subreddits
- `paranormal_scraper.py`: Scrapes posts from subreddits focused on paranormal/horror experiences

## Output Files
For pop_scraper.py and paranormal_scraper.py, the scraped data is stored in two different .txt files:
1. Full Data File (reddit_top_posts_date.txt)
    - Contains the full scraped information, including:
        - Title
        - Score
        - Time of upload
        - Number of comments
        - Post content
2. Summary File (reddit_top_posts_date_titles.txt)

## Usage
1. Create a Reddit API application on [Reddit's Developer Portal](https://www.reddit.com/prefs/apps).
2. Obtain your `client_id`, `client_secret`, `user_agent`, `username`, and `password`.
3. Configure the authentication details in each Python file.
4. Run the desired scraper script:
```bash
python test.py
```

## Example Output
```
Title: Strange Encounter in the Woods
Content: Last night, I was walking home when...
Subreddit: r/Paranormal
Upvotes: 1523
Comments: 237
```