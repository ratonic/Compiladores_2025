# Generated from IfElseLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IfElseLangParser import IfElseLangParser
else:
    from IfElseLangParser import IfElseLangParser

# This class defines a complete listener for a parse tree produced by IfElseLangParser.
class IfElseLangListener(ParseTreeListener):

    # Enter a parse tree produced by IfElseLangParser#program.
    def enterProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#program.
    def exitProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#statement.
    def enterStatement(self, ctx:IfElseLangParser.StatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#statement.
    def exitStatement(self, ctx:IfElseLangParser.StatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#assignment.
    def enterAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#assignment.
    def exitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#ifStatement.
    def enterIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#ifStatement.
    def exitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#condition.
    def enterCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#condition.
    def exitCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Variable.
    def enterVariable(self, ctx:IfElseLangParser.VariableContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Variable.
    def exitVariable(self, ctx:IfElseLangParser.VariableContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Number.
    def enterNumber(self, ctx:IfElseLangParser.NumberContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Number.
    def exitNumber(self, ctx:IfElseLangParser.NumberContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Parens.
    def enterParens(self, ctx:IfElseLangParser.ParensContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Parens.
    def exitParens(self, ctx:IfElseLangParser.ParensContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Arithmetic.
    def enterArithmetic(self, ctx:IfElseLangParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Arithmetic.
    def exitArithmetic(self, ctx:IfElseLangParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#operator.
    def enterOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#operator.
    def exitOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass



del IfElseLangParser