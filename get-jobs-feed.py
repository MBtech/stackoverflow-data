import feedparser
from datetime import datetime
import os
import pickle

data = set()
if (os.path.isfile('feed')):
    data = set(pickle.load(open('feed', 'r')))

NewsFeed = feedparser.parse("https://stackoverflow.com/jobs/feed")

jobIDs = set([x['id'] for x in data])

for entry in NewsFeed.entries:
    if entry['id'] not in jobIDs:
        del entry['updated_parsed']
        del entry['published_parsed']
        data.add(entry)
# data = data.union(set(NewsFeed.entries))

data = list(data)
print (len(data))
pickle.dump(data, open('feed', 'w'))
# print len(NewsFeed.entries)
#
sortedEntries = sorted(NewsFeed.entries, key=lambda x: datetime.strptime(
    x['updated'], '%Y-%m-%dT%H:%M:%SZ'), reverse=True)
print sortedEntries[-1]
# print sortedEntries[0]
