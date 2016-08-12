import urllib2
import json
import sys

def main():
    query=str(sys.argv[1:])
    query=query.replace(' ','%20')
    api_key='AIzaSyAFy-sdMpPqh3P6hUeEM9XeEK882RCkvZw'
    url='https://maps.googleapis.com/maps/api/place/textsearch/json?query='+query+'&key='+api_key
    load=urllib2.urlopen(url)
    data=json.load(load)
   
    for item in data['results']:
        print item['name']+' '+item['formatted_address']+'\n'

if __name__=='__main__':
    print 'Searching..'
    main()
        
    
