import json

#prompt the user for a file to import
##filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
##filename = rs.OpenFileName("Open JSON File", filter)
##
###Read JSON data into the datastore variable
##if filename:
with open("Z:\\scrapy01.json", 'r', buffering=2000000000) as f:
    datastore = json.load(f)

#Use the new datastore datastructure
#print datastore["office"]["parking"]["style"]
