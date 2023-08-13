# Generated from data/CypherParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser

# This class defines a complete generic visitor for a parse tree produced by CypherParser.

class CypherParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CypherParser#statements.
    def visitStatements(self, ctx:CypherParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#statement.
    def visitStatement(self, ctx:CypherParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleQueryOrCommand.
    def visitSingleQueryOrCommand(self, ctx:CypherParser.SingleQueryOrCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleQueryOrCommandWithUseClause.
    def visitSingleQueryOrCommandWithUseClause(self, ctx:CypherParser.SingleQueryOrCommandWithUseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#periodicCommitQueryHintFailure.
    def visitPeriodicCommitQueryHintFailure(self, ctx:CypherParser.PeriodicCommitQueryHintFailureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#regularQuery.
    def visitRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#union.
    def visitUnion(self, ctx:CypherParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleQuery.
    def visitSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleQueryWithUseClause.
    def visitSingleQueryWithUseClause(self, ctx:CypherParser.SingleQueryWithUseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#clause.
    def visitClause(self, ctx:CypherParser.ClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#useClause.
    def visitUseClause(self, ctx:CypherParser.UseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#returnClause.
    def visitReturnClause(self, ctx:CypherParser.ReturnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#returnBody.
    def visitReturnBody(self, ctx:CypherParser.ReturnBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#returnItem.
    def visitReturnItem(self, ctx:CypherParser.ReturnItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#returnItems.
    def visitReturnItems(self, ctx:CypherParser.ReturnItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#orderItem.
    def visitOrderItem(self, ctx:CypherParser.OrderItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#skip.
    def visitSkip(self, ctx:CypherParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#limit.
    def visitLimit(self, ctx:CypherParser.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#whereClause.
    def visitWhereClause(self, ctx:CypherParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#withClause.
    def visitWithClause(self, ctx:CypherParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createClause.
    def visitCreateClause(self, ctx:CypherParser.CreateClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setClause.
    def visitSetClause(self, ctx:CypherParser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setItem.
    def visitSetItem(self, ctx:CypherParser.SetItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#removeClause.
    def visitRemoveClause(self, ctx:CypherParser.RemoveClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#removeItem.
    def visitRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#deleteClause.
    def visitDeleteClause(self, ctx:CypherParser.DeleteClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#matchClause.
    def visitMatchClause(self, ctx:CypherParser.MatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#matchMode.
    def visitMatchMode(self, ctx:CypherParser.MatchModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#hints.
    def visitHints(self, ctx:CypherParser.HintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#indexHintBody.
    def visitIndexHintBody(self, ctx:CypherParser.IndexHintBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mergeClause.
    def visitMergeClause(self, ctx:CypherParser.MergeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unwindClause.
    def visitUnwindClause(self, ctx:CypherParser.UnwindClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#callClause.
    def visitCallClause(self, ctx:CypherParser.CallClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#procedureName.
    def visitProcedureName(self, ctx:CypherParser.ProcedureNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#procedureArgument.
    def visitProcedureArgument(self, ctx:CypherParser.ProcedureArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#procedureResultItem.
    def visitProcedureResultItem(self, ctx:CypherParser.ProcedureResultItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#loadCSVClause.
    def visitLoadCSVClause(self, ctx:CypherParser.LoadCSVClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#foreachClause.
    def visitForeachClause(self, ctx:CypherParser.ForeachClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryClause.
    def visitSubqueryClause(self, ctx:CypherParser.SubqueryClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryInTransactionsParameters.
    def visitSubqueryInTransactionsParameters(self, ctx:CypherParser.SubqueryInTransactionsParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryInTransactionsBatchParameters.
    def visitSubqueryInTransactionsBatchParameters(self, ctx:CypherParser.SubqueryInTransactionsBatchParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryInTransactionsErrorParameters.
    def visitSubqueryInTransactionsErrorParameters(self, ctx:CypherParser.SubqueryInTransactionsErrorParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryInTransactionsReportParameters.
    def visitSubqueryInTransactionsReportParameters(self, ctx:CypherParser.SubqueryInTransactionsReportParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternList.
    def visitPatternList(self, ctx:CypherParser.PatternListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pattern.
    def visitPattern(self, ctx:CypherParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#quantifier.
    def visitQuantifier(self, ctx:CypherParser.QuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#anonymousPattern.
    def visitAnonymousPattern(self, ctx:CypherParser.AnonymousPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#shortestPathPattern.
    def visitShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#maybeQuantifiedRelationshipPattern.
    def visitMaybeQuantifiedRelationshipPattern(self, ctx:CypherParser.MaybeQuantifiedRelationshipPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternElement.
    def visitPatternElement(self, ctx:CypherParser.PatternElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pathPatternAtoms.
    def visitPathPatternAtoms(self, ctx:CypherParser.PathPatternAtomsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#selector.
    def visitSelector(self, ctx:CypherParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pathPatternNonEmpty.
    def visitPathPatternNonEmpty(self, ctx:CypherParser.PathPatternNonEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#nodePattern.
    def visitNodePattern(self, ctx:CypherParser.NodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parenthesizedPath.
    def visitParenthesizedPath(self, ctx:CypherParser.ParenthesizedPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#nodeLabels.
    def visitNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpressionPredicate.
    def visitLabelExpressionPredicate(self, ctx:CypherParser.LabelExpressionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelOrRelType.
    def visitLabelOrRelType(self, ctx:CypherParser.LabelOrRelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelOrRelTypes.
    def visitLabelOrRelTypes(self, ctx:CypherParser.LabelOrRelTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#properties.
    def visitProperties(self, ctx:CypherParser.PropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#relationshipPattern.
    def visitRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#leftArrow.
    def visitLeftArrow(self, ctx:CypherParser.LeftArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#arrowLine.
    def visitArrowLine(self, ctx:CypherParser.ArrowLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#rightArrow.
    def visitRightArrow(self, ctx:CypherParser.RightArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pathLength.
    def visitPathLength(self, ctx:CypherParser.PathLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pathLengthLiteral.
    def visitPathLengthLiteral(self, ctx:CypherParser.PathLengthLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression.
    def visitLabelExpression(self, ctx:CypherParser.LabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression4.
    def visitLabelExpression4(self, ctx:CypherParser.LabelExpression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression4Is.
    def visitLabelExpression4Is(self, ctx:CypherParser.LabelExpression4IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression3.
    def visitLabelExpression3(self, ctx:CypherParser.LabelExpression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression3Is.
    def visitLabelExpression3Is(self, ctx:CypherParser.LabelExpression3IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression2.
    def visitLabelExpression2(self, ctx:CypherParser.LabelExpression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression2Is.
    def visitLabelExpression2Is(self, ctx:CypherParser.LabelExpression2IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression1.
    def visitLabelExpression1(self, ctx:CypherParser.LabelExpression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelExpression1Is.
    def visitLabelExpression1Is(self, ctx:CypherParser.LabelExpression1IsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression.
    def visitExpression(self, ctx:CypherParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression12.
    def visitExpression12(self, ctx:CypherParser.Expression12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression11.
    def visitExpression11(self, ctx:CypherParser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression10.
    def visitExpression10(self, ctx:CypherParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression9.
    def visitExpression9(self, ctx:CypherParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression8.
    def visitExpression8(self, ctx:CypherParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression7.
    def visitExpression7(self, ctx:CypherParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#comparisonExpression6.
    def visitComparisonExpression6(self, ctx:CypherParser.ComparisonExpression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression6.
    def visitExpression6(self, ctx:CypherParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression5.
    def visitExpression5(self, ctx:CypherParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression4.
    def visitExpression4(self, ctx:CypherParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression3.
    def visitExpression3(self, ctx:CypherParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression2.
    def visitExpression2(self, ctx:CypherParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#postFix1.
    def visitPostFix1(self, ctx:CypherParser.PostFix1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#property.
    def visitProperty(self, ctx:CypherParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyExpression.
    def visitPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression1.
    def visitExpression1(self, ctx:CypherParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#NummericLiteral.
    def visitNummericLiteral(self, ctx:CypherParser.NummericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#StringsLiteral.
    def visitStringsLiteral(self, ctx:CypherParser.StringsLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#OtherLiteral.
    def visitOtherLiteral(self, ctx:CypherParser.OtherLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#BooleanLiteral.
    def visitBooleanLiteral(self, ctx:CypherParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#KeywordLiteral.
    def visitKeywordLiteral(self, ctx:CypherParser.KeywordLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#caseExpression.
    def visitCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listComprehension.
    def visitListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listComprehensionWhereAndBar.
    def visitListComprehensionWhereAndBar(self, ctx:CypherParser.ListComprehensionWhereAndBarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternComprehension.
    def visitPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternComprehensionPrefix.
    def visitPatternComprehensionPrefix(self, ctx:CypherParser.PatternComprehensionPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#reduceExpression.
    def visitReduceExpression(self, ctx:CypherParser.ReduceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#allExpression.
    def visitAllExpression(self, ctx:CypherParser.AllExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#anyExpression.
    def visitAnyExpression(self, ctx:CypherParser.AnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#noneExpression.
    def visitNoneExpression(self, ctx:CypherParser.NoneExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleExpression.
    def visitSingleExpression(self, ctx:CypherParser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternExpression.
    def visitPatternExpression(self, ctx:CypherParser.PatternExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#shortestPathExpression.
    def visitShortestPathExpression(self, ctx:CypherParser.ShortestPathExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapProjection.
    def visitMapProjection(self, ctx:CypherParser.MapProjectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapProjectionItem.
    def visitMapProjectionItem(self, ctx:CypherParser.MapProjectionItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#existsExpression.
    def visitExistsExpression(self, ctx:CypherParser.ExistsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#countExpression.
    def visitCountExpression(self, ctx:CypherParser.CountExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#collectExpression.
    def visitCollectExpression(self, ctx:CypherParser.CollectExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringLiteral.
    def visitStringLiteral(self, ctx:CypherParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#numberLiteral.
    def visitNumberLiteral(self, ctx:CypherParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#signedIntegerLiteral.
    def visitSignedIntegerLiteral(self, ctx:CypherParser.SignedIntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listLiteral.
    def visitListLiteral(self, ctx:CypherParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapLiteral.
    def visitMapLiteral(self, ctx:CypherParser.MapLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyKeyName.
    def visitPropertyKeyName(self, ctx:CypherParser.PropertyKeyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parameter.
    def visitParameter(self, ctx:CypherParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parameterName.
    def visitParameterName(self, ctx:CypherParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#functionInvocation.
    def visitFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#functionName.
    def visitFunctionName(self, ctx:CypherParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#functionArgument.
    def visitFunctionArgument(self, ctx:CypherParser.FunctionArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#namespace.
    def visitNamespace(self, ctx:CypherParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#variableList1.
    def visitVariableList1(self, ctx:CypherParser.VariableList1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#variable.
    def visitVariable(self, ctx:CypherParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicNameList1.
    def visitSymbolicNameList1(self, ctx:CypherParser.SymbolicNameList1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createCommand.
    def visitCreateCommand(self, ctx:CypherParser.CreateCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#command.
    def visitCommand(self, ctx:CypherParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#commandWithUseGraph.
    def visitCommandWithUseGraph(self, ctx:CypherParser.CommandWithUseGraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropCommand.
    def visitDropCommand(self, ctx:CypherParser.DropCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterCommand.
    def visitAlterCommand(self, ctx:CypherParser.AlterCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showCommand.
    def visitShowCommand(self, ctx:CypherParser.ShowCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#terminateCommand.
    def visitTerminateCommand(self, ctx:CypherParser.TerminateCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showAllCommand.
    def visitShowAllCommand(self, ctx:CypherParser.ShowAllCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showNodeCommand.
    def visitShowNodeCommand(self, ctx:CypherParser.ShowNodeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showRelationshipCommand.
    def visitShowRelationshipCommand(self, ctx:CypherParser.ShowRelationshipCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showRelCommand.
    def visitShowRelCommand(self, ctx:CypherParser.ShowRelCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showPropertyCommand.
    def visitShowPropertyCommand(self, ctx:CypherParser.ShowPropertyCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#yieldItem.
    def visitYieldItem(self, ctx:CypherParser.YieldItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#yieldClause.
    def visitYieldClause(self, ctx:CypherParser.YieldClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showIndexesAllowBrief.
    def visitShowIndexesAllowBrief(self, ctx:CypherParser.ShowIndexesAllowBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showIndexesNoBrief.
    def visitShowIndexesNoBrief(self, ctx:CypherParser.ShowIndexesNoBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showConstraintsAllowBriefAndYield.
    def visitShowConstraintsAllowBriefAndYield(self, ctx:CypherParser.ShowConstraintsAllowBriefAndYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showConstraintsAllowBrief.
    def visitShowConstraintsAllowBrief(self, ctx:CypherParser.ShowConstraintsAllowBriefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showConstraintsAllowYield.
    def visitShowConstraintsAllowYield(self, ctx:CypherParser.ShowConstraintsAllowYieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showProcedures.
    def visitShowProcedures(self, ctx:CypherParser.ShowProceduresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showFunctions.
    def visitShowFunctions(self, ctx:CypherParser.ShowFunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showTransactions.
    def visitShowTransactions(self, ctx:CypherParser.ShowTransactionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#terminateTransactions.
    def visitTerminateTransactions(self, ctx:CypherParser.TerminateTransactionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showOrTerminateTransactions.
    def visitShowOrTerminateTransactions(self, ctx:CypherParser.ShowOrTerminateTransactionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringsOrExpression.
    def visitStringsOrExpression(self, ctx:CypherParser.StringsOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showSettings.
    def visitShowSettings(self, ctx:CypherParser.ShowSettingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createConstraint.
    def visitCreateConstraint(self, ctx:CypherParser.CreateConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#cypherTypeName.
    def visitCypherTypeName(self, ctx:CypherParser.CypherTypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#constraintNodePattern.
    def visitConstraintNodePattern(self, ctx:CypherParser.ConstraintNodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#constraintRelPattern.
    def visitConstraintRelPattern(self, ctx:CypherParser.ConstraintRelPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createConstraintNodeCheck.
    def visitCreateConstraintNodeCheck(self, ctx:CypherParser.CreateConstraintNodeCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createConstraintRelCheck.
    def visitCreateConstraintRelCheck(self, ctx:CypherParser.CreateConstraintRelCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropConstraint.
    def visitDropConstraint(self, ctx:CypherParser.DropConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropConstraintNodeCheck.
    def visitDropConstraintNodeCheck(self, ctx:CypherParser.DropConstraintNodeCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createIndex.
    def visitCreateIndex(self, ctx:CypherParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#oldCreateIndex.
    def visitOldCreateIndex(self, ctx:CypherParser.OldCreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createIndex_.
    def visitCreateIndex_(self, ctx:CypherParser.CreateIndex_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createFulltextIndex.
    def visitCreateFulltextIndex(self, ctx:CypherParser.CreateFulltextIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createLookupIndex.
    def visitCreateLookupIndex(self, ctx:CypherParser.CreateLookupIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#lookupIndexFunctionName.
    def visitLookupIndexFunctionName(self, ctx:CypherParser.LookupIndexFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropIndex.
    def visitDropIndex(self, ctx:CypherParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyList.
    def visitPropertyList(self, ctx:CypherParser.PropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#renameCommand.
    def visitRenameCommand(self, ctx:CypherParser.RenameCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#grantCommand.
    def visitGrantCommand(self, ctx:CypherParser.GrantCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#revokeCommand.
    def visitRevokeCommand(self, ctx:CypherParser.RevokeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#enableServerCommand.
    def visitEnableServerCommand(self, ctx:CypherParser.EnableServerCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterServer.
    def visitAlterServer(self, ctx:CypherParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#renameServer.
    def visitRenameServer(self, ctx:CypherParser.RenameServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropServer.
    def visitDropServer(self, ctx:CypherParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showServers.
    def visitShowServers(self, ctx:CypherParser.ShowServersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#allocationCommand.
    def visitAllocationCommand(self, ctx:CypherParser.AllocationCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#deallocateDatabaseFromServers.
    def visitDeallocateDatabaseFromServers(self, ctx:CypherParser.DeallocateDatabaseFromServersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#reallocateDatabases.
    def visitReallocateDatabases(self, ctx:CypherParser.ReallocateDatabasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createRole.
    def visitCreateRole(self, ctx:CypherParser.CreateRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropRole.
    def visitDropRole(self, ctx:CypherParser.DropRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#renameRole.
    def visitRenameRole(self, ctx:CypherParser.RenameRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showRoles.
    def visitShowRoles(self, ctx:CypherParser.ShowRolesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#grantRole.
    def visitGrantRole(self, ctx:CypherParser.GrantRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#revokeRole.
    def visitRevokeRole(self, ctx:CypherParser.RevokeRoleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createUser.
    def visitCreateUser(self, ctx:CypherParser.CreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropUser.
    def visitDropUser(self, ctx:CypherParser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#renameUser.
    def visitRenameUser(self, ctx:CypherParser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterCurrentUser.
    def visitAlterCurrentUser(self, ctx:CypherParser.AlterCurrentUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterUser.
    def visitAlterUser(self, ctx:CypherParser.AlterUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setPassword.
    def visitSetPassword(self, ctx:CypherParser.SetPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#passwordExpression.
    def visitPasswordExpression(self, ctx:CypherParser.PasswordExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#passwordChangeRequired.
    def visitPasswordChangeRequired(self, ctx:CypherParser.PasswordChangeRequiredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#userStatus.
    def visitUserStatus(self, ctx:CypherParser.UserStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#homeDatabase.
    def visitHomeDatabase(self, ctx:CypherParser.HomeDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showUsers.
    def visitShowUsers(self, ctx:CypherParser.ShowUsersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showCurrentUser.
    def visitShowCurrentUser(self, ctx:CypherParser.ShowCurrentUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showSupportedPrivileges.
    def visitShowSupportedPrivileges(self, ctx:CypherParser.ShowSupportedPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showPrivileges.
    def visitShowPrivileges(self, ctx:CypherParser.ShowPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showRolePrivileges.
    def visitShowRolePrivileges(self, ctx:CypherParser.ShowRolePrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showUserPrivileges.
    def visitShowUserPrivileges(self, ctx:CypherParser.ShowUserPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#grantRoleManagement.
    def visitGrantRoleManagement(self, ctx:CypherParser.GrantRoleManagementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#revokeRoleManagement.
    def visitRevokeRoleManagement(self, ctx:CypherParser.RevokeRoleManagementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#roleManagementPrivilege.
    def visitRoleManagementPrivilege(self, ctx:CypherParser.RoleManagementPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#grantPrivilege.
    def visitGrantPrivilege(self, ctx:CypherParser.GrantPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#denyPrivilege.
    def visitDenyPrivilege(self, ctx:CypherParser.DenyPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#revokePrivilege.
    def visitRevokePrivilege(self, ctx:CypherParser.RevokePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#privilege.
    def visitPrivilege(self, ctx:CypherParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#allPrivilege.
    def visitAllPrivilege(self, ctx:CypherParser.AllPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#allPrivilegeType.
    def visitAllPrivilegeType(self, ctx:CypherParser.AllPrivilegeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#allPrivilegeTarget.
    def visitAllPrivilegeTarget(self, ctx:CypherParser.AllPrivilegeTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createPrivilege.
    def visitCreatePrivilege(self, ctx:CypherParser.CreatePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropPrivilege.
    def visitDropPrivilege(self, ctx:CypherParser.DropPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showPrivilege.
    def visitShowPrivilege(self, ctx:CypherParser.ShowPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setPrivilege.
    def visitSetPrivilege(self, ctx:CypherParser.SetPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#removePrivilege.
    def visitRemovePrivilege(self, ctx:CypherParser.RemovePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#writePrivilege.
    def visitWritePrivilege(self, ctx:CypherParser.WritePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#databasePrivilege.
    def visitDatabasePrivilege(self, ctx:CypherParser.DatabasePrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dbmsPrivilege.
    def visitDbmsPrivilege(self, ctx:CypherParser.DbmsPrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#executeFunctionQualifier.
    def visitExecuteFunctionQualifier(self, ctx:CypherParser.ExecuteFunctionQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#executeProcedureQualifier.
    def visitExecuteProcedureQualifier(self, ctx:CypherParser.ExecuteProcedureQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#settingQualifier.
    def visitSettingQualifier(self, ctx:CypherParser.SettingQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#globs.
    def visitGlobs(self, ctx:CypherParser.GlobsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#qualifiedGraphPrivilegesWithProperty.
    def visitQualifiedGraphPrivilegesWithProperty(self, ctx:CypherParser.QualifiedGraphPrivilegesWithPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#qualifiedGraphPrivileges.
    def visitQualifiedGraphPrivileges(self, ctx:CypherParser.QualifiedGraphPrivilegesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#labelResource.
    def visitLabelResource(self, ctx:CypherParser.LabelResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyResource.
    def visitPropertyResource(self, ctx:CypherParser.PropertyResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#graphQualifier.
    def visitGraphQualifier(self, ctx:CypherParser.GraphQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createDatabase.
    def visitCreateDatabase(self, ctx:CypherParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#options_.
    def visitOptions_(self, ctx:CypherParser.Options_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createCompositeDatabase.
    def visitCreateCompositeDatabase(self, ctx:CypherParser.CreateCompositeDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropDatabase.
    def visitDropDatabase(self, ctx:CypherParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterDatabase.
    def visitAlterDatabase(self, ctx:CypherParser.AlterDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#startDatabase.
    def visitStartDatabase(self, ctx:CypherParser.StartDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stopDatabase.
    def visitStopDatabase(self, ctx:CypherParser.StopDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#waitClause.
    def visitWaitClause(self, ctx:CypherParser.WaitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showDatabase.
    def visitShowDatabase(self, ctx:CypherParser.ShowDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#databaseScopeList.
    def visitDatabaseScopeList(self, ctx:CypherParser.DatabaseScopeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#graphScopeList.
    def visitGraphScopeList(self, ctx:CypherParser.GraphScopeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createAlias.
    def visitCreateAlias(self, ctx:CypherParser.CreateAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#dropAlias.
    def visitDropAlias(self, ctx:CypherParser.DropAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#alterAlias.
    def visitAlterAlias(self, ctx:CypherParser.AlterAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#showAliases.
    def visitShowAliases(self, ctx:CypherParser.ShowAliasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicAliasNameList.
    def visitSymbolicAliasNameList(self, ctx:CypherParser.SymbolicAliasNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicAliasName.
    def visitSymbolicAliasName(self, ctx:CypherParser.SymbolicAliasNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicNameOrStringParameterList.
    def visitSymbolicNameOrStringParameterList(self, ctx:CypherParser.SymbolicNameOrStringParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicNameOrStringParameter.
    def visitSymbolicNameOrStringParameter(self, ctx:CypherParser.SymbolicNameOrStringParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#glob.
    def visitGlob(self, ctx:CypherParser.GlobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#globRecursive.
    def visitGlobRecursive(self, ctx:CypherParser.GlobRecursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#globPart.
    def visitGlobPart(self, ctx:CypherParser.GlobPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringImage.
    def visitStringImage(self, ctx:CypherParser.StringImageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringList.
    def visitStringList(self, ctx:CypherParser.StringListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringToken.
    def visitStringToken(self, ctx:CypherParser.StringTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringOrParameter.
    def visitStringOrParameter(self, ctx:CypherParser.StringOrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapOrParameter.
    def visitMapOrParameter(self, ctx:CypherParser.MapOrParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#map.
    def visitMap(self, ctx:CypherParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicNamePositions.
    def visitSymbolicNamePositions(self, ctx:CypherParser.SymbolicNamePositionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicNameString.
    def visitSymbolicNameString(self, ctx:CypherParser.SymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#escapedSymbolicNameString.
    def visitEscapedSymbolicNameString(self, ctx:CypherParser.EscapedSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unescapedSymbolicNameString.
    def visitUnescapedSymbolicNameString(self, ctx:CypherParser.UnescapedSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbolicLabelNameString.
    def visitSymbolicLabelNameString(self, ctx:CypherParser.SymbolicLabelNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unescapedLabelSymbolicNameString.
    def visitUnescapedLabelSymbolicNameString(self, ctx:CypherParser.UnescapedLabelSymbolicNameStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#endOfFile.
    def visitEndOfFile(self, ctx:CypherParser.EndOfFileContext):
        return self.visitChildren(ctx)



del CypherParser