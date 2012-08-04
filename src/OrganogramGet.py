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

for department in departments:
    for datestring in datestrings[departments]:

        # Top level - Perm Sec

        topurl = 'http://reference.data.gov.uk/' + datestring + '/doc/department/' + department + '/top-post.json'
        toppost = json.loads(urllib2.urlopen(topurl).read())

        pprint(toppost)
        topposturlbroken = toppost['result']['items'][0]['_about']
        print topposturlbroken

        urlbits = urlparse.urlparse(topposturlbroken)

        newpath = urlbits.path.replace('/id/', '/doc/')

        urlnew = urlbits.scheme + '://' + urlbits.netloc + '/' + datestring + newpath + '.json'
        print urlnew

        # Get links to people in level 1 - reporting to perm sec

        reportsurl = urlbits.scheme + '://' + urlbits.netloc + '/' + datestring + newpath + '/reports-full' + '.json'
        print reportsurl

        juniorstaffurl = urlbits.scheme + '://' + urlbits.netloc + '/' + datestring + newpath + '/immediate-junior-staff' + '.json'
        print reportsurl

        reports = json.loads(urllib2.urlopen(reportsurl).read())

        juniors = json.loads(urllib2.urlopen(juniorstaffurl).read())

        #Run through junior staff reporting to perm sec

        for post in juniors['result']['items']:
            posturlbroken = post['label'][0]
            print posturlbroken

        pprint(reports)

        # run through senior people reporting to perm sec - level 1

        for post in reports['result']['items']:
            posturlbroken = post['_about']

            # Get links to subordinates of level 2 
            urlbits2 = urlparse.urlparse(posturlbroken)
            newpath2 = urlbits2.path.replace('/id/', '/doc/')
            urlpost2 = urlbits2.scheme + '://' + urlbits2.netloc + '/' + datestring + newpath2 + '.json'
            post2 = json.loads(urllib2.urlopen(urlpost2).read())

            urlreports2 = urlbits2.scheme + '://' + urlbits2.netloc + '/' + datestring + newpath2 + '/reports-full.json'
            reports2 = json.loads(urllib2.urlopen(urlreports2).read())
            print urlreports2

            # run through level 2 people 

            for post in reports2['result']['items']:
                print post['label'][0]

                for post in reports['result']['items']:
                    posturlbroken = post['_about']
                    print posturlbroken

                    # Get links to level 2 

                    urlbits2 = urlparse.urlparse(posturlbroken)
                    newpath2 = urlbits2.path.replace('/id/', '/doc/')
                    urlpost2 = urlbits2.scheme + '://' + urlbits2.netloc + '/' + datestring + newpath2 + '.json'
                    post2 = json.loads(urllib2.urlopen(urlpost2).read())

                    urlreports2 = urlbits2.scheme + '://' + urlbits2.netloc + '/' + datestring + newpath2 + '/reports-full.json'
                    reports2 = json.loads(urllib2.urlopen(urlreports2).read())
                    print urlreports2

                    # run through level 2 people 

                    for post in reports2['result']['items']:
                        print post['label'][0]
