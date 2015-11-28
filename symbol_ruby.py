# imports
import ply.lex as lex
import ply.yacc as yacc
import sys
import getopt
import pdb

tokens = ('IDENTIFIER', 'DO', 'CLASS', 'HIERACHY', 'MODULE', 'DEF', 'ASSIGNATION_OPERATORS',
 'IF', 'ELSE', 'UNLESS', 'WHILE', 'ARRAY', 'CASE', 'WHEN', 'BEGIN',
 'RESCUE', 'STRING', 'FIXNUM', 'NIL', 'FLOAT', 'HASH', 'SYMBOL', 'TRUE', 'FALSE', 'CONSTANT',
 'NAMESPACE_CHARACTER', 'LOGICAL_OPERATORS', 'COMPARATOR_OPERATORS', 'OPERATORS', 'NEW_LINE', 'TAB',
 'INSTACE_VAR', 'CLASS_VAR', 'GLOBAL_VAR', 'PREDEF_VAR', 'PERIOD', 'EXC_OP', 'PIPE', 'COMMA', 'EQUAL',
 'COLON', 'QU_MARK', 'EXCL_MARK', 'OPEN_PARENTH', 'CLOSE_PARENTH', 'OPEN_KEY', 'CLOSE_KEY'
 )

# t_BREAK = r'_\\_'
t_CASE = r'>:'
t_CLASS = r'<@>'
t_DEF = r'\$'
t_DO = r'\{\+\}'
t_ELSE = r'\?@'
# t_ELSIF = r'\?@\?'
# t_ENSURE = r'_/_'
# t_FOR = '\{#\}'
t_IF = r'\?\?'
t_UNLESS = r'\-\?'
# t_IN = r'in'
t_MODULE = r'<@@>'
# t_NEXT = r'~@'
t_BEGIN = r'\^%'
# t_RAISE = r'%'
t_HIERACHY = r'<\+>'
t_NAMESPACE_CHARACTER = r'<\^>'
# t_REDO = '\-\|\*'
t_RESCUE = r'%\^'
# t_RETRY = r'retry'
# t_RETURN = r'<\-'
# t_SUPER = r'&\*&'
# t_THEN = r'\->'
# t_UNDEF = r'undef'
# t_UNTIL = r'\]\?\['
t_WHEN = r'~:'
t_WHILE = r'\[\?\]'
# t_YIELD = r'\{>\}'
t_IDENTIFIER = r'([a-z]|\_)(\w)+'
t_CONSTANT = r'[A-Z](\w)+'
t_INSTACE_VAR = r'@t_IDENTIFIER'
t_CLASS_VAR = r'@@t_IDENTIFIER'
t_GLOBAL_VAR = r'\$t_IDENTIFIER'
t_PREDEF_VAR = r'\$((\!|ERROR_INFO)|(\@|ERROR_POSITION)|(\&|MATCH)|(\`|PREMATCH)|(\'|POSTMATCH)|(\+|LAST_PARENT_MATCH)|[0-9]|(\~|LAST_MATCH_INFO)|(\=|IGNORE_CASE)|(\\|INPUT_RECORD_SEPARATOR|RS|\-0)|(\/|OUTPUT_RECORD_SEPARATOR|ORS)|(\,|OUTPUT_FIELD_SEPARATOR_OFS)|(\;|FIELD_SEPARATOR|FS|\-F)|(\.|INPUT_LINE_NUMBER|NR)|(\<|DEFAULT_INPUT)|FILENAME|(\>|DETAULT_OUTPUT)|(\_|LAST_READ_LINE)|\*|(\$|PROCESS_ID|PID|Process\.pid)|(\?|CHILD_STATUS)|(\:|LOAD_PATH)|(\"|LOADED_FEATURES|\-I)|stderr|stin|(\-d|DEBUG)|(\-K|KCODE)|(\-v|VERBOSE)|\-i|\-l|\-p|\-w)'
# t_PREDEF_CONST = r'\_\_(FILE|LINE|dir)\_\_'
t_FIXNUM = r'\-?((0((x|X)([0-9]|[a-f]|[A-F])+|(b|B)([0-1])+|([0-7]+)))|([1-9]+(\_?[0-9])*))'
t_FLOAT = r'\-?[1-9]+\.[0-9]+(e\-?[0-9]+)?'
t_STRING = r'\"([^\\"](\\")?(\\)?)*\"|\'([^\'](\\\\)?(\')?)*\''
t_ARRAY = r'\[(\s)*((.)(\s)*(\,[^,]+)*)?\]|\%w(\(.*\)|t_STRING)'
t_HASH = r'{((\s)*("[^"]+"|\'[^\']+PIPE[^\']\'|:\w+(\s)*=>|\w+:)(\s)*[^,]+,?)*}'
t_SYMBOL = r'\:(t_CONSTANT|variable)'
t_TRUE = r'TRUE|true'
t_FALSE = r'FALSE|false'
# t_RANGE =
# r'((-?\d+.?\d+)|(\'[^\']+\')|("[^"]+"))(..|...)((-?\d+.?\d+)|(\'[^\']+\')|("[^"]+"))'
t_ASSIGNATION_OPERATORS = r'\+|\-|\*\*?|\/'
t_OPERATORS = r'\+|\-|\*\*?|\/'
t_LOGICAL_OPERATORS = r'\|\||\&\&'
t_COMPARATOR_OPERATORS = r'(\<|\>|\t_EQUAL|\!)+\t_EQUAL'
# t_COMMENTS = r'#(.)*|\=begin(.|\n)*\=end'
# t_AND = r'and'
# t_OR = r'or'
t_PERIOD = r'\.'
# t_SEMICOMMA = r'\;'
t_NIL = r'nil'

