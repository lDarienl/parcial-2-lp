# Generated from grammar/grammar1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammar1Parser import grammar1Parser
else:
    from grammar1Parser import grammar1Parser

# This class defines a complete listener for a parse tree produced by grammar1Parser.
class grammar1Listener(ParseTreeListener):

    # Enter a parse tree produced by grammar1Parser#programa.
    def enterPrograma(self, ctx:grammar1Parser.ProgramaContext):
        pass

    # Exit a parse tree produced by grammar1Parser#programa.
    def exitPrograma(self, ctx:grammar1Parser.ProgramaContext):
        pass


    # Enter a parse tree produced by grammar1Parser#instruccion.
    def enterInstruccion(self, ctx:grammar1Parser.InstruccionContext):
        pass

    # Exit a parse tree produced by grammar1Parser#instruccion.
    def exitInstruccion(self, ctx:grammar1Parser.InstruccionContext):
        pass


    # Enter a parse tree produced by grammar1Parser#createStmt.
    def enterCreateStmt(self, ctx:grammar1Parser.CreateStmtContext):
        pass

    # Exit a parse tree produced by grammar1Parser#createStmt.
    def exitCreateStmt(self, ctx:grammar1Parser.CreateStmtContext):
        pass


    # Enter a parse tree produced by grammar1Parser#readStmt.
    def enterReadStmt(self, ctx:grammar1Parser.ReadStmtContext):
        pass

    # Exit a parse tree produced by grammar1Parser#readStmt.
    def exitReadStmt(self, ctx:grammar1Parser.ReadStmtContext):
        pass


    # Enter a parse tree produced by grammar1Parser#updateStmt.
    def enterUpdateStmt(self, ctx:grammar1Parser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by grammar1Parser#updateStmt.
    def exitUpdateStmt(self, ctx:grammar1Parser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by grammar1Parser#deleteStmt.
    def enterDeleteStmt(self, ctx:grammar1Parser.DeleteStmtContext):
        pass

    # Exit a parse tree produced by grammar1Parser#deleteStmt.
    def exitDeleteStmt(self, ctx:grammar1Parser.DeleteStmtContext):
        pass


    # Enter a parse tree produced by grammar1Parser#objeto.
    def enterObjeto(self, ctx:grammar1Parser.ObjetoContext):
        pass

    # Exit a parse tree produced by grammar1Parser#objeto.
    def exitObjeto(self, ctx:grammar1Parser.ObjetoContext):
        pass


    # Enter a parse tree produced by grammar1Parser#par.
    def enterPar(self, ctx:grammar1Parser.ParContext):
        pass

    # Exit a parse tree produced by grammar1Parser#par.
    def exitPar(self, ctx:grammar1Parser.ParContext):
        pass


    # Enter a parse tree produced by grammar1Parser#clave.
    def enterClave(self, ctx:grammar1Parser.ClaveContext):
        pass

    # Exit a parse tree produced by grammar1Parser#clave.
    def exitClave(self, ctx:grammar1Parser.ClaveContext):
        pass


    # Enter a parse tree produced by grammar1Parser#array.
    def enterArray(self, ctx:grammar1Parser.ArrayContext):
        pass

    # Exit a parse tree produced by grammar1Parser#array.
    def exitArray(self, ctx:grammar1Parser.ArrayContext):
        pass


    # Enter a parse tree produced by grammar1Parser#valor.
    def enterValor(self, ctx:grammar1Parser.ValorContext):
        pass

    # Exit a parse tree produced by grammar1Parser#valor.
    def exitValor(self, ctx:grammar1Parser.ValorContext):
        pass


    # Enter a parse tree produced by grammar1Parser#condiciones.
    def enterCondiciones(self, ctx:grammar1Parser.CondicionesContext):
        pass

    # Exit a parse tree produced by grammar1Parser#condiciones.
    def exitCondiciones(self, ctx:grammar1Parser.CondicionesContext):
        pass


    # Enter a parse tree produced by grammar1Parser#expr.
    def enterExpr(self, ctx:grammar1Parser.ExprContext):
        pass

    # Exit a parse tree produced by grammar1Parser#expr.
    def exitExpr(self, ctx:grammar1Parser.ExprContext):
        pass


    # Enter a parse tree produced by grammar1Parser#andExpr.
    def enterAndExpr(self, ctx:grammar1Parser.AndExprContext):
        pass

    # Exit a parse tree produced by grammar1Parser#andExpr.
    def exitAndExpr(self, ctx:grammar1Parser.AndExprContext):
        pass


    # Enter a parse tree produced by grammar1Parser#notExpr.
    def enterNotExpr(self, ctx:grammar1Parser.NotExprContext):
        pass

    # Exit a parse tree produced by grammar1Parser#notExpr.
    def exitNotExpr(self, ctx:grammar1Parser.NotExprContext):
        pass


    # Enter a parse tree produced by grammar1Parser#primaryExpr.
    def enterPrimaryExpr(self, ctx:grammar1Parser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by grammar1Parser#primaryExpr.
    def exitPrimaryExpr(self, ctx:grammar1Parser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by grammar1Parser#comparacion.
    def enterComparacion(self, ctx:grammar1Parser.ComparacionContext):
        pass

    # Exit a parse tree produced by grammar1Parser#comparacion.
    def exitComparacion(self, ctx:grammar1Parser.ComparacionContext):
        pass


    # Enter a parse tree produced by grammar1Parser#opComp.
    def enterOpComp(self, ctx:grammar1Parser.OpCompContext):
        pass

    # Exit a parse tree produced by grammar1Parser#opComp.
    def exitOpComp(self, ctx:grammar1Parser.OpCompContext):
        pass



del grammar1Parser