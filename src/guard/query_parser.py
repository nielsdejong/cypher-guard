
from antlr4 import *
from antlr4.InputStream import InputStream
from guard.generated.CypherLexer import CypherLexer
from guard.generated.CypherParser import CypherParser
from guard.pattern_extractor import PatternExtractor


def extract_rel_patterns(input):
    """
    Takes a Cypher query 'input', and extracts node/relationship patterns from it.
    Parsing is done using the Antlr4 library and the official Cypher grammar file.
    Logical pattern inspired by https://github.com/Flitternie/GraphQ_Trans/blob/master/cypher/parser.py
    """
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
