
from antlr4 import *
from antlr4.InputStream import InputStream

from guard.generated.CypherLexer import CypherLexer
from guard.generated.CypherParser import CypherParser
from guard.generated.CypherParserVisitor import CypherParserVisitor
from guard.generated.CypherParserListener import CypherParserListener
from guard.parser.pattern_extractor import PatternExtractor

def extract_rel_patterns(input):
    input_stream = InputStream(input)
    lexer = CypherLexer(input_stream)
    lexer.removeErrorListeners() 
        
    token_stream = CommonTokenStream(lexer)
    parser = CypherParser(token_stream)
    parser.removeErrorListeners()

    listener = PatternExtractor(input)
    tree = parser.singleQueryOrCommand()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.node_patterns, listener.rel_patterns