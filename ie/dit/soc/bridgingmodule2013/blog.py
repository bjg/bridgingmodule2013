'''
Created on 3 Sep 2013

@author: brian
'''

import datetime

blog = [
        {
         "author": "Joe Bloggs",
         "title": "My first article",
         "body": "This is a blog post",
         "posted_at": datetime.datetime.now(),
         "comments": [
                      {"body": "This is fab",
                       "comment_by": "larry@example.com"
                       },
                      {"body": "Not so good",
                       "comment_by": "jane@doe.com"
                       }
                     ]
       }
]

print blog[0]['comments'][1]["body"]