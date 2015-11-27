# imports 
import ply.lex as lex
import ply.yacc as yacc

tokens = ('IDENTIFIER', 'DO', 'CLASS', 'HIERACHY', 'MODULE', 'DEF', 'VALUE', 'ASSIGNATION_OPERATORS',
 'IF', 'ELSE', 'UNLESS', 'WHILE', 'RANGE', 'ARRAY', 'CASE', 'INSTR', 'WHEN', 'BEGIN', 
 'RESCUE', 'STRING', 'FIXNUM', 'NIL', 'FLOAT', 'HASH', 'SYMBOL', 'TRUE', 'FALSE', 'CONSTANT', 
 'NAMESPACE_CHARACTER','LOGICAL_OPERATORS', 'COMPARATOR_OPERATORS', 'OPERATORS', 'NEW_LINE', 'TAB',
 'INSTACE_VAR', 'CLASS_VAR', 'GLOBAL_VAR', 'PREDEF_VAR'
 )

import lexer

lex.lex()

import parser

yacc.yacc()