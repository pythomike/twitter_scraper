# What It Is?
See something cool on Twitter, think "I'd like to read that/investigate it later", hit favourite, forget about entirely. 5 years pass, and you discover hundreds of "liked" tweets and a whole bunch of things you never read.

After creating an app in Twitter, this will grab info about tweets you've favourited and dump them into a CSV file for easy consumption.
# What It Does?
Downloads the most recent 200 liked tweets, and writes them into a CSV. Currently grabbing...
- The text of the tweet (limited to preview, not full 240 characters)
- The user who tweeted it
- Created data (of the tweet)
- ID (for eventual pagination)
# What's It Need To Do?
- Grab all favourites
- Grab full text of tweets
- Parse links out into their own columns
- Handle images
- What about threads?
- ANALYZE!