
from antlr4 import *
from antlr4.InputStream import InputStream

from parser.generated.CypherLexer import CypherLexer
from parser.generated.CypherParser import CypherParser
from parser.generated.CypherParserVisitor import CypherParserVisitor
from parser.generated.CypherParserListener import CypherParserListener
from parser.pattern_extractor import PatternExtractor

def extract_rel_patterns_from_query(input):
    input_stream = InputStream(input)
    lexer = CypherLexer(input_stream)
    lexer.removeErrorListeners() 
        
    token_stream = CommonTokenStream(lexer)
    parser = CypherParser(token_stream)
    parser.removeErrorListeners()

    listener = PatternExtractor()
    tree = parser.singleQueryOrCommand()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print(listener.node_patterns)
    print(listener.rel_patterns)
    return