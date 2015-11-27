def p_main(p):
	'symbol_ruby : class_def | module_def | method_def | ins'
	print p[1]

def p_method_main(p):
	'method_call : method_cl'
	print p[1]

def p_method_main_2(p):
	'method_call : IDENTIFIER block_def | method_cl block_def'
	print p[1] + p[2]

def p_method_cl(p):
	'method_cl : IDENTIFIER value'
	print p[1]

def p_method_cl_params(p):
	'method_cl : IDENTIFIER \'(\' parameter \')\' | IDENTIFIER \'(\' hash_pr \')\''
	print p[1] + p[2] + p[3] + p[4]

def p_hash_parameter(p):
	'hash_pr : IDENTIFIER \':\' value \',\' hash_pr'
	print p[1] + p[2] + p[3] + p[4]

def p_has_parameter_end(p):
	'hash_pr : IDENTIFIER \':\' value '
	print p[1] + p[2] + p[3]

def p_block_def(p):
	'block_def : DO \'|\' parameter \'|\' new_cmd'
	print p[1] + p[2] + p[3] + p[4] + p[5]

def p_block_def_simple(p):
	'block_def : \'{\' \'|\' parameter \'|\' ins \'}\''
	print p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_class_def(p):
	'class_def : CLASS name hierachy NEW_LINE TAB symbol_ruby'
	print p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_hierachy(p):
	'hierachy : HIERACHY name'
	print p[1] + p[2]

def p_hierachy_empty(p):
	'hierachy : '
	print p[1]

def p_module_def(p):
	'module_def : MODULE name NEW_LINE TAB symbol_ruby'
	print p[1] + p[2] + p[3] + p[4] + p[5]

def p_method_def(p):
	'method_def : DEF IDENTIFIER method_s \'(\' method_p \')\' new_cmd '
	print p[1] + p[2] + p[3] + p[4] + p[5] + p[7]

def p_method_s(p):
	'method_s : '!' | '?' | '
	print p[1]

def p_method_p_assig_cont(p):
	'method_p : IDENTIFIER \'=\' value \',\' method_p'
	print p[1] + p[2] + p[3] + p[4] + p[5]

def p_method_p_single_cont(p):
	'method_p : '









