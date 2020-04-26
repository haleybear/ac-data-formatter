import json

fields = ['Name','Price','Location','Time','Months']
filename = input()
outputfilename = input()
output_file = open(outputfilename,'w')
formatlist = []
outputdict = {}


with open(filename) as fh:
    i = 0
    for line in fh:
        if i == 0:
            outputdict[fields[i]] = line
            i += 1
        else if i == 1:

        while i<len(fields):
            [fields[i]] = description[i]

