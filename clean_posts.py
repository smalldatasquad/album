import csv
import os
import json
from pprint import pprint
from collections import defaultdict
import secrets


with open('fb_posts.json') as data:
    d = json.load(data)
    # print d['posts'][secrets.fb_name][0]['date']
    for post in d['posts'][secrets.fb_name]:
        print post['content']['text']
    #print d['posts'][secrets.fb_name][0]['content']['text']
    # print d['posts'][secrets.fb_name][0]['content']['author']



# simplejson = []
# for i in d:
#     single_query = {}
#     single_query["post"] = i['posts'][secrets.fb_name][0]['content']['text']
#     single_query["timestamp_usec"] = i['posts'][secrets.fb_name][0]['date']
#     single_query["author"] = i['posts'][secrets.fb_name][0]['content']['author']
#     simplejson.append(single_query)
#
# print simplejson

## make a super simple json
# simplejson = []
# for j in alljsons:
#     single_query = {}
#     single_query["post"] = j['query']['query_text']
#     single_query["timestamp_usec"] = j['query']['id'][0]['timestamp_usec']
#     simplejson.append(single_query)

#
# print simplejson





#pprint(d)


# with open('some.csv', 'w', newline='', encoding='utf-8') as f:
    # writer = csv.writer(f)
    # writer.writerows(d)

# with open('utf.csv','w') as fout:
    # writer=csv.writer(fout)
    # writer.writerows([simplejson[0].keys()])
    # for row in simplejson:
	# row = [s.encode('utf-8') for s in row.values()]
	# print row


# json1_data = json.loads(json1_str)[0]
# Now you can access the data stored in datapoints just as you were expecting:
#
# datapoints = json1_data['datapoints']
