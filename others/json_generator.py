from sys import argv

if len(argv) == 2:
	infile = argv[1]
else:
	print("Usage: python3 json.py infile")

outfile = infile + ".json"
with open(outfile, 'w') as json_file:
    json.dump(infile, json_file, indent=4)

