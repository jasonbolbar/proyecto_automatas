import symbol_lexer
import symbol_coder
import ply.yacc as yacc
import pdb

tokens = symbol_lexer.tokens

def p_symbol_ruby(p):

	'''symbol_ruby : method symbol_ruby
				   | new_cmd symbol_ruby
				   | class symbol_ruby
				   | module symbol_ruby
				   | __FILE__ symbol_ruby
				   | __LINE__ symbol_ruby
				   | __DIR__ symbol_ruby
				   | method
				   | new_cmd
				   | class
				   | module
				   | __LINE__
				   | __DIR__
				   | __FILE__
	'''
	p[0] = symbol_coder.c_concatenate(p)
	

def p_variable(p):
	'''variable : IDENTIFIER 
	      | instance_variable 
	      | class_variable 
	      | global_variable
	      | SELF
	      '''
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
	'''
	p[0] = symbol_coder.c_concatenate(p)
  

def p_method(p):
	'method : DEF IDENTIFIER method_s OPEN_PARENTH method_p CLOSE_PARENTH mult_cmd END'
	p[0] = symbol_coder.c_method(p)


def p_pipe_params(p):
	'''pipe_params : PIPE parameter PIPE
				   '''
	p[0] = symbol_coder.c_concatenate(p)

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
	           | assig
	           | COMMENT
	           '''
	p[0] = symbol_coder.c_instructions(p)

def p_ins_single(p):
	'''ins : cmd
		   | cond_ins
		   | exception
		   | assign_value
		   | arithmetical_operation
		  '''
	p[0] = symbol_coder.c_concatenate(p)

def p_assig(p):
	'''assig : variable EQUAL cmd
			 | variable EQUAL assign_value
			 | CONSTANT EQUAL cmd
			 | CONSTANT EQUAL assign_value
			 | variable PERIOD attribute_call EQUAL cmd
			 | variable PERIOD attribute_call EQUAL assign_value
			 | variable EQUAL variable PERIOD attribute_call 
			 | variable PERIOD attribute_call EQUAL variable PERIOD attribute_call 
	'''

	p[0] = symbol_coder.c_concatenate(p)

def p_attribute_call(p):
	'''
	attribute_call : IDENTIFIER PERIOD attribute_call
				   | IDENTIFIER
	'''

	p[0] = symbol_coder.c_concatenate(p)

def p_cmd(p):
	'''cmd : method_call
		   | namespace PERIOD method_call
	       | variable PERIOD method_call
	       '''
	p[0] = symbol_coder.c_concatenate(p)		

def p_method_main(p):
	'''method_call : method_cl PERIOD method_call 
	               | method_cl
	               | method_block
	               '''
	p[0] = symbol_coder.c_concatenate(p)

def p_method_cl_params(p):
	'''method_cl : method_call_name OPEN_PARENTH method_call_parameters CLOSE_PARENTH
				 '''
	p[0] = symbol_coder.c_concatenate(p)

def p_method_block_params(p):
	'''method_block : method_cl block_do
				 	'''
	p[0] = symbol_coder.c_concatenate(p)	

def p_block_do(p):
	'''block_do : DO pipe_params mult_cmd END
			    | DO mult_cmd END
				'''
	p[0] = symbol_coder.c_block(p)

def p_method_call_parameters(p):
	'''
	method_call_parameters : parameter 
						   | hash_pr
	'''
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_parameter(p):
	'hash_pr : IDENTIFIER COLON value COMMA hash_pr'
	p[0] = symbol_coder.c_concatenate(p)


def p_has_parameter_end(p):
	'hash_pr : IDENTIFIER COLON value'
	p[0] = symbol_coder.c_concatenate(p)

def p_parameter_end(p):
	'''parameter : ins
				 |
				 '''
	p[0] = symbol_coder.c_concatenate(p)		

def p_parameter_def(p):
	'parameter : ins COMMA parameter'
	p[0] = symbol_coder.c_concatenate(p)


def p_method_call_name(p):
	''' method_call_name : IDENTIFIER
						 | SUPER 
						 | YIELD 
	                     | RETURN 
	                     | ALIAS 
	                     | RAISE
	                     | NOT
	                     | UNDEF
	                     | BREAK
	                     | RETRY
	                     | REDO
	                     | NEXT
	                     '''
	p[0] = symbol_coder.c_replace_method_name(p)

def p_cond_ins(p):
	'''cond_ins : if
				| unless
				| while
				| case
				'''	
	p[0] = symbol_coder.c_concatenate(p)		

def p_if_else_simple(p):
	'''if : condition QU_MARK cmd COLON cmd
		  | condition QU_MARK assign_value COLON assign_value'''
	p[0] = symbol_coder.c_concatenate(p)

