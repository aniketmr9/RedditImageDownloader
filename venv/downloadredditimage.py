import praw,requests,re

r = praw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     username='username',
                     password='password',
                     user_agent='testbot by /u/aniketmr10')
#r = praw.Reddit("Get top post")
urls = []
subreddit = r.subreddit('EarthPorn')
posts = subreddit.top(limit=10)
for post in posts:
    url = (post.url)
    print(url)
    urls.append(url)
print(urls)
for url in urls:
    if ".jpg" in url:
        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]
        if "." not in file_name:
            file_name += ".jpg"
        print(file_name)
        r = requests.get(url)
        with open(file_name,"wb") as f:
            f.write(r.content)
