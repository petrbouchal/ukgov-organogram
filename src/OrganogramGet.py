'''
Created on Aug 4, 2012

@author: petrbouchal
'''

#import scraperwiki

import json
import urllib2
from urllib2 import urlparse
from pprint import pprint

Mar11 = '2011-03-31'
Sep11 = '2011-09-30'
Mar12 = '2012-31-03'

departments = ['dfe']

datestrings = {}
datestrings['dfe'] = [Sep11]
datestrings['dft'] = [Sep11]

def postsjson(origurl, posttype='report'):
    urlbits = urlparse.urlparse(origurl)
    newpath = urlbits.path.replace('/id/', '/doc/')
    if posttype == 'top':
        post = 'toppost'
    elif posttype == 'report':
        post = 'immediate-reports'
    elif posttype == 'allreport':
        post = 'reports-full'
    elif posttype == 'junior':
        post = 'immediate-junior-staff'
    elif posttype == 'stats':
        post = 'statistics'
    urlpost = urlbits.scheme + '://' + urlbits.netloc + '/' + datestring + newpath + '/' + post + '.json'
    returnedposts = json.loads(urllib2.urlopen(urlpost).read())
    print urlpost
    return returnedposts

for department in departments:
    for datestring in datestrings[department]:

        # Top level - Perm Sec

        level = 0

        topurl = 'http://reference.data.gov.uk/' + datestring + '/doc/department/' + department + '/top-post.json'
        toppost = json.loads(urllib2.urlopen(topurl).read())

        topposturlbroken = toppost['result']['items'][0]['_about']
        print topposturlbroken

        # Get links to people in level 1 - reporting to perm sec

        level = 1

        reports1 = postsjson(topposturlbroken, 'report')
        juniors1 = postsjson(topposturlbroken, 'junior')

        stats1 = postsjson(topposturlbroken, stats)

        #Run through junior staff reporting to perm sec

        for post in juniors1['result']['items']:
            juniorpostlabel = post['label'][0]
            print juniorpostlabel

        # run through senior people reporting to perm sec - level 1

        for post in reports1['result']['items']:
            posturlbroken = post['_about']

            # now level 2

            level = 2

            juniors2 = postsjson(posturlbroken, 'junior')
            for post in juniors2['result']['items']: print post['label'][0]

            reports2 = postsjson(posturlbroken)

            for post in reports2['result']['items']:
                print post['label'][0]
                posturlbroken = post['_about']

                # retrieve level 3 people

                level = 3

                juniors3 = postsjson(posturlbroken, 'junior')
                for post in juniors3['result']['items']: print post['label'][0]

                reports3 = postsjson(posturlbroken)

                for post in reports3['result']['items']:
                    posturlbroken = post['_about']
                    print posturlbroken

                    level = 4

                    juniors4 = postsjson(posturlbroken, 'junior')
                    for post in juniors4['result']['items']: print post['label'][0]

                    reports4 = postsjson(posturlbroken)

                    for post in reports4['result']['items']:
                        print post['label'][0]
                        posturlbroken = post['_about']

                        reports5 = postsjson(posturlbroken)
