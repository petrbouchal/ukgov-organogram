'''
Created on Feb 9, 2013

@author: petrbouchal
'''
import json, csv
from pprint import pprint
import urllib2
from urllib2 import urlparse
from datetime import datetime
from collections import defaultdict

import scraperwiki
from pprint import pprint

now = datetime.now()
today = datetime.today()

# build date and time strings
datestring = datetime.strftime(today, '%Y-%m-%d')
datetimestring = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
filedatestring = datetime.strftime(now, '%Y%m%d_%H%M')

def postsjson(origurl, datatype='report'):
    """ Return iterable JSON of posttype got by updating and querying origurl"""
    urlbits = urlparse.urlparse(origurl)
    newpath = urlbits.path.replace('/id/', '/doc/')
    if datatype == 'info':
        post = ''
    elif datatype == 'report':
        post = '/immediate-reports'
    elif datatype == 'allreport':
        post = '/reports-full'
    elif datatype == 'junior':
        post = '/immediate-junior-staff'
    elif datatype == 'stats':
        post = '/statistics'
    urlpost = urlbits.scheme + '://' + urlbits.netloc + '/' + org['Date'] + newpath + post + '.json'
    returnedposts = json.loads(urllib2.urlopen(urlpost).read())
    print urlpost
    return returnedposts

def TraverseJobs(joburl):
    jobjson = json.loads(urllib2.urlopen(joburl).read())
    pprint(jobjson)

    jobabout = jobjson['_about']

    print(jobabout)

TraverseJobs('http://reference.data.gov.uk/2012-09-30/doc/department/dft/top-post.json')
