#imports
import ply.lex as lex

############################ PALABRAS RESERVADAS ###########################

RESERVED = {
'__FILE__':'__FILE__',
'__LINE__':'__LINE__',
'__dir__':'__DIR__',
'and':'AND',
'or':'OR',
'in':'IN',
'self':'SELF',
'redo':"REDO",
'false':'FALSE',
'nil':'NIL',
'retry':'RETRY',
'true':'TRUE',
'alias':'ALIAS',
'not':'NOT',
'undef':'UNDEF'
}


################################## TOKENS ##################################

tokens = ('__FILE__','__LINE__','IDENTIFIER','COMMENT','DEF','END','UNLESS',
	'IF','AND','OR','IN','BEGIN','ENSURE','REDO','SUPER','BREAK','DO','FALSE',
	'NEXT','THEN','WHEN','CASE','ELSE','FOR','NIL','RETRY','WHILE','ALIAS',
	'CLASS','ELSIF','NOT','RETURN','UNDEF','CONSTANT','YIELD','FIXNUM',
	'FLOAT','STRING','HASH','SYMBOL', 'RANGE', 'OPERATOR','PIPE','COMMA',
	'EQUAL','COLON','QU_MARK','EXCL_MARK','OPEN_PARENTH','CLOSE_PARENTH','OPEN_BRACE',
	'CLOSE_BRACE','SEMICOLON','PERIOD','SPACE','MODULE','RESCUE','TRUE','GT','LT','SPECIAL_VAR',
	'__DIR__','DOLLAR','AT','UNTIL','OPEN_SQT','CLOSE_SQT','SPECIAL_NUM', 'SELF'
	)


################################## ANALISIS LEXICO ############################################

t_COMMENT = r'[ ]*\043[^\n]*'
t_DEF = r'\$->'
t_END = r'\<\$\>'
t_IF = r'\?\?'
t_UNLESS = r'\?-'
t_AND = r'&&'
t_OR = r'\|\|'
t_BEGIN = r'\^%'
t_ENSURE = r'>;'
t_MODULE = r'<@@>'
t_SUPER = r'&\*&'
t_BREAK = r'>\.<'
t_DO = r'{\+}'
t_FALSE = r'FALSE'
t_NEXT = r'~@'
t_RESCUE = r'%\^'
t_THEN = r'>-'
t_WHEN = r'~:'
t_CASE = r'>:'
t_ELSE = r'\?@' 
t_FOR = r'{\#}'
t_TRUE = r'TRUE'
t_WHILE = r'\[\?\]'
t_UNTIL = r'\]\?\['
t_CLASS = r'<@>'
t_ELSIF = r'\?@\?'
t_RETURN = r'<\-'
t_CONSTANT = r'[A-Z](\w)*'
t_YIELD = r'{>}'

def t_IDENTIFIER(t):
    r'([a-z]|\_)(\w)*'
    t.type = RESERVED.get(t.value, "IDENTIFIER")
    return t

#### LITERALES ####

t_FLOAT = r'[-+]?[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?'
t_FIXNUM = r'[-+]?[1-9]+(\_[0-9]+)*'
t_STRING = r'\"([^\\"](\\")?(\\)?)*\"|\'([^\'](\\\\)?(\\\')?)*\''
t_SYMBOL = r'\:([A-Z](\w)+|([a-z]|\_)(\w)*)'
t_SPECIAL_NUM = r'[-+]?0((x|X)([0-9]|[a-f]|[A-F])+|(b|B)([0-1])+|([0-7]+))'

#### OPERADORES ####

t_OPERATOR = r'\+|\-|\*\*?|\/'
t_PIPE = r'\|'
t_COMMA = r'\,'
t_EQUAL = r'\='
t_COLON = r'\:'
t_QU_MARK = r'\?'
t_EXCL_MARK = r'\!'
t_OPEN_PARENTH = r'\('
t_CLOSE_PARENTH = r'\)'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_OPEN_SQT = r'\['
t_CLOSE_SQT = r'\]'
t_PERIOD = r'\.'
t_SEMICOLON = r'\;'
t_SPACE = r'[ ]+'
t_GT = r'<'
t_LT = r'>'
t_DOLLAR = r'\$'
t_AT = r'@'
t_SPECIAL_VAR = r'\$(!|@|&|`|\'|\+|[0-9]|~|=|/|\\|,|;|\.|<|>|_|\*|\$|\?|:|\"|-d|-K|-v|-a|-i|-l|-p|-w)'


#### IGNORADOS ####

def t_newline(t):
    r'\n+'
    pass

def t_tab(t):
    r'\t+'
    pass    

def t_error(t):
    print t
    t.lexer.skip(1)

lexer = lex.lex()    