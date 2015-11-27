def p_main(p):
	'symbol_ruby : class_def | module_def | method_def | ins'
	print p[1]

def p_method_main(p):
	'method_call : method_cl'
	p[0] = p[1]

def p_method_main_2(p):
	'method_call : IDENTIFIER block_def | method_cl block_def'
	p[0] = p[1] + p[2]

def p_method_cl(p):
	'method_cl : IDENTIFIER value'
	p[0] = p[1]

def p_method_cl_params(p):
	'method_cl : IDENTIFIER \'(\' parameter \')\' | IDENTIFIER \'(\' hash_pr \')\''
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_hash_parameter(p):
	'hash_pr : IDENTIFIER \':\' value \',\' hash_pr'
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_has_parameter_end(p):
	'hash_pr : IDENTIFIER \':\' value '
	p[0] = p[1] + p[2] + p[3]

def p_block_def(p):
	'block_def : DO \'|\' parameter \'|\' new_cmd'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_block_def_simple(p):
	'block_def : \'{\' \'|\' parameter \'|\' ins \'}\''
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_class_def(p):
	'class_def : CLASS name hierachy NEW_LINE TAB symbol_ruby'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_hierachy(p):
	'hierachy : HIERACHY name'
	p[0] = p[1] + p[2]

def p_hierachy_empty(p):
	'hierachy : '
	p[0] = p[1]

def p_module_def(p):
	'module_def : MODULE name NEW_LINE TAB symbol_ruby'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_method_def(p):
	'method_def : DEF IDENTIFIER method_s \'(\' method_p \')\' new_cmd '
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[7]

def p_method_s(p):
	'method_s : \'!\' | \'?\' | '
	p[0] = p[1]

def p_method_pa_assig_cont(p):
	'method_p : IDENTIFIER \'=\' value \',\' method_p'
	p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_method_pa_single_cont(p):
	'method_p : IDENTIFIER \',\' method_p'
	p[0] = p[1] + p[2] + p[3]

def p_method_pa_assig_end(p):
	'method_p : IDENTIFIER \'=\' value'
	p[0] = p[1] + p[2] + p[3]

def p_method_pa_single_end(p):
	'method_p : IDENTIFIER'
	p[0] = p[1]

def	p_ins_single(p):
	'ins : cmd | exception_def | cond_ins | assig'
	p[0] = p[1]

def p_inst(p):
	'ins : NEW_LINE ins'
	p[0] = p[1] + p[2]

def p_cond_ins(p):
	'cond_ins : if_def | unless_def | while_def | case_def'
	p[0] = p[1]

def p_cmd_single(p):
	'cmd : method_call | vars'
	p[0] = p[1]

def p_cmd(p):
	'cmd : vars \'.\' cmd'
	p[0] = p[1] + p[2] + p[3]

def p_assig(p):
	'assig : vars ASSIGNATION_OPERATORS cmd | vars ASSIGNATION_OPERATORS value'
	p[0] = p[1] + p[2] + p[3]

def p_if_def_complex(p):
	'if_def : if_inst else_def'
	p[0] = p[1] + p[2]

def p_if_def_simple(p):
	'if_def : condition \'?\' ins \':\' ins'
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
	'case_stmt : vars | value'
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
	'rescue : RESCUE vars \'=>\' name new_cmd'
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_condition_single(p):
	'condition : value | vars'
	p[0] = p[1]

def p_condition_def(p):
	'condition : value operator | vars operator'
	p[0] = p[1] + p[2]

def p_parameter_end(p):
	'parameter : value'
	p[0] = p[1]

def p_parameter_def(p):
	'parameter : value \',\' parameter'
	p[0] = p[1] + p[2] + p[3]

def p_value(p):
	'value : STRING | FIXNUM | NIL | FLOAT | ARRAY | HASH | SYMBOL | TRUE | FALSE'
	p[0] = p[1]

def p_name_single(p):
	'name : CONSTANT'
	p[0] = p[1]

def p_name_complex(p):
	'name : CONSTANT NAMESPACE_CHARACTER name'
	p[0] = p[1] + p[2] + p[3]

def p_operator(p):
	'operator : LOGICAL_OPERATORS | COMPARATOR_OPERATORS | OPERATORS'
	p[0] = p[1]

def p_vars(p):
	'vars : INSTACE_VAR | CLASS_VAR | GLOBAL_VAR | PREDEF_VAR'
	p[0] = p[1]

def p_new_cmd(p):
	'new_cmd : NEW_LINE TAB ins'
	p[0] = p[1] + p[2] + p[3]



