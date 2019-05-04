import csv
import codecs
sitedict = {}
fileReader = csv.reader(codecs.open('usercred.csv','r', 'utf-16'))

#maybe try a dictionary inside of a dictionary?
for row in fileReader:
    print(row[0])
    sitedict["school"] = 'odu.edu'
    if row[0] == "School ":
        print("match found")
    else:
        print("match not found")
    for site in sitedict.keys():
        if row[0]== site:
            print("matching keys found")
        else:
            print("no matching keys found")