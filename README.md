# Script to scan media for news and tweet relevent content

### Twitter is an awesome tool for sharing interesting stories. This script finds news reports about a specific topic using Aylien's NewsAPI and tweets the most popular story.

### Getting started 

###Setup a twitter APP
This script assumes you are familiar with twitter. 

Go to `https://apps.twitter.com` and click the  "Create New App"  button. 

### Setup an Aylien News API account. 

Go to `https://aylien.com/news-api/`  and click "Sign Up"


### Using this script

`git clone `

`cd AI_twitterbot_aylien`
 
`nano credentials.py`

You need to enter your twitter API keys and your Aylien NewsAPI keys. 


`nano aylien_twitterbot.py` 

Look for the line ` ENTER YOUR HANDLE HERE`

enter your twitter handle

Look for `News item`

enter the headline item you are interested in.

Use the script by typing:
`python aylien_twitterbot.py`

### Automating the script

Setup a cron job
