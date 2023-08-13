from parser.parser import extract_rel_patterns_from_query


class CypherGuard():
    schema: str

    def __init__(self, schema) -> None:
        self.schema = schema
        pass

    def correct_query(self, input) -> str:
        output = extract_rel_patterns_from_query(input)
        return output


# test stuff
query = 'match (n:Person) match (n:Actor)-[a:ACTED_IN|DIRECTED*1..2]->(m:Movie)<-[:ACTED_IN*2]-() RETURN n,a,m'
guard = CypherGuard(schema='test')
output = guard.correct_query(query)
print(output)