from requests_oauthlib import OAuth1Session

# Your credentials

import os

# Twitter credentials from .env
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
OPENAI_API_KEY = 

# OpenAI API key (assuming you want this private too, add it to .env if not already)

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Add to .env as OPENAI_API_KEY=your_key_here


# Your X ID: 1905157307069296640
# Confirmed username: @AIFlow_Intern


# TWITTER_ID=2292112907
TWITTER_NAME="AIFlow_Intern"
TWITTER_ID = "1905157307069296640"
TWITTER_DESCRIPTION=""
API_KEY="Qlc5yGigMaeq1ianUt9Hb5kBw"
API_SECRET="sifMBk27TyialjomW74WNepXjeisenh0OFA8xS88euWG0lphux"
OPENAI_API_KEY="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"
ACCESS_TOKEN="1905157307069296640-xmyJ5arSn9zpydjEOmGoWBHVq3cdMY"
ACCESS_TOKEN_SECRET="ebk6xiTlSl0H5SmXyVH5sWE4KXKn939uhRMvAhkWrERuH"

#ACCESS_TOKEN=2292112907-"Fho5Ijkmc8MLLGFicTdlPP3SUmtPSeOaZztIIep"
#ACCESS_TOKEN_SECRET="jvsq4RqPjkpgljb5JI7OMJfGw042MF73Mzf3VIGEdsoov"


# API endpoint
url = "https://api.twitter.com/2/users/me"

# Set up OAuth 1.0a session
twitter = OAuth1Session(
    client_key=API_KEY,
    client_secret=API_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_TOKEN_SECRET
)

# Make the API request
try:
    response = twitter.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()
    user_id = data["data"]["id"]
    username = data["data"]["username"]
    print(f"Your X ID: {user_id}")
    print(f"Confirmed username: @{username}")
except Exception as e:
    print(f"Error: {e}")
    if response:
        print(f"Response content: {response.text}")