t_NEW_LINE = r'\n'
t_TAB = r'\t'
t_EXC_OP = r'\=\>'
t_PIPE = r'\|'
t_COMMA = r'\,'
t_EQUAL = r'\='
t_COLON = r'\:'
t_QU_MARK = r'\?'
t_EXCL_MARK = r'\!'
t_OPEN_PARENTH = r'\('
t_CLOSE_PARENTH = r'\)'
t_OPEN_KEY = r'\('
t_CLOSE_KEY = r'\)'

# tokens default
t_ignore = " "


def t_error(t):
    print 'error lexico'
    t.lexer.skip(1)

lex.lex(debug=True)


def p_main(p):
	'''symbol_ruby : ins
	               | class_def
	               | module_def
	               | method_def

	               '''
	print p[1]


def p_method_main(p):
	'method_call : method_cl'
	p[0] = p[1]


def p_method_main_2(p):
	'''method_call : IDENTIFIER block_def
	               | method_cl block_def
	               '''
	p[0] = p[1] + p[2]


def p_method_cl(p):
	'method_cl : IDENTIFIER value'
	p[0] = p[1]


def p_method_cl_params(p):
	'''method_cl : IDENTIFIER OPEN_PARENTH parameter CLOSE_PARENTH
	             | IDENTIFIER OPEN_PARENTH hash_pr CLOSE_PARENTH'''
	p[0] = p[1] + p[2] + p[3] + p[4]


def p_hash_parameter(p):
	'hash_pr : IDENTIFIER COLON value COMMA hash_pr'
	p[0] = p[1] + p[2] + p[3] + p[4]


def p_has_parameter_end(p):
	'hash_pr : IDENTIFIER COLON value'
	p[0] = p[1] + p[2] + p[3]


def p_block_def(p):
	'block_def : DO PIPE parameter PIPE new_cmd'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_block_def_simple(p):
	'block_def : OPEN_KEY PIPE parameter PIPE ins CLOSE_KEY'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]


def p_class_def(p):
	'class_def : CLASS name hierachy NEW_LINE TAB symbol_ruby'
	p[0] = p[1] + p[2] + p[4]


def p_hierachy(p):
	'hierachy : HIERACHY name'
	p[0] = p[1] + p[2]


def p_hierachy_empty(p):
	'hierachy : '


def p_module_def(p):
	'module_def : MODULE name NEW_LINE TAB symbol_ruby'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_method_def(p):
	'method_def : DEF IDENTIFIER method_s OPEN_PARENTH method_p CLOSE_PARENTH new_cmd'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[7]


def p_method_s(p):
	'''method_s : EXCL_MARK
				| QU_MARK
				|
				'''
	p[0] = p[1]


def p_method_pa_assig_cont(p):
	'method_p : IDENTIFIER EQUAL value COMMA method_p'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_method_pa_single_cont(p):
	'method_p : IDENTIFIER COMMA method_p'
	p[0] = p[1] + p[2] + p[3]


def p_method_pa_assig_end(p):
	'method_p : IDENTIFIER EQUAL value'
	p[0] = p[1] + p[2] + p[3]


