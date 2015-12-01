def c_global_variable(p):
	if len(p) == 3:
		return p[1] + p[2]	
	else:
		return p[1]

def c_class_variable(p):
	return p[1] + p[2] + p[3]

def c_instance_variable(p):
	return p[1] + p[2]

def c_variable(p):
	return p[1]