##import json
##with open("C:/json/scrapy01.json", 'r', buffering=20000000) as records:
##    data = json.load(records)
##    for app_record in data:
##        print (len(app_record))
##        #app_jason = json.loads(app_record)
##        ##print (app_jason)
##        #data = json.loads(line)
import ijson
##
##parser = ijson.parse("C:/json/scrapy01.json")
###Ratings, AdroidVersion, Downloads
##for downloads, ratings, version in parser:
##    if(downloads, ratings) == ('Downloads', 'Ratings'):
##        print(version)
##        #stream.write(version)

f = open("C:/json/scrapy01.json", 'r', buffering=20000000)
objects = ijson.items(f, 'Ratings')
ratings = (r for r in objects)
for rate in ratings:
    print(rate)