def p_method_pa_single_end(p):
	'method_p : IDENTIFIER'
	p[0] = p[1]


def p_ins_single(p):
	'''ins : assig
		   | exception_def
		   | cond_ins
		   | cmd
		   '''
	p[0] = p[1]


def p_inst(p):
	'ins : NEW_LINE ins'
	p[0] = p[1] + p[2]


def p_cond_ins(p):
	'''cond_ins : if_def
				| unless_def
				| while_def
				| case_def
				'''
	p[0] = p[1]


def p_cmd_single(p):
	'''cmd : method_call
		   | vars'''
	p[0] = p[1]


def p_cmd(p):
	'cmd : vars PERIOD cmd'
	p[0] = p[1] + p[2] + p[3]


def p_assig(p):
	'''assig : vars ASSIGNATION_OPERATORS cmd
	       | vars ASSIGNATION_OPERATORS value'''
	p[0] = p[1] + p[2] + p[3]


def p_if_def_complex(p):
	'if_def : if_inst else_def'
	p[0] = p[1] + p[2]


def p_if_def_simple(p):
	'if_def : condition QU_MARK ins COLON ins'
	p[0] = p[1] + p[2] + p[3] + p[4]


def p_if_ins(p):
	'if_inst : IF condition new_cmd'
	p[0] = p[1] + p[2] + p[3]


def p_unless_def(p):
	'unless_def : UNLESS condition new_cmd'
	p[0] = p[1] + p[2] + p[3]


def p_while_def(p):
	'while_def : WHILE condition new_cmd'
	p[0] = p[1] + p[2] + p[3]


def p_else_def(p):
	'else_def : ELSE new_cmd'
	p[0] = p[1] + p[2]


def p_else_def_empty(p):
	'else_def : '
	p[0] = p[1]


def p_case_def(p):
	'case_def : CASE case_stmt case_when'
	p[0] = p[1] + p[2] + p[3]


def p_case_stmt(p):
	'''case_stmt : vars
				 | value'''
	p[0] = p[1]


def p_case_when_cont(p):
	'case_when : WHEN condition new_cmd case_when'
	p[0] = p[1] + p[2] + p[3] + p[4]


def p_case_when_end(p):
	'case_when : WHEN condition new_cmd'
	p[0] = p[1] + p[2] + p[3]


def p_exception_def(p):
	'exception_def : BEGIN new_cmd rescue'
	p[0] = p[1] + p[2] + p[3]


def p_rescue_def(p):
	'rescue : RESCUE name new_cmd'
	p[0] = p[1] + p[2] + p[3]


def p_rescue_var_def(p):
	'rescue : RESCUE vars EXC_OP name new_cmd'
	p[0] = p[1] + p[2] + p[3] + p[4]


def p_condition_single(p):
	'''condition : value
				 | vars
				 '''
	p[0] = p[1]


def p_condition_def(p):
	'''condition : value operator
				 | vars operator
				 '''
	p[0] = p[1] + p[2]


def p_parameter_end(p):
	'parameter : value'
	p[0] = p[1]


def p_parameter_def(p):
	'parameter : value COMMA parameter'
	p[0] = p[1] + p[2] + p[3]


def p_value(p):
	'''value : STRING
			 | FIXNUM
			 | NIL
			 | FLOAT
			 | ARRAY
			 | HASH
			 | SYMBOL
			 | TRUE
			 | FALSE
			 '''
	p[0] = p[1]


def p_name_single(p):
	'name : CONSTANT'
	p[0] = p[1]


def p_name_complex(p):
	'name : CONSTANT NAMESPACE_CHARACTER name'
	p[0] = p[1] + p[2] + p[3]


def p_operator(p):
	'''operator : LOGICAL_OPERATORS
				| COMPARATOR_OPERATORS
				| OPERATORS
				'''
	p[0] = p[1]


def p_vars(p):
	'''vars : INSTACE_VAR
			| CLASS_VAR
			| GLOBAL_VAR
			| PREDEF_VAR
			'''
	p[0] = p[1]


def p_new_cmd(p):
	'new_cmd : NEW_LINE TAB ins'
	p[0] = p[1] + p[2] + p[3]


def p_error(p):
	pdb.set_trace()
	print 'error sintactico'

    


def main(argv):
	inputfile = ''
	outputfile = ''
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
	parser.parse(''.join(file.readlines()))
if __name__ == "__main__":
	main(sys.argv[1:])
