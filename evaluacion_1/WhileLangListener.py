# Generated from WhileLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#statement.
    def enterStatement(self, ctx:WhileLangParser.StatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#statement.
    def exitStatement(self, ctx:WhileLangParser.StatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStatement.
    def enterIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStatement.
    def exitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#breakStatement.
    def enterBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#breakStatement.
    def exitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#continueStatement.
    def enterContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#continueStatement.
    def exitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#condition.
    def enterCondition(self, ctx:WhileLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#condition.
    def exitCondition(self, ctx:WhileLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Variable.
    def enterVariable(self, ctx:WhileLangParser.VariableContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Variable.
    def exitVariable(self, ctx:WhileLangParser.VariableContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Number.
    def enterNumber(self, ctx:WhileLangParser.NumberContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Number.
    def exitNumber(self, ctx:WhileLangParser.NumberContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Parens.
    def enterParens(self, ctx:WhileLangParser.ParensContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Parens.
    def exitParens(self, ctx:WhileLangParser.ParensContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Arithmetic.
    def enterArithmetic(self, ctx:WhileLangParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Arithmetic.
    def exitArithmetic(self, ctx:WhileLangParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by WhileLangParser#operator.
    def enterOperator(self, ctx:WhileLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by WhileLangParser#operator.
    def exitOperator(self, ctx:WhileLangParser.OperatorContext):
        pass



del WhileLangParser