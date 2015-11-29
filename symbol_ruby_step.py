# imports
import ply.lex as lex
import ply.yacc as yacc
import sys
import getopt
import pdb

tokens = ('CLASS','CONSTANT','SPACE','NEW_LINE','TAB','COLON','MODULE','IDENTIFIER','DEF')

t_CLASS = r'<@>'
t_CONSTANT = r'[A-Z](\w)+'
t_SPACE = r'\s'
t_NEW_LINE = r'\n+'
t_TAB = r'\t+'
t_COLON = r'\:'
t_MODULE = r'<@@>'
t_IDENTIFIER = r'([a-z]|\_)(\w)+'
t_DEF = r'\$'


def t_error(t):
    print 'Error in line {}, column {}, with {}'.format(t.lineno,t.lexpos,t.value)
    t.lexer.skip(1)

def p_main(p):
	'main : symbol_ruby'
	p[0] = p[1]

def p_symbol_ruby(p):
	'''symbol_ruby : class_def 
				   | module_def
				   | method_def
				   '''
	p[0] = p[1]	


def p_class_def(p):
	'class_def : CLASS SPACE name NEW_LINE TAB symbol_ruby'
	p[0] = 'class {}\n{}\nend'.format(p[3],p[6])

def p_module_def(p):
	'module_def : MODULE SPACE name NEW_LINE TAB symbol_ruby'
	p[0] = 'module {}{}end'.format(p[3],p[6])

def p_namespaced_name(p):
	'name : CONSTANT COLON COLON name'
	p[0] = '{}::{}'.format(p[1],p[4])

def p_name(p):
	'name : CONSTANT'
	p[0] = p[1]

def p_method_def(p):
	'method_def : DEF SPACE IDENTIFIER NEW_LINE TAB cmd'
	p[0] = p[1]

def p_cmd(p):
	'cmd : IDENTIFIER'	
	p[0] = p[1]

		

    
    

def main(argv):
	inputfile = ''
	outputfile = ''
	lexer = lex.lex()
	parser = yacc.yacc()
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
	file = open(inputfile)
	print file.readlines()
	result = parser.parse(file.read())
	print result
if __name__ == "__main__":
	main(sys.argv[1:])	



