# What is it?
See something cool on Twitter, think "I'd like to read that/investigate it later", hit favourite, forget about entirely. 5 years pass, and you discover hundreds of "liked" tweets and a whole bunch of things you never read.

After creating an app in Twitter, this will grab info about tweets you've favourited and dump them into a CSV file for easy consumption.

# What does it do?
Downloads all available favourites, dumps everything into a JSON file, also parses out basic information about a favourite, writes to CSV.
- The text of the tweet (limited to preview, not full 240 characters)
- The user who tweeted it
- Created data (of the tweet)
- ID (for eventual pagination)
- lol stuff

# What needs to be done?
- Grab full text of tweets
- Parse links out into their own columns
- Handle images
- What about threads?
- ANALYZE!
- Dig through the monster JSON file, grab hashtags from each favourite
- Group faves by hashtag/poster/subject matter
- Can I set up the auth flow so someone can just enter their credentials?

# Structure of `gear` object
```
gear = {
  "api_key":"",
  "api_secret":"",
  "access_token":"",
  "access_token_secret":""
}
```
Extensively uses [Python Twitter](https://github.com/bear/python-twitter)
