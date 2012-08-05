'''
Created on Aug 4, 2012

@author: petrbouchal
'''

output = 'csv' # should be csv, scraperwiki, or scraperwiki_local

import json
import urllib2
from urllib2 import urlparse
from pprint import pprint
import csv
from datetime import datetime
#from pprint import pprint
now = datetime.now()
today = datetime.today()

# build date and time strings
datestring = datetime.strftime(today, '%Y-%m-%d')
datetimestring = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
filedatestring = datetime.strftime(now, '%Y%m%d_%H%M')

# build header
fieldnames = {}

# prepare for writing
csvout = "../output/Organograms" + '_' + filedatestring + '.csv'
csvout_final = '../output/Organograms_current'
writer = csv.DictWriter(open(csvout, 'wb'), csv.QUOTE_ALL, fieldnames=fieldnames)

headers = {}
for n in fieldnames:
    headers[n] = n
writer.writerow(headers)

# create list of dates and dates in departments
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
        row = {}

        topurl = 'http://reference.data.gov.uk/' + datestring + '/doc/department/' + department + '/top-post.json'
        toppost = json.loads(urllib2.urlopen(topurl).read())

        topposturlbroken = toppost['result']['items'][0]['_about']

        print topurl
        topstats = postsjson(topposturlbroken, 'stats')

        # Get links to people in level 1 - reporting to perm sec

        level = 1
        print 'Level' + str(level)
        row = {}
        # build row here - from toppost and topstats
        # write row here

        reports1 = postsjson(topposturlbroken, 'report')
        juniors1 = postsjson(topposturlbroken, 'junior')

        #Run through junior staff reporting to perm sec

        for post in juniors1['result']['items']:
            juniorpostlabel = post['label'][0]
            row = {}
            # set up row here from post 
            # write row here
            print juniorpostlabel

        # run through senior people reporting to perm sec - level 1

        for post in reports1['result']['items']:
            posturlbroken = post['_about']

            stats1 = postsjson(posturlbroken, 'stats')

            # now level 2

            level = 2
            row = {}
            # set up row here from post and stats1
            # write row here

            juniors2 = postsjson(posturlbroken, 'junior')
            for post in juniors2['result']['items']:
                print post['label'][0]
                row = {}
                # set up row here
                # write row here


            reports2 = postsjson(posturlbroken)

            for post in reports2['result']['items']:
                print post['label'][0]
                posturlbroken = post['_about']
                stats2 = postsjson(posturlbroken, 'stats')
                row = {}
                # set up row here from post and stats1
                # write row here

                # retrieve level 3 people

                level = 3

                juniors3 = postsjson(posturlbroken, 'junior')
                for post in juniors3['result']['items']:
                    print post['label'][0]
                    row = {}
                    # set up row here
                    # write row here

                reports3 = postsjson(posturlbroken)

                for post in reports3['result']['items']:
                    posturlbroken = post['_about']
                    print posturlbroken
                    stats3 = postsjson(posturlbroken, 'stats')
                    row = {}
                    # set up row here from post and stats
                    # write row here

                    level = 4

                    juniors4 = postsjson(posturlbroken, 'junior')
                    for post in juniors4['result']['items']:
                        print post['label'][0]
                        row = {}
                        # set up row here
                        # write row here

                    reports4 = postsjson(posturlbroken)

                    for post in reports4['result']['items']:
                        print post['label'][0]
                        posturlbroken = post['_about']
                        stats4 = postsjson(posturlbroken, 'stats')
                        row = {}
                        # set up row here from post and stats4
                        # write row here

                        juniors5 = postsjson(posturlbroken, 'junior')
                        for post in juniors5:
                            print post['label'][0]
                            row = {}
                            # set up row here
                            # write row here


