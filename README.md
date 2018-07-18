# AI Twitterbot

### Twitter is an awesome tool for sharing interesting stories. This script finds news reports about a specific topic using Aylien's NewsAPI and tweets the most popular story.

## Getting started 

### Setup a twitter APP

This script assumes you have a twitter account are familiar with the basics of twitter (e.g., what a tweet is and what a twitter handle is). 

Go to `https://apps.twitter.com` and click the  "Create New App"  button. 

Fill out the form and you will see four tabs "Details", "Settings", "Keys and Access Tokens", "Permissions"

Select the `Keys and Access Tokens` tab. 

Click the `Generate Consumer Key and Secret`

You will need to note the following credentials

`Consumer Key (API Key)   ********************`

`Consumer Secret (API Secret)      ******************`

`Access Token ****************`

`Access Token Secret   ************`

### Setup an Aylien News API account

The NLP tool used in this script is from Aylien. I'm a big fan of this company since they publish tons of useful blogs and have really good documentation generally. Recently they released a specialised tool called "News API" which automates the task of finding headlines accross thousands of media outlets. In principle this could be run continuosly and you could generate real time feedback about what the media are saying about your company. In this script we will keep it simple and simply find some interesting articles.

Go to `https://aylien.com/news-api/`  and click "Sign Up"

Fill out the form and you will receive an Action Required email asking you to validate your account. 

You will need to create an application key.

Next go to `https://newsapi.aylien.com/admin`  

You need to note the following credentials:

`App ID  ********`

`AppKey  *****************`

### Using this script

`git clone https://github.com/tmcellfree/AI_twitterbot_aylien.git`

`cd AI_twitterbot_aylien`
 
`nano credentials.py`

You need to enter your twitter API keys and your Aylien NewsAPI keys from earlier. 

`nano aylien_twitterbot.py` 

Look for the line `INSERT YOUR TWITTER HANDLE`

enter your twitter handle without the @ symbol

Look for `YOUR NEWS ITEM HERE`

The default is "Synthetic Biology" but enter the headline item you are interested in.

Use the script by typing:
`python aylien_twitterbot.py`

### Automating the script

If you have a server (e.g., a digital ocean droplet), you could run this script continuously. 

Setup a cron job by typing

`crontab -e`

scroll to the bottom of the script and add 

` 0 */6 * * * /usr/bin/python /INSERT_YOUR_DIRECTORY_LOCATION/AI_twitterbot_aylien/aylien_twitterbot.py`

This will run your script every six hours (every sixth hour to be precise..). If you would like to adjust this then you can read `http://www.adminschoice.com/crontab-quick-reference` to get a better understanding of the crontab environment. This is worth reading since crontabs are awesome for automating regular tasks! 
