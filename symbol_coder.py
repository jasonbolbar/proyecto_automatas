import pdb
def c_concatenate(p):
	return "".join([p[i] for i in range(1,len(p))])

def c_concatenate_by_index(p, begin, end):
	return "".join([p[i] for i in range(begin,end+1)])

def c_method(p):
	return 'def ' + c_concatenate_by_index(p,2,6) + '\n' + p[7] + 'end\n'	

def c_instructions(p):
	return p[1] + '\n'

def c_class(p):
	return 'class ' + p[2] + p[3] + '\n' + p[4] + 'end\n'

def c_inheritance(p):
	return ' ' + p[1] + ' ' + p[2]	

def c_module(p):
	return 'module ' + p[2]	+ '\n' + p[3] + 'end\n'

def c_replace_method_name(p):
	if p[1] == '&*&':
		return 'super'
	if p[1] == '<-':
		return 'return'
	if p[1] ==  '{>}':
		return 'yield'
	return p[1]

def c_block(p):
	if p[1] == '{+}':
		if len(p) == 4:
			return 'do ' + '\n' + p[2] + 'end'	
		else :
			return 'do ' + p[2] + '\n' + p[3] + 'end'	
	else:
		return c_concatenate(p)


################################################ JASON IS WORKING HERE ############################################
