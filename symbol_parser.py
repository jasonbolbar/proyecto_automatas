import symbol_lexer
import symbol_coder
import ply.yacc as yacc

tokens = symbol_lexer.tokens

def p_symbol_ruby(p):
	'''symbol_ruby : variable
	'''
	p[0] = p[1]
	

def p_variable(p):
	'''variable : IDENTIFIER 
	            | instance_variable 
	            | class_variable 
	            | global_variable'''
	p[0] = symbol_coder.c_variable(p)

def p_instance_variable(p):
	'''instance_variable : AT IDENTIFIER 
	                     | AT CONSTANT'''
	p[0] = symbol_coder.c_instance_variable(p)

def p_class_variable(p):
	'''class_variable : AT AT IDENTIFIER 
	                     | AT AT CONSTANT'''
	p[0] = symbol_coder.c_class_variable(p)

def p_global_variable(p):
	'''global_variable : DOLLAR IDENTIFIER
	                     | DOLLAR CONSTANT 
	                     | SPECIAL_VAR'''
	p[0] = symbol_coder.c_global_variable(p)                    
	


parser = yacc.yacc()

