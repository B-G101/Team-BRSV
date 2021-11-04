import json
f = open("tweetdata.json")
tweets = json.load(f)

for i in tweets['data']:
    print(i['text'] + '\n')