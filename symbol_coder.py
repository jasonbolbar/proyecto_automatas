import pdb
def c_concatenate(p):
	return "".join([p[i] for i in range(1,len(p))if p[i] != ''])

def c_concatenate_by_index(p, begin, end):
	return "".join([p[i] for i in range(begin,end+1)])

def c_method(p):
	return 'def ' + c_concatenate_by_index(p,2,6) + '\n' + p[7] + 'end\n' + p[8]	

def c_instructions(p):
	return p[1] + '\n'

def c_class(p):
	return 'class ' + p[2] + p[3] + '\n' + p[4] + 'end\n' + p[6]

def c_inheritance(p):
	if len(p) == 1:
		return ''
	else:
		return ' ' + '<' + ' ' + p[2]	

def c_module(p):
	return 'module ' + p[2]	+ '\n' + p[3] + 'end\n' + p[5]


def c_replace_method_name(p):
	if p[1] == '&*&':
		return 'super'
	if p[1] == '<-':
		return 'return'
	if p[1] ==  '{>}':
		return 'yield'
	if p[1] == '%':
		return 'raise'
	return p[1]

def c_block(p):
	if len(p) == 1:
		return ''
	else:
		if p[1] == '{+}':
			if len(p) == 4:
				return 'do ' + '\n' + p[2] + 'end'	
			else :
				return 'do ' + p[2] + '\n' + p[3] + 'end'	
		else:
			return c_concatenate(p)

def c_if(p):
	return 'if ' + p[2] + p[3] + 'end\n'

def c_unless(p):
	return 'if ' + p[2] + p[3] + 'end\n'

def c_elsif(p):
	if len(p) == 1:
		return ''
	else:
		if p[4] == '':
			return 'elsif ' + p[2] + '\n' + p[3]
		else:
			return 'elsif ' + p[2] + '\n' + p[3]  + '\n' + p[4]  		

def c_while(p):
	return 'while ' + p[2] + p[3] + 'end\n'

def c_case(p):
	return 'case ' + p[2] + p[3]

def c_case_when(p):
	return 'when ' + c_concatenate_by_index(p,2,len(p)-1) 	

def c_else(p):
	return 'else\n' + p[2]	

def c_exception(p):
	return 'begin\n' + p[2] + 'rescue ' + p[4] + '\n' + p[5] + p[6] + 'end\n'		

def c_rescue(p):	
	if len(p) > 2:
		return p[1] + ' => ' + p[3]
	elif len(p) == 2:
		return p[1]	
	else:
		return ''	

def c_ensure(p):
	if len(p) == 1:
		return ''
	else:	
		return 'ensure\n' + p[2]	