def p_if_complex(p):
	'if : IF mult_conds mult_cmd elsif else_cond END'
	p[0] = symbol_coder.c_if(p)

def p_unless_complex(p):
	'unless : UNLESS mult_conds mult_cmd else_cond END'
	p[0] = symbol_coder.c_unless(p)

def p_elsif(p):
	'''
	elsif : ELSIF mult_conds mult_cmd elsif
		  | 
	'''
	p[0] = symbol_coder.c_elsif(p)

def p_else_conditional(p):
	'''else_cond : else
			   	 |
			     '''	
	p[0] = symbol_coder.c_concatenate(p)		     

def p_while_complex(p):
	'while : while_word mult_conds mult_cmd END'
	p[0] = symbol_coder.c_while(p)

def p_while_word(p):
	'''while_word : WHILE
				  | UNTIL
				  '''
	p[0] = symbol_coder.c_concatenate(p)			  

def p_case(p):
	'case : CASE condition case_when END'
	p[0] = symbol_coder.c_case(p)

def p_case_when_cont(p):
	'case_when : WHEN condition mult_cmd case_when'
	p[0] = symbol_coder.c_case_when(p)


def p_case_when_end(p):
	'case_when : WHEN condition mult_cmd else'
	p[0] = symbol_coder.c_case_when(p)

def p_else(p):
	'else : ELSE mult_cmd'
	p[0] = symbol_coder.c_else(p)

def p_condition(p):
	'''mult_conds : condition log_oper mult_conds
				  | condition
				  '''
	p[0] = symbol_coder.c_concatenate_with_character(p,' ')

def p_condition_def(p):
	'''condition : cmd operator cmd 
				 | cmd operator variable
				 | value operator value
				 | variable operator cmd
				 | variable operator variable
				 | variable operator value
				 | value operator variable
				 | cmd
				 | assign_value
				 '''
	p[0] = symbol_coder.c_concatenate_with_character(p,' ')

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


def p_exception(p):
	'''exception : BEGIN mult_cmd RESCUE rescue mult_cmd else_cond ensure END '''
	p[0] = symbol_coder.c_exception(p)

def p_rescue(p):
	'''rescue : CONSTANT
				| CONSTANT EXC_OP variable
				'''
	p[0] = symbol_coder.c_rescue(p)

def p_ensure(p):
	'''ensure : ENSURE mult_cmd
			 |
			 '''
	p[0] = symbol_coder.c_ensure(p)		 

def p_class(p):
	'class : CLASS namespace inheritance symbol_ruby END'
	p[0] = symbol_coder.c_class(p)

def p_inheritance(p):
	'''inheritance : INHERITANCE namespace
				   |
				   '''	
	p[0] = symbol_coder.c_inheritance(p)	

def p_module_def(p):
	'module : MODULE namespace symbol_ruby END'
	p[0] = symbol_coder.c_module(p)		   

def p_array(p):
	'array : OPEN_SQT array_content CLOSE_SQT'
	p[0] = symbol_coder.c_concatenate(p)

def p_array_content(p):
	'''array_content : cmd COMMA array_content
					 | cmd
					 | assign_value COMMA array_content
					 | assign_value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)	

def p_hash(p):
	'hash : OPEN_BRACE hash_content CLOSE_BRACE'
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_content(p):
	'''hash_content : hash_key EQUAL LT cmd COMMA hash_content
					 | IDENTIFIER COLON cmd COMMA hash_content
					 | hash_key EQUAL LT assign_value COMMA hash_content
					 | IDENTIFIER COLON assign_value COMMA hash_content
					 | hash_key EQUAL LT cmd
					 | IDENTIFIER COLON cmd
					 | hash_key EQUAL LT assign_value
					 | IDENTIFIER COLON assign_value
					 |
					 '''
	p[0] = symbol_coder.c_concatenate(p)

def p_hash_key(p):
	'''hash_key : value'''
	p[0] = symbol_coder.c_concatenate(p)

def p_assign_value(p):
	'''assign_value : value 
				    | variable
				    '''
	p[0] = symbol_coder.c_concatenate(p)

def p_arithmetical_operation(p):
	'''
	arithmetical_operation : cmd OPERATOR arithmetical_operation
						   | assign_value OPERATOR arithmetical_operation
						   | cmd OPERATOR assign_value
						   | assign_value OPERATOR cmd 
						   | cmd OPERATOR cmd
						   | assign_value OPERATOR assign_value
	'''
	p[0] = symbol_coder.c_concatenate(p)

def p_namespace(p):
	'''
	namespace : CONSTANT COLON COLON namespace
			  | CONSTANT
	'''
	p[0] = symbol_coder.c_concatenate(p)


def p_error(p):
	print("Syntax error at token {} in line {}".format(p.value,p.lineno))	






parser = yacc.yacc()

