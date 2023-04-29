import sys
import numpy as np
from antlr4 import *
from LittleDuckLexer import LittleDuckLexer
from LittleDuckParser import LittleDuckParser
from LittleDuckListener import LittleDuckListener
from enum import IntEnum

# memory allocated for variables
N = 5000
INTMIN = -2147483648
pilaTipos = list()
# var_table -> nombre: (tipo, valor)
var_table = {}
pilaOperadores = list()
# addresses
pilaOperandos = list()
pilaSaltos = list()
# operador, var1, var2, result
cuadruplos = list()
dirInts = 1000
dirFloat = 2000
dirCte_int = 3000
dirCte_float = 3500
dirBool = 4000
dirCte_str = 5000
constantes = {}

###### CUBO SEMANTICO ######
class Type(IntEnum):
    INVALID = 0
    INT = 1
    FLOAT = 2
    BOOL = 3
    STRING = 4

class Operator(IntEnum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVISION = 4
    LESSTHAN = 5
    MORETHAN = 6
    NOT = 7
    PAREN = 8
    EQUAL = 9
    GOTOF = 10
    GOTOV = 11
    PRINT = 12

cube = np.zeros((6, 6, 13))
cube[Type.INT][Type.INT][Operator.PLUS] = Type.INT # int + int = int
cube[Type.INT][Type.INT][Operator.MINUS] = Type.INT  # int - int = int
cube[Type.INT][Type.INT][Operator.TIMES] = Type.INT # int * int = int
cube[Type.INT][Type.INT][Operator.DIVISION] = Type.INT  # int / int = int
cube[Type.INT][Type.INT][Operator.LESSTHAN] = Type.BOOL  # int < int = bool
cube[Type.INT][Type.INT][Operator.MORETHAN] = Type.BOOL # int > int = bool
cube[Type.INT][Type.INT][Operator.NOT] = Type.BOOL # int <> int = bool
cube[Type.INT][Type.INT][Operator.EQUAL] = Type.INT # int = int -> int

cube[Type.INT][Type.FLOAT][Operator.PLUS] = Type.FLOAT  # int + float = float
cube[Type.INT][Type.FLOAT][Operator.MINUS] = Type.FLOAT # int - float = float
cube[Type.INT][Type.FLOAT][Operator.TIMES] = Type.FLOAT # int * float = float
cube[Type.INT][Type.FLOAT][Operator.DIVISION] = Type.FLOAT # int / float = float
cube[Type.INT][Type.FLOAT][Operator.LESSTHAN] = Type.BOOL # int < float = bool
cube[Type.INT][Type.FLOAT][Operator.MORETHAN] = Type.BOOL # int > float = bool
cube[Type.INT][Type.FLOAT][Operator.NOT] = Type.BOOL # int <> float = bool
cube[Type.INT][Type.FLOAT][Operator.EQUAL] = Type.FLOAT # int = float -> float

cube[Type.FLOAT][Type.INT][Operator.PLUS] = Type.FLOAT # float + int = float
cube[Type.FLOAT][Type.INT][Operator.MINUS] = Type.FLOAT # float - int = float
cube[Type.FLOAT][Type.INT][Operator.TIMES] = Type.FLOAT # float * int = float
cube[Type.FLOAT][Type.INT][Operator.DIVISION] = Type.FLOAT # float / int = float
cube[Type.FLOAT][Type.INT][Operator.LESSTHAN] = Type.BOOL # float < int = bool
cube[Type.FLOAT][Type.INT][Operator.MORETHAN] = Type.BOOL # float > int = bool
cube[Type.FLOAT][Type.INT][Operator.NOT] = Type.BOOL # float <> int = bool
cube[Type.FLOAT][Type.INT][Operator.EQUAL] = Type.FLOAT # float = int -> float

cube[Type.FLOAT][Type.FLOAT][Operator.PLUS] = Type.FLOAT # float + float = float
cube[Type.FLOAT][Type.FLOAT][Operator.MINUS] = Type.FLOAT # float - float = float
cube[Type.FLOAT][Type.FLOAT][Operator.TIMES] = Type.FLOAT # float * float = float
cube[Type.FLOAT][Type.FLOAT][Operator.DIVISION] = Type.FLOAT # float / float = float
cube[Type.FLOAT][Type.FLOAT][Operator.LESSTHAN] = Type.BOOL# float < float = bool
cube[Type.FLOAT][Type.FLOAT][Operator.MORETHAN] = Type.BOOL # float > float = bool
cube[Type.FLOAT][Type.FLOAT][Operator.NOT] = Type.BOOL # float <> float = bool
cube[Type.FLOAT][Type.FLOAT][Operator.EQUAL] = Type.FLOAT # float = float -> float

def getAddressByType(tipo):
    global dirInts
    global dirFloat
    global dirBool
    if tipo == Type.INT:
        dirInts = dirInts + 1
        return dirInts - 1
    elif tipo == Type.FLOAT:
        dirFloat = dirFloat + 1
        return dirFloat - 1
    elif tipo == Type.BOOL:
        dirBool = dirBool + 1
        return dirBool - 1

# custom listener
class ProgramaListener(LittleDuckListener):
    def exitExit_plus(self, ctx: LittleDuckParser.Exit_plusContext):
        pilaOperadores.append(Operator.PLUS)

    def exitExit_minus(self, ctx: LittleDuckParser.Exit_minusContext):
        pilaOperadores.append(Operator.MINUS)

    def exitExit_times(self, ctx: LittleDuckParser.Exit_timesContext):
        pilaOperadores.append(Operator.TIMES)

    def exitExit_division(self, ctx: LittleDuckParser.Exit_divisionContext):
        pilaOperadores.append(Operator.DIVISION)
    
    def exitExit_morethan(self, ctx: LittleDuckParser.Exit_morethanContext):
        pilaOperadores.append(Operator.MORETHAN)

    def exitExit_lessthan(self, ctx: LittleDuckParser.Exit_lessthanContext):
        pilaOperadores.append(Operator.LESSTHAN)

    def exitExit_not(self, ctx: LittleDuckParser.Exit_notContext):
        pilaOperadores.append(Operator.NOT)

    def exitExit_openp(self, ctx: LittleDuckParser.Exit_openpContext):
        pilaOperadores.append(Operator.PAREN)

    def exitExit_closep(self, ctx: LittleDuckParser.Exit_closepContext):
        pilaOperadores.pop()

    def exitExit_equals(self, ctx: LittleDuckParser.Exit_equalsContext):
        pilaOperadores.append(Operator.EQUAL)

    def fill(self,  end: int, next: int):
        c = cuadruplos[end]
        c = (c[0], c[1], c[2], next)
        cuadruplos[end] = c

    def exitVar_cte(self, ctx: LittleDuckParser.Var_cteContext):
        global dirCte_int
        global dirCte_float
        if ctx.CTE_I() is not None:
            cteInt = int(ctx.getText())
            if cteInt in constantes:
                address = constantes[cteInt]
            else:
                address = dirCte_int
                constantes[cteInt] = address
                dirCte_int = dirCte_int + 1
            pilaOperandos.append(address)
            pilaTipos.append(Type.INT)
        elif ctx.CTE_F() is not None:
            cteFloat = float(ctx.getText())
            if cteFloat in constantes:
                address = constantes[cteFloat]
            else:
                address = dirCte_float
                constantes[cteFloat] = address
                dirCte_float = dirCte_float + 1
            pilaOperandos.append(address)
            pilaTipos.append(Type.FLOAT)
        elif ctx.ID() is not None:
            varID = ctx.getText()
            if varID in var_table:
                tipo = var_table[varID][0]
                pilaOperandos.append(var_table[varID][1])
                pilaTipos.append(tipo)
            else:
                raise Exception("Variable no declarada... what -> " + ctx.getText())

    def exitExit_factor(self, ctx: LittleDuckParser.Exit_factorContext):
        if not len(pilaOperadores) == 0:
            if pilaOperadores[-1] == Operator.TIMES or pilaOperadores[-1] == Operator.DIVISION:
                right_operand = pilaOperandos.pop()
                right_type = pilaTipos.pop()
                left_operand = pilaOperandos.pop()
                left_type = pilaTipos.pop()
                operador = pilaOperadores.pop()

                result_type = Type(cube[left_type][right_type][operador])
                if result_type == Type.INVALID:
                    raise Exception("Type mismatch")
                else:
                    direccion_result = getAddressByType(result_type)
                    cuadruplos.append((operador, left_operand, right_operand, direccion_result))
                    pilaOperandos.append(direccion_result)
                    pilaTipos.append(result_type)

    def exitExit_termino(self, ctx):
        if not len(pilaOperadores) == 0:
            if pilaOperadores[-1] == Operator.PLUS or pilaOperadores[-1] == Operator.MINUS:
                right_operand = pilaOperandos.pop()
                right_type = pilaTipos.pop()
                left_operand = pilaOperandos.pop()
                left_type = pilaTipos.pop()
                operador = pilaOperadores.pop()

                result_type = Type(cube[left_type][right_type][operador])
                if result_type == Type.INVALID:
                    raise Exception("Type mismatch")
                else:
                    direccion_result = getAddressByType(result_type)
                    cuadruplos.append((operador, left_operand, right_operand, direccion_result))
                    pilaOperandos.append(direccion_result)
                    pilaTipos.append(result_type)
    
    def exitExit_exp(self, ctx):
        if not len(pilaOperadores) == 0:
            if pilaOperadores[-1] == Operator.MORETHAN or pilaOperadores[-1] == Operator.LESSTHAN or pilaOperadores[-1] == Operator.NOT:
                right_operand = pilaOperandos.pop()
                right_type = pilaTipos.pop()
                left_operand = pilaOperandos.pop()
                left_type = pilaTipos.pop()
                operador = pilaOperadores.pop()

                result_type = Type(cube[left_type][right_type][operador])
                if result_type == Type.INVALID:
                    raise Exception("Type mismatch")
                else:
                    direccion_result = getAddressByType(result_type)
                    cuadruplos.append((operador, left_operand, right_operand, direccion_result))
                    pilaOperandos.append(direccion_result)
                    pilaTipos.append(result_type)

    def exitAsigna(self, ctx):
        varIds = ctx.getTokens(LittleDuckParser.ID)

        for token in varIds:
            if not token.getText() in var_table:
                raise Exception("Variable no declarada : " + token.getText())

        if not len(pilaOperadores) == 0:
            if pilaOperadores[-1] == Operator.EQUAL:
                right_operand = pilaOperandos.pop()
                right_type = pilaTipos.pop()
                left_operand = pilaOperandos.pop()
                left_type = pilaTipos.pop()
                operador = pilaOperadores.pop()

                result_type = Type(cube[left_type][right_type][operador])
                if result_type == Type.INVALID:
                    raise Exception("Type mismatch")
                cuadruplos.append((operador, left_operand, right_operand, left_operand))        

    def exitAsigna_var(self, ctx):
        if ctx.ID() is not None:
            varname = ctx.getText()
            if not varname in var_table:
                raise Exception(varname + " Variable no declarada")

            direccion = var_table[varname][1]
            pilaOperandos.append(direccion)
            pilaTipos.append(var_table[varname][0])

    def exitPnvar(self, ctx):
        pilaTipos.pop()

    def exitExit_si(self, ctx):
        tipoExp = pilaTipos.pop()
        res = pilaOperandos.pop()

        if tipoExp != Type.BOOL:
             raise Exception("Condicion no es de tipo BOOL")
        
        cuadruplos.append((Operator.GOTOF, res, None, None))
        pilaSaltos.append(len(cuadruplos)-1)

    def exitExit_condition(self, ctx):
        end = pilaSaltos.pop()
        print("end ", end)
        self.fill(end, len(cuadruplos))

    def exitExit_sino(self, ctx):
        cuadruplos.append((Operator.GOTOV, None, None, None))
        f = pilaSaltos.pop()
        pilaSaltos.append(len(cuadruplos)-1)
        self.fill(f, len(cuadruplos))

    def exitExit_while(self, ctx):
        pilaSaltos.append(len(cuadruplos))

    def exitExit_endwhile(self, ctx):
        end = pilaSaltos.pop()
        anterior = pilaSaltos.pop()

        cuadruplos.append((Operator.GOTOV, None, None, anterior))
        self.fill(end, len(cuadruplos))

    def exitContenido(self, ctx):
        global dirCte_str
        if ctx.STRING() is not None:
            cteStr = ctx.getText()
            if cteStr in constantes:
                address = constantes[cteStr]
            else:
                address = dirCte_str
                constantes[cteStr] = address
                dirCte_str = dirCte_str + 1
            pilaOperandos.append(address)
            pilaTipos.append(Type.STRING)

    def enterEscritura(self, ctx):
        pilaOperadores.append(Operator.PRINT)

    def exitEscritura(self, ctx):
        op = pilaOperadores.pop()
        res = pilaOperandos.pop()
        pilaTipos.pop()
        cuadruplos.append((op, None, None, res))

    def exitVar_id(self, ctx: LittleDuckParser.Var_idContext):
        # print(pending_type[-1])
        if ctx.ID() is not None:
            if(ctx.getText() in var_table):
                raise Exception("Esa variable ya existe!!")
            else:
                address = getAddressByType(pilaTipos[-1])
                var_table[ctx.getText()] = (pilaTipos[-1], address)

    def exitTipo(self, ctx):
        if ctx.INT() is not None:
            pilaTipos.append(Type.INT)
        elif ctx.FLOAT() is not None:
            pilaTipos.append(Type.FLOAT)
        
    def exitPrograma(self, ctx):
        print(var_table)

        for cuadruplo in cuadruplos:
            print(cuadruplo)

        print("si funciona :)")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LittleDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LittleDuckParser(stream)
    tree = parser.programa()

    printer = ProgramaListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
 
if __name__ == '__main__':
    main(sys.argv)
