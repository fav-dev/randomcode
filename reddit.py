#!/usr/bin/env python3

import praw

# Replace the values below with your own Reddit account information and app details
reddit = praw.Reddit(
    client_id='wioN9lykZZBPasxICdwr7A',
    client_secret='3qc2ldycdSRz8cAj9nlGpuahvudbcA',
    redirect_uri ='http://localhost:8000',
    username='M1700249',
    password='Deaths123',
    user_agent='auto_post:v1.0.0(by /u/M1700249)')


auth_url = reddit.auth.url(
    scopes=["*"],
    state="random_string",
    duration="permanent",
)
print(auth_url)

# ... user is redirected to the URL specified in auth_url

# Go to the auth_url in your browser, authorize the app, and get the code from the redirected URL

# Use the code to get the access token
access_token = reddit.auth.authorize(code="code_from_redirected_url")

# Replace the values below with the details of the subreddit you want to post to
subreddit_name = 'NoFap'
subreddit = reddit.subreddit(subreddit_name)

# Replace the values below with the details of your post
post_title = 'your_post_title'
post_body = 'your_post_body'

# Create the post
post = subreddit.submit(title=post_title, selftext=post_body)

print('Post created successfully!')

if post.id:
    print('Post created successfully!')
else:
    print('Error: post was not created.')
