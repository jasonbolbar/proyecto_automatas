def c_concatenate(p):
	return "".join([p[i] for i in range(1,len(p))])

def c_concatenate_by_index(p, begin, end):
	return "".join([p[i] for i in range(begin,end+1)])

def c_method(p):
	return 'def' + c_concatenate_by_index(p,2,9) + '\nend'	



################################################ JASON IS WORKING HERE ############################################
