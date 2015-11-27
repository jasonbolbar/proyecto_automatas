%token IDENTIFIER DO CLASS HIERACHY MODULE DEF VALUE ASSIGNATION_OPERATORS
%token IF ELSE UNLESS WHILE FOR IN RANGE ARRAY CASE INSTR WHEN BEGIN RESCUE
%token RESCUE STRING FIXNUM NIL FLOAT HASH SYMBOL TRUE FALSE CONSTANT NAMESPACE_CHARACTER
%token LOGICAL_OPERATORS COMPARATOR_OPERATORS OPERATORS NEW_LINE TAB
%token INSTACE_VAR CLASS_VAR GLOBAL_VAR PREDEF_VAR 

%start symbol_ruby

%%

symbol_ruby : class_def | module_def | method_def | ins ;
method_call : method_cl | IDENTIFIER block_def | method_cl block_def ;
method_cl : IDENTIFIER value | IDENTIFIER '(' parameter ')' | IDENTIFIER '(' hash_pr ')' ;
hash_pr : IDENTIFIER ':' value ',' hash_pr | IDENTIFIER ':' value ;
block_def : DO '|' parameter '|' new_cmd | '{' '|' parameter '|' ins '}' ;
class_def : CLASS name hierachy NEW_LINE TAB symbol_ruby ;
hierachy : HIERACHY name | ;
module_def : MODULE name NEW_LINE TAB symbol_ruby ;
method_def : DEF IDENTIFIER method_s '(' method_p ')' new_cmd ; 
method_s : '!' | '?' | ;
method_p : IDENTIFIER '=' value ',' method_p | IDENTIFIER ',' method_p | IDENTIFIER '=' value | IDENTIFIER ;
ins : cmd | exception_def | cond_ins  | assig | NEW_LINE ins ; 
cond_ins : if_def | unless_def | while_def | case_def ;
cmd : method_call | vars | vars '.' cmd ;
assig : vars ASSIGNATION_OPERATORS cmd | vars ASSIGNATION_OPERATORS value ;
if_def : if_inst else_def | condition '?' ins ':' ins ;
if_inst : IF condition new_cmd ;
unless_def : UNLESS condition new_cmd ;
while_def : WHILE condition new_cmd ;
else_def : ELSE new_cmd | ;
case_def : CASE case_stmt case_when ;
case_stmt : vars | value ;
case_when : WHEN condition new_cmd | WHEN condition new_cmd case_when ;
exception_def : BEGIN new_cmd rescue ;
rescue : RESCUE name new_cmd | RESCUE vars '=>' name new_cmd ;
condition : value operator | value | vars operator | vars ;
parameter : value ',' parameter | value ;
value : STRING | FIXNUM | NIL | FLOAT | ARRAY | HASH | SYMBOL | TRUE | FALSE ;
name : CONSTANT | CONSTANT NAMESPACE_CHARACTER name ;
operator : LOGICAL_OPERATORS | COMPARATOR_OPERATORS | OPERATORS ;
vars : INSTACE_VAR | CLASS_VAR | GLOBAL_VAR | PREDEF_VAR ;
new_cmd : NEW_LINE TAB ins ;
