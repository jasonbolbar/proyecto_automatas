import symbol_lexer
import symbol_coder
import ply.yacc as yacc

tokens = symbol_lexer.tokens

def p_symbol_ruby(p):
	'''symbol_ruby : variable
				  | value
				  | method
				  | range 
	'''
	# La produccion range se debe usar donde se ocupa
	p[0] = symbol_coder.c_concatenate(p)
	

def p_variable(p):
	'''variable : IDENTIFIER 
	      | instance_variable 
	      | class_variable 
	      | global_variable'''
	p[0] = symbol_coder.c_concatenate(p)

def p_instance_variable(p):
	'''instance_variable : AT IDENTIFIER 
	           | AT CONSTANT'''
	p[0] = symbol_coder.c_concatenate(p)

def p_class_variable(p):
	'''class_variable : AT AT IDENTIFIER 
	           | AT AT CONSTANT'''
	p[0] = symbol_coder.c_concatenate(p)

def p_global_variable(p):
	'''global_variable : DOLLAR IDENTIFIER
	           | DOLLAR CONSTANT 
	           | SPECIAL_VAR'''
	p[0] = symbol_coder.c_concatenate(p) 

def p_value(p):
	'''
	value : FLOAT 
		 | STRING 
		 | FIXNUM 
		 | SYMBOL 
		 | NIL 
		 | TRUE 
		 | FALSE
		 | SPECIAL_NUM 
		 | array
		 | hash
		 | SELF
	'''
	p[0] = symbol_coder.c_concatenate(p)
  

def p_method(p):
	'method : DEF IDENTIFIER method_s OPEN_PARENTH method_p CLOSE_PARENTH new_cmd END'
	p[0] = symbol_coder.c_method(p)

def p_method_s(p):
	'''method_s : EXCL_MARK
				| QU_MARK
				|
				'''
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_assig_cont(p):
	'method_p : IDENTIFIER EQUAL value COMMA method_p'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_assig_end(p):
	'method_p : IDENTIFIER EQUAL value'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_single_cont(p):
	'method_p : IDENTIFIER COMMA method_p'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_single_end(p):
	'''method_p : IDENTIFIER 
				|
				'''
	p[0] = symbol_coder.c_concatenate(p)

def p_new_cmd(p):
	'new_cmd : ins'
	p[0] = symbol_coder.c_concatenate(p)

def p_ins_single(p):
	'''ins : assig
		  | cmd
		  |
		  '''
	p[0] = symbol_coder.c_concatenate(p)




def p_assig(p):
	'''assig : variable EQUAL cmd
	    | variable EQUAL value'''
	p[0] = symbol_coder.c_concatenate(p)

def p_cmd_single(p):
	'''cmd : method_call
		  | variable'''
	p[0] = symbol_coder.c_concatenate(p)


def p_cmd(p):
	'cmd : variable PERIOD cmd'
	p[0] = symbol_coder.c_concatenate(p)	

def p_method_main(p):
	'method_call : method_cl'
	p[0] = symbol_coder.c_concatenate(p)


def p_method_main_2(p):
	'''method_call : IDENTIFIER block_def
	        | method_cl block_def
	        '''
	p[0] = symbol_coder.c_concatenate(p)

def p_method_cl(p):
	'method_cl : IDENTIFIER value'
	p[0] = symbol_coder.c_concatenate(p)


def p_method_cl_params(p):
	'''method_cl : IDENTIFIER OPEN_PARENTH parameter CLOSE_PARENTH
	       | IDENTIFIER OPEN_PARENTH hash_pr CLOSE_PARENTH'''
	p[0] = symbol_coder.c_concatenate(p)


def p_hash_parameter(p):
	'hash_pr : IDENTIFIER COLON value COMMA hash_pr'
	p[0] = symbol_coder.c_concatenate(p)


def p_has_parameter_end(p):
	'hash_pr : IDENTIFIER COLON value'
	p[0] = symbol_coder.c_concatenate(p)


def p_block_def(p):
	'block_def : DO PIPE parameter PIPE new_cmd'
	p[0] = symbol_coder.c_concatenate(p)


def p_block_def_simple(p):
	'block_def : OPEN_BRACE PIPE parameter PIPE ins CLOSE_BRACE'
	p[0] = symbol_coder.c_concatenate(p)

def p_parameter_end(p):
	'parameter : value'
	p[0] = symbol_coder.c_concatenate(p)


def p_parameter_def(p):
	'parameter : value COMMA parameter'
	p[0] = symbol_coder.c_concatenate(p)






################################################ JASON IS WORKING HERE ############################################
def p_array(p):
	'array : OPEN_SQT array_content CLOSE_SQT'
	p[0] = symbol_coder.c_concatenate(p)

def p_array_content(p):
	'''array_content : variable COMMA array_content
					 | value COMMA array_content
					 | variable
					 | value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)	

def p_hash(p):
	'hash : OPEN_BRACE hash_content CLOSE_BRACE'
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_content(p):
	'''hash_content : hash_key EQUAL LT hash_value
					 | IDENTIFIER COLON hash_value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_key(p):
	'''hash_key : value'''
	p[0] = p[1]

def p_hash_value(p):
	'''hash_value : value 
				| variable'''
	p[0] = p[1]	

def p_range(p):
	'''range : value PERIOD PERIOD value
	'''
	p[0] = symbol_coder.c_concatenate(p)





parser = yacc.yacc()

