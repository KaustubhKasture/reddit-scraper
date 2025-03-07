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
- `final.py`: Scrapes posts from general experience-sharing subreddits
- `paranormal.py`: Scrapes posts from subreddits focused on paranormal/horror experiences

## Usage
1. Create a Reddit API application on [Reddit's Developer Portal](https://www.reddit.com/prefs/apps).
2. Obtain your `client_id`, `client_secret`, `user_agent`, `username`, and `password`.
3. Configure the authentication details in each Python file.
4. Run the desired scraper script:
```bash
python single_subreddit_scraper.py
```

## Example Output
```json
{
    "title": "Strange Encounter in the Woods",
    "content": "Last night, I was walking home when...",
    "subreddit": "r/Paranormal",
    "score": 1523,
    "comments": 237
}
```