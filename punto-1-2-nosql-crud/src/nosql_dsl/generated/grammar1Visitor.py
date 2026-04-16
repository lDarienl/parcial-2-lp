# Generated from /home/ubuntu/Darien/LenguajesProgramacion/parcial-2-lp/punto-1-2-nosql-crud/grammar/grammar1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammar1Parser import grammar1Parser
else:
    from grammar1Parser import grammar1Parser

# This class defines a complete generic visitor for a parse tree produced by grammar1Parser.

class grammar1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammar1Parser#programa.
    def visitPrograma(self, ctx:grammar1Parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#instruccion.
    def visitInstruccion(self, ctx:grammar1Parser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#createStmt.
    def visitCreateStmt(self, ctx:grammar1Parser.CreateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#readStmt.
    def visitReadStmt(self, ctx:grammar1Parser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#updateStmt.
    def visitUpdateStmt(self, ctx:grammar1Parser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#deleteStmt.
    def visitDeleteStmt(self, ctx:grammar1Parser.DeleteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#objeto.
    def visitObjeto(self, ctx:grammar1Parser.ObjetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#par.
    def visitPar(self, ctx:grammar1Parser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#clave.
    def visitClave(self, ctx:grammar1Parser.ClaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#array.
    def visitArray(self, ctx:grammar1Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#valor.
    def visitValor(self, ctx:grammar1Parser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#condiciones.
    def visitCondiciones(self, ctx:grammar1Parser.CondicionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#expr.
    def visitExpr(self, ctx:grammar1Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#andExpr.
    def visitAndExpr(self, ctx:grammar1Parser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#notExpr.
    def visitNotExpr(self, ctx:grammar1Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#primaryExpr.
    def visitPrimaryExpr(self, ctx:grammar1Parser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#comparacion.
    def visitComparacion(self, ctx:grammar1Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammar1Parser#opComp.
    def visitOpComp(self, ctx:grammar1Parser.OpCompContext):
        return self.visitChildren(ctx)



del grammar1Parser