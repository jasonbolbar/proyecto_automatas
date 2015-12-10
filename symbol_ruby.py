import symbol_parser
import sys
import getopt

# Escribir el codigo compilado en un archivo de formato .rb
def write_compiled(filename,compiled):
	if compiled == None:
		return None
	file = open(filename.split('.')[0] + '.rb','w')
	file.truncate()
	file.write(compiled)
	file.close()

# Metodo principal
def main(argv):
	inputfile = ''
	parser = symbol_parser.parser

	#Obtiene los parametros enviados por linea de comandos

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

	# Compilacion de codigo		
			
	compiled = parser.parse(open(inputfile).read())	
	write_compiled(inputfile,compiled)	
if __name__ == "__main__":
	main(sys.argv[1:])	
