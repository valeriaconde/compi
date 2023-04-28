# Generated from LittleDuck.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LittleDuckParser import LittleDuckParser
else:
    from LittleDuckParser import LittleDuckParser

# This class defines a complete listener for a parse tree produced by LittleDuckParser.
class LittleDuckListener(ParseTreeListener):

    # Enter a parse tree produced by LittleDuckParser#programa.
    def enterPrograma(self, ctx:LittleDuckParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#programa.
    def exitPrograma(self, ctx:LittleDuckParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#vars.
    def enterVars(self, ctx:LittleDuckParser.VarsContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#vars.
    def exitVars(self, ctx:LittleDuckParser.VarsContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#pnvar.
    def enterPnvar(self, ctx:LittleDuckParser.PnvarContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#pnvar.
    def exitPnvar(self, ctx:LittleDuckParser.PnvarContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#var_id.
    def enterVar_id(self, ctx:LittleDuckParser.Var_idContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#var_id.
    def exitVar_id(self, ctx:LittleDuckParser.Var_idContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#cuerpo.
    def enterCuerpo(self, ctx:LittleDuckParser.CuerpoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#cuerpo.
    def exitCuerpo(self, ctx:LittleDuckParser.CuerpoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#tipo.
    def enterTipo(self, ctx:LittleDuckParser.TipoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#tipo.
    def exitTipo(self, ctx:LittleDuckParser.TipoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#estatuto.
    def enterEstatuto(self, ctx:LittleDuckParser.EstatutoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#estatuto.
    def exitEstatuto(self, ctx:LittleDuckParser.EstatutoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#asigna.
    def enterAsigna(self, ctx:LittleDuckParser.AsignaContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#asigna.
    def exitAsigna(self, ctx:LittleDuckParser.AsignaContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#asigna_var.
    def enterAsigna_var(self, ctx:LittleDuckParser.Asigna_varContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#asigna_var.
    def exitAsigna_var(self, ctx:LittleDuckParser.Asigna_varContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_equals.
    def enterExit_equals(self, ctx:LittleDuckParser.Exit_equalsContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_equals.
    def exitExit_equals(self, ctx:LittleDuckParser.Exit_equalsContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#expresion.
    def enterExpresion(self, ctx:LittleDuckParser.ExpresionContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#expresion.
    def exitExpresion(self, ctx:LittleDuckParser.ExpresionContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#h.
    def enterH(self, ctx:LittleDuckParser.HContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#h.
    def exitH(self, ctx:LittleDuckParser.HContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_morethan.
    def enterExit_morethan(self, ctx:LittleDuckParser.Exit_morethanContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_morethan.
    def exitExit_morethan(self, ctx:LittleDuckParser.Exit_morethanContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_lessthan.
    def enterExit_lessthan(self, ctx:LittleDuckParser.Exit_lessthanContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_lessthan.
    def exitExit_lessthan(self, ctx:LittleDuckParser.Exit_lessthanContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_not.
    def enterExit_not(self, ctx:LittleDuckParser.Exit_notContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_not.
    def exitExit_not(self, ctx:LittleDuckParser.Exit_notContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_exp.
    def enterExit_exp(self, ctx:LittleDuckParser.Exit_expContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_exp.
    def exitExit_exp(self, ctx:LittleDuckParser.Exit_expContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#condicion.
    def enterCondicion(self, ctx:LittleDuckParser.CondicionContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#condicion.
    def exitCondicion(self, ctx:LittleDuckParser.CondicionContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#m.
    def enterM(self, ctx:LittleDuckParser.MContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#m.
    def exitM(self, ctx:LittleDuckParser.MContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_openp.
    def enterExit_openp(self, ctx:LittleDuckParser.Exit_openpContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_openp.
    def exitExit_openp(self, ctx:LittleDuckParser.Exit_openpContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_closep.
    def enterExit_closep(self, ctx:LittleDuckParser.Exit_closepContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_closep.
    def exitExit_closep(self, ctx:LittleDuckParser.Exit_closepContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_si.
    def enterExit_si(self, ctx:LittleDuckParser.Exit_siContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_si.
    def exitExit_si(self, ctx:LittleDuckParser.Exit_siContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_sino.
    def enterExit_sino(self, ctx:LittleDuckParser.Exit_sinoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_sino.
    def exitExit_sino(self, ctx:LittleDuckParser.Exit_sinoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#ciclo.
    def enterCiclo(self, ctx:LittleDuckParser.CicloContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#ciclo.
    def exitCiclo(self, ctx:LittleDuckParser.CicloContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#escritura.
    def enterEscritura(self, ctx:LittleDuckParser.EscrituraContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#escritura.
    def exitEscritura(self, ctx:LittleDuckParser.EscrituraContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#k.
    def enterK(self, ctx:LittleDuckParser.KContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#k.
    def exitK(self, ctx:LittleDuckParser.KContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#w.
    def enterW(self, ctx:LittleDuckParser.WContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#w.
    def exitW(self, ctx:LittleDuckParser.WContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exp.
    def enterExp(self, ctx:LittleDuckParser.ExpContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exp.
    def exitExp(self, ctx:LittleDuckParser.ExpContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_plus.
    def enterExit_plus(self, ctx:LittleDuckParser.Exit_plusContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_plus.
    def exitExit_plus(self, ctx:LittleDuckParser.Exit_plusContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_minus.
    def enterExit_minus(self, ctx:LittleDuckParser.Exit_minusContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_minus.
    def exitExit_minus(self, ctx:LittleDuckParser.Exit_minusContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#termino.
    def enterTermino(self, ctx:LittleDuckParser.TerminoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#termino.
    def exitTermino(self, ctx:LittleDuckParser.TerminoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_times.
    def enterExit_times(self, ctx:LittleDuckParser.Exit_timesContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_times.
    def exitExit_times(self, ctx:LittleDuckParser.Exit_timesContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_division.
    def enterExit_division(self, ctx:LittleDuckParser.Exit_divisionContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_division.
    def exitExit_division(self, ctx:LittleDuckParser.Exit_divisionContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_termino.
    def enterExit_termino(self, ctx:LittleDuckParser.Exit_terminoContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_termino.
    def exitExit_termino(self, ctx:LittleDuckParser.Exit_terminoContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#exit_factor.
    def enterExit_factor(self, ctx:LittleDuckParser.Exit_factorContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#exit_factor.
    def exitExit_factor(self, ctx:LittleDuckParser.Exit_factorContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#factor.
    def enterFactor(self, ctx:LittleDuckParser.FactorContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#factor.
    def exitFactor(self, ctx:LittleDuckParser.FactorContext):
        pass


    # Enter a parse tree produced by LittleDuckParser#var_cte.
    def enterVar_cte(self, ctx:LittleDuckParser.Var_cteContext):
        pass

    # Exit a parse tree produced by LittleDuckParser#var_cte.
    def exitVar_cte(self, ctx:LittleDuckParser.Var_cteContext):
        pass



del LittleDuckParser