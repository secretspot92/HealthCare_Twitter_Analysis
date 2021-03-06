import sys
import json
import operator

def main():
	afinnfile = open(sys.argv[1])

	wdict = {}
	get = wdict.get
	point = 0
	for line in afinnfile:
		for word in line.split():
				term = word
				wdict[term] = get(term, 0) + 1
				point +=1

	count = wdict.items()
	count.sort(key=operator.itemgetter(1),reverse=True)
	for i in range(len(count)):
		print count[i][0], count[i][1]

if __name__ == '__main__':
    main()
