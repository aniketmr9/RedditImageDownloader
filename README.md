# Reddit Image Downloader

This script downloads the top 10 images from mentioned subreddit.

# Install PRAW(Python Reddit API Wrapper)

<a href="https://pypi.org/project/praw/#files">PRAW PyPI</a>

Follow the steps in this <a href="https://www.pythonforengineers.com/build-a-reddit-bot-part-1/">guide</a> on how to get a client id and secret key on reddit.

Change the subreddit according to your wish:

subreddit = r.subreddit('YoursubredditName')

Change the number of images you want and category(top,hot,new etc):

posts = subreddit.top(limit=10)
