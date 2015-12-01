import symbol_parser
import sys
import getopt


def main(argv):
	inputfile = ''
	parser = symbol_parser.parser
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile>'
			sys.exit()
		elif opt in ('-i','--ifile'):
			inputfile = arg
	print parser.parse(open(inputfile).read())		
if __name__ == "__main__":
	main(sys.argv[1:])	
