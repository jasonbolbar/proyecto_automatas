import symbol_lexer
import ply.yacc as yacc

tokens = symbol_lexer.tokens

def p_symbol_ruby(p):
	'''symbol_ruby : variable 
				   | array
	'''
	p[0] = p[1]

def p[]	

def p_variable(p):
	'''variable : IDENTIFIER 
	            | instance_variable 
	            | class_variable 
	            | global_variable'''
	p[0] = p[1]

def p_instance_variable(p):
	'''instance_variable : AT IDENTIFIER 
	                     | AT CONSTANT'''
	p[0] = p[1] + p[2]

def p_class_variable(p):
	'''class_variable : AT AT IDENTIFIER 
	                     | AT AT CONSTANT'''
	p[0] = p[1] + p[2] + p[3]

def p_global_variable(p):
	'''global_variable : DOLLAR IDENTIFIER
	                     | DOLLAR CONSTANT 
	                     | SPECIAL_VAR'''
	if len(p) == 3:
		p[0] = p[1] + p[2]	
	else:
		p[0] = p[1]


parser = yacc.yacc()

