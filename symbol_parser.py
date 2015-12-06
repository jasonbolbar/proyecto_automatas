import symbol_lexer
import symbol_coder
import ply.yacc as yacc

tokens = symbol_lexer.tokens

def p_symbol_ruby(p):
	'''symbol_ruby : method
				   | mult_cmd
				   | class
				   | module
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
	'method : DEF IDENTIFIER method_s OPEN_PARENTH method_p CLOSE_PARENTH mult_cmd END'
	p[0] = symbol_coder.c_method(p)

def p_method_s(p):
	'''method_s : EXCL_MARK
				| QU_MARK
				|
				'''
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_assig_cont(p):
	'method_p : IDENTIFIER EQUAL assign_value COMMA method_p'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_assig_end(p):
	'method_p : IDENTIFIER EQUAL assign_value'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_single_cont(p):
	'method_p : IDENTIFIER COMMA method_p'
	p[0] = symbol_coder.c_concatenate(p)

def p_method_pa_single_end(p):
	'''method_p : IDENTIFIER 
				|
				'''
	p[0] = symbol_coder.c_concatenate(p)

def p_multiple_cmd(p):
	'''mult_cmd : new_cmd mult_cmd
			   | new_cmd'''
	p[0] = symbol_coder.c_concatenate(p)		   

def p_new_cmd_single(p):
	'''new_cmd : ins 
	           | assig'''
	p[0] = symbol_coder.c_instructions(p)

def p_ins_single(p):
	'''ins : cmd
		   | cond_ins
		  '''
	p[0] = symbol_coder.c_concatenate(p)

def p_assig(p):
	'assig : variable assig_operator ins'
	p[0] = symbol_coder.c_concatenate(p)	

def p_assig_operator(p):
	'''assig_operator : OPERATOR EQUAL
	                | EQUAL '''
	p[0] = symbol_coder.c_concatenate(p)		

def p_cmd(p):
	'''cmd : method_call
		   | assign_value 
	       | assign_value PERIOD method_call
	       '''
	p[0] = symbol_coder.c_concatenate(p)		

def p_method_main(p):
	'''method_call : method_cl PERIOD method_call 
	               | method_cl
	               '''
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

def p_parameter_end(p):
	'''parameter : assign_value
				 |
				 '''
	p[0] = symbol_coder.c_concatenate(p)		

def p_parameter_def(p):
	'parameter : assign_value COMMA parameter'
	p[0] = symbol_coder.c_concatenate(p)


def p_cond_ins(p):
	'''cond_ins : if
				| unless
				| while
				| case
				'''	
	p[0] = symbol_coder.c_concatenate(p)		

def p_if_else_simple(p):
	'if : condition QU_MARK cmd COLON cmd'
	p[0] = symbol_coder.c_concatenate(p)

def p_if_complex(p):
	'if : IF mult_conds mult_cmd else_cond'
	p[0] = symbol_coder.c_if(p)

def p_unless_complex(p):
	'unless : UNLESS mult_conds mult_cmd else_cond'
	p[0] = symbol_coder.c_unless(p)

def p_else_conditional(p):
	'''else_cond : else
			   	 | END
			     '''	
	p[0] = symbol_coder.c_else_end(p)		     

def p_while_complex(p):
	'while : WHILE mult_conds mult_cmd END'
	p[0] = symbol_coder.c_while(p)

def p_case(p):
	'case : CASE condition case_when'
	p[0] = symbol_coder.c_case(p)

def p_case_when_cont(p):
	'case_when : WHEN condition mult_cmd case_when'
	p[0] = symbol_coder.c_case_when(p)


def p_case_when_end(p):
	'case_when : WHEN condition mult_cmd else'
	p[0] = symbol_coder.c_case_when(p)

def p_else_def(p):
	'else : ELSE mult_cmd END'
	p[0] = symbol_coder.c_else(p)

def p_condition(p):
	'''mult_conds : condition log_oper mult_conds
				  | condition
				  '''
	p[0] = symbol_coder.c_concatenate(p)

def p_condition_def(p):
	'''condition : cmd operator end_cond 
				 | end_cond
				 '''
	p[0] = symbol_coder.c_concatenate(p)

def p_end_condition(p):
	'end_cond : cmd'	
	p[0] = symbol_coder.c_condition(p)

def p_operator(p):
	'''operator : EQUAL EQUAL
				| EXCL_MARK EQUAL
				| GT
				| LT
				| GT EQUAL
				| LT EQUAL
				| GT EQUAL LT
				| EQUAL EQUAL EQUAL
				'''
	p[0] = symbol_coder.c_concatenate(p)

def p_logical_operator(p):
	'''log_oper : AND 
				| OR
				'''
	p[0] = symbol_coder.c_concatenate(p)		




def p_class(p):
	'class : CLASS CONSTANT inheritance symbol_ruby END'
	p[0] = symbol_coder.c_class(p)

def p_inheritance(p):
	'''inheritance : INHERITANCE CONSTANT
				   |
				   '''	
	p[0] = symbol_coder.c_inheritance(p)	

def p_module_def(p):
	'module : MODULE CONSTANT symbol_ruby END'
	p[0] = symbol_coder.c_module(p)		   

################################################ JASON IS WORKING HERE ############################################
def p_array(p):
	'array : OPEN_SQT array_content CLOSE_SQT'
	p[0] = symbol_coder.c_concatenate(p)

def p_array_content(p):
	'''array_content : assign_value COMMA array_content
					 | assign_value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)	

def p_hash(p):
	'hash : OPEN_BRACE hash_content CLOSE_BRACE'
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_content(p):
	'''hash_content : hash_key EQUAL LT assign_value
					 | IDENTIFIER COLON assign_value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_key(p):
	'''hash_key : value'''
	p[0] = p[1]

def p_assign_value(p):
	'''assign_value : value 
				    | variable'''
	p[0] = p[1]	






parser = yacc.yacc()

