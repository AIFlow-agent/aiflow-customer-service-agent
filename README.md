# 🤖 AIFlow Twitter Bot
Automate the generation and posting of unique, insightful tweets about **AIFlow**, a decentralized intelligent agent ecosystem integrating Web3 and AI (BNB Chain, Greenfield, DAO governance, etc.). Tweets are created using OpenAI's GPT-4o and automatically posted to your Twitter/X account via the `TwitterTool` integration in the Swarms ecosystem.

## ✨ Features
- ✅ Posts non-repetitive, engaging tweets generated from the **AIFlow white paper**
- 🤖 Uses a specialized AI agent trained to act as an **AIFlow Promoter**
- 📡 Fully automated — just set your API keys and run
- 🖼️ (Optional) Supports posting tweets with custom images
- 🔐 Environment variables for secure key management

## 🚀 Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/entrova-ai-hq/aiflow-twitter-bot.git
cd aiflow-twitter-bot
```

### 2. Install dependencies
```bash
pip install python-dotenv swarms swarm-models
```

### 3. Set your environment variables
Create a `.env` file in the project root:
```bash
touch .env
```
Add the following:
```env
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
OPEN_API_KEy=your_openai_api_key
```
> ⚠️ Make sure the casing matches exactly (`OPEN_API_KEY` is used in the code)

## 🧠 How It Works
1. Loads credentials from `.env`
2. Initializes an `OpenAIChat` GPT-4o model with a system prompt tailored to promote **AIFlow**
3. Defines a `TwitterTool` using your API keys
4. Posts 3 unique tweets, generated from a prompt summarizing the AIFlow ecosystem

Each tweet includes:
- An AI-generated statement about AIFlow
- A randomized emoji
- A timestamp + UUID suffix to ensure uniqueness

## 🔄 Example Tweet Output
```
AIFlow agents optimize DeFi insurance in real time using BNB Chain + on-chain data — fully autonomous and privacy-preserving. 🌍 13:57:02 | a9d3f2
```

## 🖼️ Optional: Post with Images
To post tweets with attached images:
1. Save your PNGs to a `data-test/` folder (`data-test/1.png`, `data-test/2.png`, etc.)
2. Uncomment the `post_unique_tweets_with_images()` function
3. Call it in `if __name__ == "__main__":`
```python
# post_unique_tweets_with_images(3)
```

## 🛠 File Structure
```
TWTR/
├── agent_workspace/
│   └── prompts/              # Subfolder for any prompt templates
├── data-test/                # Optional images to post with tweets
├── .env                      # Your API credentials
├── aiflow.py                 # Main Twitter bot script (AIFlow-focused)
├── get_x_id.py              # Utility script to fetch your X/Twitter ID
├── tool.py                   # Older or alt version of tweet script
├── error.txt                 # Error logs or messages (if any)
└── README.md                 # You're here!
```

## 🧪 Testing
Run the script from the command line:
```bash
python airflow.py
```

Expected behavior: 3 unique tweets about AIFlow are posted to your X account.


## 📄 License
MIT License — use it, fork it, launch your own bot!