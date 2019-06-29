import praw,requests,re

r = praw.Reddit(client_id='client_id', #add your client id
                     client_secret='client_secret', #add your client secret
                     username='username', #reddit username
                     password='password', #reddit password
                     user_agent='testbot by /u/aniketmr10') #message, can be anything
#r = praw.Reddit("Get top post")
urls = []
subreddit = r.subreddit('EarthPorn') #mention the name of the subreddit eg. r/EarthPorn, r/games
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
