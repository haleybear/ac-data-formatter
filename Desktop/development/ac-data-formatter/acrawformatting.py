import sys, json

if len(sys.argv)<2:
    print('Fatal: Please include an input and output file.')
    print("Usage: Python3 %s <input file name> <output file name>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1] #input source file
outputfilename = sys.argv[2] #output source file
fields = ['Name','Price','Location','Time','Months']
output_file = open(outputfilename,'w')
final_result = []
obj = {}
delimiting_string = " D"
i = 0

with open(filename) as f:
    for line in f:
        if delimiting_string in line:
            #reset counter
            #check if in next line too - if so, skip and move on

            i = 0
            obj[fields[4]]=' '
            final_result.append(obj)
            obj = dict()
            continue
        cleanup = line.rstrip("\n\r")
        obj[fields[i]] = cleanup
        i += 1

with open(outputfilename, 'w', encoding='utf-8') as f:
    f.write(json.dumps(final_result, ensure_ascii=False))
