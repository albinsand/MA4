"""
Solutions to module 2 - A calculator
Student: Albin Sand 
Mail: hansalbinsand@gmail.com
Reviewed by: Tom Smedsaas
Reviewed date: 2022-09-21
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from statistics import mean
from tokenize import TokenError
from winreg import REG_RESOURCE_REQUIREMENTS_LIST  
from MA2tokenizer import TokenizeWrapper


#######################################################
def fib(n):
    
    memory = {0:0, 1:1}

    def fib_mem (n):
        if n not in memory :
            memory [n] = fib_mem (n-1) + fib_mem (n-2)
        return memory [n]
    return fib_mem (n)


def fac(n):
    if n==0:
        return 1
    else :  
        return n*fac(n-1)

##################################################

class EvalutionError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if not wtok.is_at_end():
        raise SyntaxError("Expected end of line")

    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""

    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_number() :
            raise SyntaxError("Expected name')'")
        else:
            variables[str(wtok.get_current())] = result
            wtok.next()
    
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        else: 
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/': 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        else:
            try:
                wtok.next()
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                 raise EvalutionError("Divison by zero")

    return result

def arglist(wtok, variables):
    """ See syntax chart for arglist"""
    if wtok.get_current() == '(':
        wtok.next()
        result = [assignment(wtok,variables)]
        while wtok.get_current() == ',':
            wtok.next()
            result = result + [assignment(wtok,variables)]

    if wtok.get_current() != ')':       
        raise SyntaxError("Expected ')' or ','")

    wtok.next()
    return result
    


def factor(wtok, variables):
    """ See syntax chart for factor"""

    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
           
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.is_name():

        if wtok.get_current() in variables:
            result = variables[wtok.get_current()]
            wtok.next()

        elif wtok.get_current() in function_1:

            fu_1 = function_1[wtok.get_current()]
            wtok.next()

            if wtok.get_current() == '(':

                try:

                    wtok.next()
                    result = fu_1(assignment(wtok, variables))
                    wtok.next()

                except RecursionError:
                    raise EvalutionError("Maximum recursion depth exceeded")

                except ValueError:
                    raise EvalutionError("Math domain error")
           
            else:
                raise SyntaxError("Expected '('")

        elif wtok.get_current() in function_n:
        
            fu_n=function_n[wtok.get_current()]
            wtok.next()
            result = fu_n(arglist(wtok,variables))

        else:
            raise EvalutionError("Name not defiend: " + wtok.get_current())


    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)   

    else:
        raise SyntaxError("Not valied expression") 

    return result

function_1 = {'sin':math.sin,'cos':math.cos,'log':math.log,'exp':math.exp, 'fac':fac,'fib':fib}
function_n = {'min':min,'max':max,'sum':sum,'mean':mean}
         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}

    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except EvalutionError as se:
                print("*** EvalutionError: ", se)
                print("Undefined mathematical expression")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

    


if __name__ == "__main__":
    main()
